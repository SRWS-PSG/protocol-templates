# Build script for the scoping review protocol template.
# Usage:
#   pwsh ./templates/scoping-review/build.ps1               # build all targets (docx, html) for both EN and JA
#   pwsh ./templates/scoping-review/build.ps1 -Target docx  # build a specific target
#   pwsh ./templates/scoping-review/build.ps1 -Lang ja      # build a specific language only
#
# Outputs go to templates/scoping-review/build/ which is gitignored.

[CmdletBinding()]
param(
    [ValidateSet('all','docx','html','pdf')]
    [string]$Target = 'all',
    [ValidateSet('all','en','ja')]
    [string]$Lang = 'all'
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
        Src  = Join-Path $here 'protocol_template_for_scoping_review.md'
        Base = 'protocol_template_for_scoping_review'
    }
    ja = @{
        Src  = Join-Path $here 'protocol_template_for_scoping_review.ja.md'
        Base = 'protocol_template_for_scoping_review.ja'
    }
}

if (-not (Test-Path $outdir)) { New-Item -ItemType Directory -Path $outdir | Out-Null }

# Fetch the Vancouver CSL on first run (Zotero Style Repository, MIT-style license).
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
        "--resource-path=$here",
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

$pdfArgs = @('--pdf-engine=xelatex','-V','CJKmainfont=Yu Gothic')

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
            Invoke-Pandoc -Src $cfg.Src -ExtraArgs $docxArgs -Out (Join-Path $outdir "$base.docx")
            Invoke-Pandoc -Src $cfg.Src -ExtraArgs $htmlArgs -Out (Join-Path $outdir "$base.html")
        }
    }
}

Write-Host "Done. Output in $outdir"
