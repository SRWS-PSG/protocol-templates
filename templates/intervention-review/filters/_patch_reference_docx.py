"""Patch reference.docx with:
  - default body fonts: Times New Roman (ASCII) + MS Mincho (East Asian)
  - heading fonts (H1-H9): Arial (ASCII) + Yu Gothic (East Asian)
  - default East Asian language: ja-JP (so Word treats body text as Japanese)
  - default line spacing 1.5
  - 'Note' (paragraph) and 'Placeholder' (character) styles in light blue
    (#4FC3F7) — matching the HTML CSS.

Idempotent: re-running on an already patched file will overwrite cleanly
because we regenerate from the bundled default each time via pandoc.

This reference.docx is shared by both intervention-review and
scoping-review templates (their build.ps1 scripts both point here).
"""
from __future__ import annotations

import re
import shutil
import subprocess
import zipfile
from pathlib import Path

HERE = Path(__file__).parent
REF = HERE / "reference.docx"
COLOR = "4FC3F7"  # light blue
ASCII_FONT = "Times New Roman"
EA_FONT = "MS Mincho"
HEADING_ASCII_FONT = "Arial"
HEADING_EA_FONT = "Yu Gothic"
EA_LANG = "ja-JP"
# Word stores line spacing in 240ths of a line for "auto" lineRule.
# 1.5 lines = 360.
LINE_SPACING = "360"

NOTE_STYLE = f'''  <w:style w:type="paragraph" w:customStyle="1" w:styleId="Note">
    <w:name w:val="Note" />
    <w:basedOn w:val="Normal" />
    <w:qFormat />
    <w:pPr>
      <w:pBdr>
        <w:left w:val="single" w:sz="18" w:space="6" w:color="{COLOR}" />
      </w:pBdr>
    </w:pPr>
    <w:rPr>
      <w:color w:val="{COLOR}" />
    </w:rPr>
  </w:style>
'''

PLACEHOLDER_STYLE = f'''  <w:style w:type="character" w:customStyle="1" w:styleId="Placeholder">
    <w:name w:val="Placeholder" />
    <w:qFormat />
    <w:rPr>
      <w:b />
      <w:color w:val="{COLOR}" />
    </w:rPr>
  </w:style>
'''

NOTE_INLINE_STYLE = f'''  <w:style w:type="character" w:customStyle="1" w:styleId="NoteInline">
    <w:name w:val="NoteInline" />
    <w:qFormat />
    <w:rPr>
      <w:color w:val="{COLOR}" />
    </w:rPr>
  </w:style>
'''

# Paragraph style for list items inside a Note blockquote.
# Inherits from Compact so list-item spacing stays tight, but adds the
# same left border as Note (so the cyan bar continues through the list)
# and keepNext so consecutive items try to avoid splitting at page breaks.
NOTE_LIST_PARAGRAPH_STYLE = f'''  <w:style w:type="paragraph" w:customStyle="1" w:styleId="NoteListParagraph">
    <w:name w:val="NoteListParagraph" />
    <w:basedOn w:val="Compact" />
    <w:qFormat />
    <w:pPr>
      <w:pBdr>
        <w:left w:val="single" w:sz="18" w:space="6" w:color="{COLOR}" />
      </w:pBdr>
      <w:keepNext />
    </w:pPr>
    <w:rPr>
      <w:color w:val="{COLOR}" />
    </w:rPr>
  </w:style>
'''


def _ensure_default_reference() -> None:
    """Always regenerate from pandoc's bundled default so patches are idempotent."""
    subprocess.run(
        ["pandoc", "-o", str(REF), "--print-default-data-file", "reference.docx"],
        check=True,
    )


def _patch_styles_xml(xml: str) -> str:
    # 1. Replace the default rFonts in docDefaults > rPrDefault with our fonts.
    xml = re.sub(
        r'<w:rPrDefault>\s*<w:rPr>\s*<w:rFonts[^/]*/>',
        (
            '<w:rPrDefault><w:rPr>'
            f'<w:rFonts w:ascii="{ASCII_FONT}" w:hAnsi="{ASCII_FONT}" '
            f'w:eastAsia="{EA_FONT}" w:cs="{ASCII_FONT}"/>'
        ),
        xml,
        count=1,
    )

    # 1b. Set default East Asian language to ja-JP so Word treats body text
    #     as Japanese (pandoc's default is zh-CN).
    xml = re.sub(
        r'(<w:lang\b[^/]*?\bw:eastAsia=")[^"]*(")',
        rf'\g<1>{EA_LANG}\g<2>',
        xml,
        count=1,
    )

    # 1c. Override heading fonts (H1-H9) to gothic (Arial / Yu Gothic).
    #     Pandoc's default headings use majorHAnsi / majorEastAsia themes,
    #     which fall back to body fonts (Times New Roman / MS Mincho).
    #     For Japanese protocol documents we want headings in gothic.
    heading_fonts_tag = (
        f'<w:rFonts w:ascii="{HEADING_ASCII_FONT}" '
        f'w:hAnsi="{HEADING_ASCII_FONT}" '
        f'w:eastAsia="{HEADING_EA_FONT}" '
        f'w:cs="{HEADING_ASCII_FONT}"/>'
    )
    for level in range(1, 10):
        # Replace the first <w:rFonts .../> inside this Heading style block.
        # Use \s+ instead of literal spaces because the opening <w:style ...>
        # tag may be wrapped onto multiple lines in the source XML.
        xml = re.sub(
            (
                r'(<w:style\s+w:type="paragraph"\s+w:styleId="Heading'
                + str(level) + r'".*?<w:rPr>\s*)<w:rFonts\b[^/]*/>'
            ),
            r'\1' + heading_fonts_tag,
            xml,
            count=1,
            flags=re.S,
        )
        # Same for the linked HeadingNChar character style.
        xml = re.sub(
            (
                r'(<w:style\s+w:type="character"\s+w:customStyle="1"\s+'
                r'w:styleId="Heading' + str(level)
                + r'Char".*?<w:rPr>\s*)<w:rFonts\b[^/]*/>'
            ),
            r'\1' + heading_fonts_tag,
            xml,
            count=1,
            flags=re.S,
        )

    # 2. Add / replace default paragraph spacing (1.5 line spacing).
    spacing_tag = (
        f'<w:spacing w:line="{LINE_SPACING}" w:lineRule="auto" '
        'w:before="0" w:after="0"/>'
    )
    if "<w:pPrDefault>" in xml:
        xml = re.sub(
            r'<w:pPrDefault>\s*<w:pPr>(.*?)</w:pPr>\s*</w:pPrDefault>',
            lambda m: (
                '<w:pPrDefault><w:pPr>'
                + re.sub(r'<w:spacing[^/]*/>', '', m.group(1))
                + spacing_tag
                + '</w:pPr></w:pPrDefault>'
            ),
            xml,
            count=1,
            flags=re.S,
        )
    else:
        xml = xml.replace(
            "</w:docDefaults>",
            f"<w:pPrDefault><w:pPr>{spacing_tag}</w:pPr></w:pPrDefault></w:docDefaults>",
        )

    # 3. Append Note / Placeholder / NoteInline / NoteListParagraph styles
    #    if not already present.
    if 'w:styleId="Note"' not in xml:
        xml = xml.replace(
            "</w:styles>",
            NOTE_STYLE
            + PLACEHOLDER_STYLE
            + NOTE_INLINE_STYLE
            + NOTE_LIST_PARAGRAPH_STYLE
            + "</w:styles>",
        )
    return xml


def patch() -> None:
    _ensure_default_reference()
    tmp = REF.with_suffix(".docx.tmp")

    with zipfile.ZipFile(REF) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                data = _patch_styles_xml(data.decode("utf-8")).encode("utf-8")
            zout.writestr(item, data)

    shutil.move(tmp, REF)
    print(
        f"Patched {REF}: body fonts={ASCII_FONT}/{EA_FONT}, "
        f"heading fonts={HEADING_ASCII_FONT}/{HEADING_EA_FONT}, "
        f"ea-lang={EA_LANG}, line-spacing=1.5, "
        f"Note/Placeholder color=#{COLOR}."
    )


if __name__ == "__main__":
    patch()
