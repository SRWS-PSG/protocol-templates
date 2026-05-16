# Build script for the protocol template.
# Usage:
#   pwsh ./template/build.ps1               # build all targets (docx, pdf if LaTeX available, html)
#   pwsh ./template/build.ps1 -Target docx  # build a specific target
#
# Outputs go to template/build/ which is gitignored.

[CmdletBinding()]
param(
    [ValidateSet('all','docx','html','pdf')]
    [string]$Target = 'all'
)

$ErrorActionPreference = 'Stop'

$here    = Split-Path -Parent $MyInvocation.MyCommand.Path
$src     = Join-Path $here 'protocol_template_for_intervention_review.md'
$bib     = Join-Path $here 'references.bib'
$cslPath = Join-Path $here 'vancouver.csl'
$outdir  = Join-Path $here 'build'

if (-not (Test-Path $outdir)) { New-Item -ItemType Directory -Path $outdir | Out-Null }

# Fetch the Vancouver CSL on first run (Zotero Style Repository, MIT-style license).
if (-not (Test-Path $cslPath)) {
    Write-Host "Downloading Vancouver CSL..."
    Invoke-WebRequest -Uri 'https://www.zotero.org/styles/vancouver' -OutFile $cslPath
}

$commonArgs = @(
    $src,
    '--from=markdown',
    '--citeproc',
    "--bibliography=$bib",
    "--csl=$cslPath",
    '--standalone'
)

function Invoke-Pandoc {
    param([string[]]$ExtraArgs, [string]$Out)
    $args = $commonArgs + $ExtraArgs + @('-o', $Out)
    Write-Host "pandoc $($args -join ' ')"
    & pandoc @args
}

switch ($Target) {
    'docx' {
        Invoke-Pandoc -ExtraArgs @('--to=docx') -Out (Join-Path $outdir 'protocol_template_for_intervention_review.docx')
    }
    'html' {
        Invoke-Pandoc -ExtraArgs @('--to=html5','--toc') -Out (Join-Path $outdir 'protocol_template_for_intervention_review.html')
    }
    'pdf' {
        Invoke-Pandoc -ExtraArgs @('--pdf-engine=xelatex','-V','CJKmainfont=Yu Gothic') -Out (Join-Path $outdir 'protocol_template_for_intervention_review.pdf')
    }
    'all' {
        Invoke-Pandoc -ExtraArgs @('--to=docx') -Out (Join-Path $outdir 'protocol_template_for_intervention_review.docx')
        Invoke-Pandoc -ExtraArgs @('--to=html5','--toc') -Out (Join-Path $outdir 'protocol_template_for_intervention_review.html')
    }
}

Write-Host "Done. Output in $outdir"
