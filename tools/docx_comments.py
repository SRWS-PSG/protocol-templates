"""Inject anchored Word comments into a .docx.

When the resulting docx is uploaded to Google Drive with auto-conversion,
each Word comment becomes a proper anchored Google Docs comment. This is the
robust path: Drive's anchored-comment JSON for Docs is undocumented and
empirically doesn't resolve text ranges, so we let the docx import handle it.

API:
    inject_comments(docx_in, docx_out, comments, author="SRWS-PSG")
        comments: list of dicts with keys:
            anchor   (str)   text to wrap (substring of paragraph text)
            body     (str)   comment body
            occurrence (int, optional, default 1)

Returns a list of (comment_dict, matched|None) tuples so the caller can warn
about unresolved anchors.
"""

from __future__ import annotations

import re
import shutil
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
W = f"{{{W_NS}}}"
R = f"{{{R_NS}}}"
CT = f"{{{CT_NS}}}"

# Register so ElementTree writes back with `w:`/`r:` prefixes.
ET.register_namespace("w", W_NS)
ET.register_namespace("r", R_NS)
ET.register_namespace("", CT_NS)


@dataclass
class _PendingComment:
    cid: int
    anchor: str
    body: str
    occurrence: int = 1


def _candidate_anchors(anchor: str) -> list[str]:
    """Pandoc drops `#` and emphasis markers when converting to docx."""
    out = [anchor]
    stripped = anchor.lstrip()
    if stripped.startswith("#"):
        s = stripped
        while s.startswith("#"):
            s = s[1:]
        s = s.lstrip()
        if s:
            out.append(s)
    if (
        len(stripped) >= 2
        and stripped.startswith("*")
        and stripped.endswith("*")
        and not stripped.startswith("**")
    ):
        out.append(stripped[1:-1])
    return out


def _t_text(t_elem: ET.Element) -> str:
    return t_elem.text or ""


def _make_t(text: str, preserve_space: bool = True) -> ET.Element:
    t = ET.Element(f"{W}t")
    if preserve_space:
        t.set(f"{{{ET.register_namespace.__module__.split('.')[0]}}}space", "preserve")  # noqa
    t.text = text
    return t


def _make_run_like(orig_run: ET.Element, text: str) -> ET.Element:
    """Clone a <w:r> but with new text content, preserving <w:rPr>."""
    new_r = ET.Element(f"{W}r")
    rpr = orig_run.find(f"{W}rPr")
    if rpr is not None:
        new_r.append(_clone(rpr))
    t = ET.SubElement(new_r, f"{W}t")
    # preserve whitespace
    t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text
    return new_r


def _clone(elem: ET.Element) -> ET.Element:
    new = ET.Element(elem.tag, elem.attrib)
    new.text = elem.text
    new.tail = elem.tail
    for child in elem:
        new.append(_clone(child))
    return new


def _comment_reference_run(cid: int) -> ET.Element:
    r = ET.Element(f"{W}r")
    rpr = ET.SubElement(r, f"{W}rPr")
    rstyle = ET.SubElement(rpr, f"{W}rStyle")
    rstyle.set(f"{W}val", "CommentReference")
    ref = ET.SubElement(r, f"{W}commentReference")
    ref.set(f"{W}id", str(cid))
    return r


def _try_anchor_in_paragraph(
    paragraph: ET.Element, anchor: str, occurrence_remaining: int
) -> tuple[int, int, int] | None:
    """Find anchor in this paragraph's concatenated text.

    Returns (match_start, match_end, occurrences_consumed) within concatenated text,
    or None if the anchor doesn't occur enough times here.
    """
    runs = paragraph.findall(f"{W}r")
    texts: list[tuple[ET.Element, ET.Element, str]] = []  # (run, t-elem, text)
    parts: list[str] = []
    for r in runs:
        for t in r.findall(f"{W}t"):
            parts.append(_t_text(t))
            texts.append((r, t, _t_text(t)))
    full = "".join(parts)

    start = -1
    consumed = 0
    while consumed < occurrence_remaining:
        start = full.find(anchor, start + 1)
        if start < 0:
            return None
        consumed += 1
    return start, start + len(anchor), consumed


def _wrap_anchor_in_paragraph(
    paragraph: ET.Element, anchor: str, match_start: int, match_end: int, cid: int
) -> None:
    """Insert commentRangeStart, commentRangeEnd, commentReference around match_start..match_end
    within the paragraph's text, splitting runs as needed.
    """
    children = list(paragraph)
    # Build a flat list of (child-index-in-paragraph, run, t-elem, text, abs-start)
    abs_pos = 0
    locations: list[tuple[int, ET.Element, ET.Element, str, int]] = []
    for idx, child in enumerate(children):
        if child.tag == f"{W}r":
            for t in child.findall(f"{W}t"):
                txt = _t_text(t)
                locations.append((idx, child, t, txt, abs_pos))
                abs_pos += len(txt)

    # Identify which (run, t) contains match_start and match_end
    start_loc = None
    end_loc = None
    for loc in locations:
        idx, run, t, txt, ap = loc
        if ap <= match_start < ap + len(txt) or (ap == match_start and len(txt) == 0):
            start_loc = loc
        if ap < match_end <= ap + len(txt):
            end_loc = loc
        if start_loc and end_loc:
            break

    if not start_loc or not end_loc:
        return

    # Strategy:
    #  1. Split the start run's <w:t> at (match_start - ap_start) into "before" and "after_start".
    #  2. Split the end run's <w:t> at (match_end - ap_end) into "before_end" and "after".
    #  3. Insert commentRangeStart between the "before" run and "after_start" run.
    #  4. Insert commentRangeEnd + commentReference between "before_end" run and "after" run.
    #
    # If start and end fall in the same run, we end up with three pieces: before / anchor / after.

    s_idx, s_run, s_t, s_txt, s_ap = start_loc
    e_idx, e_run, e_t, e_txt, e_ap = end_loc

    if s_run is e_run:
        rel_start = match_start - s_ap
        rel_end = match_end - s_ap
        before_text = s_txt[:rel_start]
        anchor_text = s_txt[rel_start:rel_end]
        after_text = s_txt[rel_end:]

        # Replace s_run with up to three new runs, plus commentRangeStart/End + reference between them.
        new_elems: list[ET.Element] = []
        if before_text:
            new_elems.append(_make_run_like(s_run, before_text))
        crs = ET.Element(f"{W}commentRangeStart")
        crs.set(f"{W}id", str(cid))
        new_elems.append(crs)
        new_elems.append(_make_run_like(s_run, anchor_text))
        cre = ET.Element(f"{W}commentRangeEnd")
        cre.set(f"{W}id", str(cid))
        new_elems.append(cre)
        new_elems.append(_comment_reference_run(cid))
        if after_text:
            new_elems.append(_make_run_like(s_run, after_text))

        # Splice into paragraph
        pos = list(paragraph).index(s_run)
        paragraph.remove(s_run)
        for offset, el in enumerate(new_elems):
            paragraph.insert(pos + offset, el)
        return

    # Different runs: split start run's text at rel_start, end run's text at rel_end.
    rel_start = match_start - s_ap
    rel_end = match_end - e_ap

    s_before = s_txt[:rel_start]
    s_after = s_txt[rel_start:]
    e_before = e_txt[:rel_end]
    e_after = e_txt[rel_end:]

    # Replace start run with: maybe-before-run, commentRangeStart, after-run
    pos = list(paragraph).index(s_run)
    paragraph.remove(s_run)
    new_start_elems: list[ET.Element] = []
    if s_before:
        new_start_elems.append(_make_run_like(s_run, s_before))
    crs = ET.Element(f"{W}commentRangeStart")
    crs.set(f"{W}id", str(cid))
    new_start_elems.append(crs)
    if s_after:
        new_start_elems.append(_make_run_like(s_run, s_after))
    for offset, el in enumerate(new_start_elems):
        paragraph.insert(pos + offset, el)

    # Replace end run with: before-run, commentRangeEnd, commentReference, maybe-after-run
    pos = list(paragraph).index(e_run)
    paragraph.remove(e_run)
    new_end_elems: list[ET.Element] = []
    if e_before:
        new_end_elems.append(_make_run_like(e_run, e_before))
    cre = ET.Element(f"{W}commentRangeEnd")
    cre.set(f"{W}id", str(cid))
    new_end_elems.append(cre)
    new_end_elems.append(_comment_reference_run(cid))
    if e_after:
        new_end_elems.append(_make_run_like(e_run, e_after))
    for offset, el in enumerate(new_end_elems):
        paragraph.insert(pos + offset, el)


def _build_comments_xml(comments: list[_PendingComment], author: str) -> bytes:
    root = ET.Element(f"{W}comments")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for pc in comments:
        c = ET.SubElement(root, f"{W}comment")
        c.set(f"{W}id", str(pc.cid))
        c.set(f"{W}author", author)
        c.set(f"{W}date", now)
        c.set(f"{W}initials", "")
        for line in pc.body.splitlines() or [""]:
            p = ET.SubElement(c, f"{W}p")
            r = ET.SubElement(p, f"{W}r")
            t = ET.SubElement(r, f"{W}t")
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            t.text = line
    return b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n' + ET.tostring(
        root, encoding="utf-8"
    )


def _patch_content_types(types_xml: bytes) -> bytes:
    text = types_xml.decode("utf-8")
    if "wordprocessingml.comments+xml" in text:
        return types_xml
    override = (
        '<Override PartName="/word/comments.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
    )
    return text.replace("</Types>", override + "</Types>").encode("utf-8")


def _patch_doc_rels(rels_xml: bytes) -> bytes:
    text = rels_xml.decode("utf-8")
    if 'Target="comments.xml"' in text:
        return rels_xml
    # find a free rId
    used = set(re.findall(r'Id="(rId\d+)"', text))
    n = 1
    while f"rId{n}" in used:
        n += 1
    new_rel = (
        f'<Relationship Id="rId{n}" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" '
        'Target="comments.xml"/>'
    )
    return text.replace("</Relationships>", new_rel + "</Relationships>").encode("utf-8")


def inject_comments(
    docx_in: Path,
    docx_out: Path,
    comments: list[dict],
    author: str = "SRWS-PSG",
) -> list[tuple[dict, str | None]]:
    """Inject Word comments into docx_in and write to docx_out.

    `comments` is a list of dicts with keys: anchor (str), body (str),
    optional occurrence (int, default 1), and optional id (passed through).
    Returns [(comment_dict, matched_anchor_or_None), ...].
    """
    with zipfile.ZipFile(docx_in) as zin:
        files = {n: zin.read(n) for n in zin.namelist()}

    doc_root = ET.fromstring(files["word/document.xml"])
    body = doc_root.find(f"{W}body")
    if body is None:
        raise RuntimeError("no <w:body> found in document.xml")

    pending: list[_PendingComment] = []
    results: list[tuple[dict, str | None]] = []
    next_cid = 0

    for spec in comments:
        anchor = spec["anchor"]
        body_text = spec["body"]
        target_occurrence = int(spec.get("occurrence", 1))

        matched_anchor: str | None = None
        match_loc: tuple[ET.Element, int, int] | None = None

        # Multiple comments may share the same anchor + occurrence; docx allows
        # overlapping comment ranges, so we look up the literal occurrence the
        # user requested every time and let the comment ranges stack.
        for candidate in _candidate_anchors(anchor):
            running = 0
            for para in body.iter(f"{W}p"):
                concat = "".join(_t_text(t) for t in para.iter(f"{W}t"))
                count_in_para = concat.count(candidate)
                if count_in_para == 0:
                    continue
                if running + count_in_para >= target_occurrence:
                    nth_in_para = target_occurrence - running
                    pos = -1
                    for _ in range(nth_in_para):
                        pos = concat.find(candidate, pos + 1)
                    match_loc = (para, pos, pos + len(candidate))
                    matched_anchor = candidate
                    break
                running += count_in_para
            if match_loc:
                break

        if match_loc is None:
            results.append((spec, None))
            continue

        para, m_start, m_end = match_loc
        _wrap_anchor_in_paragraph(para, matched_anchor, m_start, m_end, next_cid)
        pending.append(_PendingComment(cid=next_cid, anchor=anchor, body=body_text))
        results.append((spec, matched_anchor))
        next_cid += 1

    # Serialize modified document.xml
    files["word/document.xml"] = (
        b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        + ET.tostring(doc_root, encoding="utf-8")
    )

    # Build comments.xml
    if pending:
        files["word/comments.xml"] = _build_comments_xml(pending, author)
        files["[Content_Types].xml"] = _patch_content_types(files["[Content_Types].xml"])
        files["word/_rels/document.xml.rels"] = _patch_doc_rels(
            files["word/_rels/document.xml.rels"]
        )

    docx_out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(docx_out, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)

    return results
