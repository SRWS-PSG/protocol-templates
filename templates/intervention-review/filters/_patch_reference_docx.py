"""Patch reference.docx with:
  - default fonts: Times New Roman (ASCII) + MS Mincho (East Asian)
  - default line spacing 1.5
  - 'Note' (paragraph) and 'Placeholder' (character) styles in light blue
    (#4FC3F7) — matching the HTML CSS.

Idempotent: re-running on an already patched file will overwrite cleanly
because we regenerate from the bundled default each time via pandoc.
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
      <w:ind w:left="240" />
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

    # 3. Append Note / Placeholder styles if not already present.
    if 'w:styleId="Note"' not in xml:
        xml = xml.replace("</w:styles>", NOTE_STYLE + PLACEHOLDER_STYLE + "</w:styles>")
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
        f"Patched {REF}: fonts={ASCII_FONT}/{EA_FONT}, "
        f"line-spacing=1.5, Note/Placeholder color=#{COLOR}."
    )


if __name__ == "__main__":
    patch()
