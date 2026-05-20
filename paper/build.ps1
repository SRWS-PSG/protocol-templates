# Build script for the companion paper (MetaArXiv submission).
# Usage:
#   pwsh ./paper/build.ps1                # build all targets (pdf, docx, html) for en
#   pwsh ./paper/build.ps1 -Target pdf    # build a specific target
#   pwsh ./paper/build.ps1 -Lang ja       # build the Japanese mirror if present
#
# Outputs go to paper/build/ which is gitignored.
#
# PDF is the format submitted to MetaArXiv (OSF Preprints). It must satisfy
# Google Scholar's inclusion requirements: searchable text, title in largest
# font at top, identifiable References section, fonts embedded, < 5 MB.

[CmdletBinding()]
param(
    [ValidateSet('all','pdf','docx','html')]
    [string]$Target = 'all',
    [ValidateSet('all','en','ja')]
    [string]$Lang = 'en'
)

$ErrorActionPreference = 'Stop'

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$bib     = Join-Path $here 'references.bib'
$cslPath = Join-Path $here 'vancouver.csl'
$outdir  = Join-Path $here 'build'
$luaFilt = Join-Path $here 'filters/highlight.lua'
$css     = Join-Path $here 'filters/style.css'
$refDocx = Join-Path $here 'filters/reference.docx'

$sources = @{
    en = @{
        Src  = Join-Path $here 'manuscript.md'
        Base = 'manuscript'
    }
    ja = @{
        Src  = Join-Path $here 'manuscript.ja.md'
        Base = 'manuscript.ja'
    }
}

if (-not (Test-Path $outdir)) { New-Item -ItemType Directory -Path $outdir | Out-Null }

if (-not (Test-Path $cslPath)) {
    Write-Host "Downloading Vancouver CSL..."
    Invoke-WebRequest -Uri 'https://www.zotero.org/styles/vancouver' -OutFile $cslPath
}

function Invoke-Pandoc {
    param([string]$Src, [string[]]$ExtraArgs, [string]$Out)
    $commonArgs = @(
        $Src,
        '--from=markdown',
        '--citeproc',
        "--bibliography=$bib",
        "--csl=$cslPath",
        "--lua-filter=$luaFilt",
        '--standalone'
    )
    $pandocArgs = $commonArgs + $ExtraArgs + @('-o', $Out)
    Write-Host "pandoc $($pandocArgs -join ' ')"
    & pandoc @pandocArgs
}

$docxArgs = @('--to=docx')
if (Test-Path $refDocx) { $docxArgs += "--reference-doc=$refDocx" }

$htmlArgs = @('--to=html5','--toc','--embed-resources')
if (Test-Path $css) { $htmlArgs += "--css=$css" }

# PDF is the submission target. xelatex required for CJK if JA build.
# For en, the CJKmainfont arg is harmless if no CJK is used.
$pdfArgs = @('--pdf-engine=xelatex','-V','CJKmainfont=Yu Gothic','-V','geometry=margin=1in','-V','fontsize=11pt')

$langs = if ($Lang -eq 'all') { @('en','ja') } else { @($Lang) }

foreach ($lng in $langs) {
    $cfg  = $sources[$lng]
    if (-not (Test-Path $cfg.Src)) {
        Write-Host "Skip $lng — source not found: $($cfg.Src)"
        continue
    }
    $base = $cfg.Base

    switch ($Target) {
        'docx' { Invoke-Pandoc -Src $cfg.Src -ExtraArgs $docxArgs -Out (Join-Path $outdir "$base.docx") }
        'html' { Invoke-Pandoc -Src $cfg.Src -ExtraArgs $htmlArgs -Out (Join-Path $outdir "$base.html") }
        'pdf'  { Invoke-Pandoc -Src $cfg.Src -ExtraArgs $pdfArgs  -Out (Join-Path $outdir "$base.pdf")  }
        'all'  {
            Invoke-Pandoc -Src $cfg.Src -ExtraArgs $pdfArgs  -Out (Join-Path $outdir "$base.pdf")
            Invoke-Pandoc -Src $cfg.Src -ExtraArgs $docxArgs -Out (Join-Path $outdir "$base.docx")
            Invoke-Pandoc -Src $cfg.Src -ExtraArgs $htmlArgs -Out (Join-Path $outdir "$base.html")
        }
    }
}

Write-Host "Done. Output in $outdir"
Write-Host ""
Write-Host "Submission checklist (MetaArXiv / Google Scholar):"
Write-Host "  [ ] PDF < 5 MB"
Write-Host "  [ ] Title in largest font (>= 24pt) at top of page 1"
Write-Host "  [ ] Authors visible below title (16-23pt)"
Write-Host "  [ ] Abstract section identifiable"
Write-Host "  [ ] References section identifiable (heading 'References')"
Write-Host "  [ ] Text is selectable / searchable (not scanned)"
