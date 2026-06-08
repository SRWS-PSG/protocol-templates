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

# PDF is the submission target.
# Primary engine is xelatex (needed for CJK in the JA build). If no LaTeX
# engine is installed, fall back to: pandoc -> docx -> LibreOffice -> PDF.
# The LibreOffice route yields a searchable, font-embedded PDF that meets
# Google Scholar's inclusion requirements, and needs no TeX install.
$pdfArgs = @('--pdf-engine=xelatex','-V','CJKmainfont=Yu Gothic','-V','geometry=margin=1in','-V','fontsize=11pt')

function Resolve-Soffice {
    foreach ($c in @('soffice',
                     'C:/Program Files/LibreOffice/program/soffice.exe',
                     'C:/Program Files (x86)/LibreOffice/program/soffice.exe')) {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if ($cmd) { return $cmd.Source }
        if (Test-Path $c) { return $c }
    }
    return $null
}

function Invoke-PdfBuild {
    param([string]$Src, [string]$Base)
    $out = Join-Path $outdir "$Base.pdf"
    $hasTex = Get-Command xelatex -ErrorAction SilentlyContinue
    if ($hasTex) {
        Invoke-Pandoc -Src $Src -ExtraArgs $pdfArgs -Out $out
        return
    }
    $soffice = Resolve-Soffice
    if (-not $soffice) {
        throw "No PDF engine found. Install a LaTeX engine (xelatex) or LibreOffice (soffice)."
    }
    Write-Host "xelatex not found; using LibreOffice docx->PDF route."
    $tmpDocx = Join-Path $outdir "$Base.docx"
    Invoke-Pandoc -Src $Src -ExtraArgs $docxArgs -Out $tmpDocx
    if (Test-Path $out) { Remove-Item $out -Force }
    # soffice writes asynchronously and returns before the file is flushed.
    & $soffice --headless --convert-to pdf --outdir $outdir $tmpDocx
    $deadline = 30
    while ($deadline -gt 0 -and -not (Test-Path $out)) { Start-Sleep -Milliseconds 500; $deadline-- }
    if (-not (Test-Path $out)) { throw "LibreOffice failed to produce $out (is another LibreOffice instance running?)" }
    Write-Host "PDF written: $out"
}

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
        'pdf'  { Invoke-PdfBuild -Src $cfg.Src -Base $base }
        'all'  {
            Invoke-PdfBuild -Src $cfg.Src -Base $base
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
