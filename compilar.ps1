param([string]$Python = 'python')
$ErrorActionPreference = 'Stop'
Push-Location $PSScriptRoot
try {
    Get-Command $Python, pdflatex -ErrorAction Stop | Out-Null
    & $Python scripts/gerar_brasil.py
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar a seção Brasil.' }
    & $Python scripts/gerar_integracao.py
    if ($LASTEXITCODE -ne 0) { throw 'Falha ao gerar o gráfico de integração.' }
    New-Item -ItemType Directory -Force -Path build,pdfs | Out-Null
    foreach ($obsolete in 'aula1_notas', 'aula2_notas', 'encerramento_aula3_notas', 'guia_facilitadores') {
        Remove-Item -LiteralPath "pdfs/$obsolete.pdf" -ErrorAction SilentlyContinue
    }
    $sources = @(
        'slides/aula1.tex', 'slides/aula2.tex', 'slides/encerramento_aula3.tex',
        'slides/aula1_resumo.tex', 'slides/aula2_resumo.tex', 'slides/encerramento_aula3_resumo.tex',
        'apoio/roadmap.tex', 'apoio/exercicios.tex', 'apoio/gabarito.tex',
        'apoio/mapa_brasil.tex', 'apoio/integracao_processadores.tex'
    )
    foreach ($source in $sources) {
        $name = [IO.Path]::GetFileNameWithoutExtension($source)
        Push-Location ([IO.Path]::GetDirectoryName($source))
        try {
            foreach ($pass in 1..2) {
                & pdflatex '-interaction=nonstopmode' '-halt-on-error' '-output-directory=../build' "$name.tex" *> "../build/${name}_compilacao.log"
                if ($LASTEXITCODE -ne 0) {
                    Get-Content "../build/${name}_compilacao.log" -Tail 40
                    throw "Falha ao compilar $name. Consulte build/${name}_compilacao.log."
                }
            }
        } finally { Pop-Location }
        Copy-Item -LiteralPath "build/$name.pdf" -Destination "pdfs/$name.pdf" -Force
        Write-Host "OK: $name"
    }
    Write-Host 'Os 11 PDFs foram compilados em pdfs/.'
} finally { Pop-Location }
