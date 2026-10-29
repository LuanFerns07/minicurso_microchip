#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
mkdir -p build pdfs
for task_obsolete in aula1_notas aula2_notas encerramento_aula3_notas guia_facilitadores; do
    rm -f -- "pdfs/${task_obsolete}.pdf"
done
python3 scripts/gerar_brasil.py
python3 scripts/gerar_integracao.py
for task_source in slides/aula1.tex slides/aula2.tex slides/encerramento_aula3.tex slides/aula1_resumo.tex slides/aula2_resumo.tex slides/encerramento_aula3_resumo.tex apoio/roadmap.tex apoio/exercicios.tex apoio/gabarito.tex apoio/mapa_brasil.tex apoio/integracao_processadores.tex; do
    task_name="$(basename -- "$task_source" .tex)"
    echo "Compilando $task_name..."
    if ! latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=../build "$task_source" > "build/${task_name}_compilacao.log" 2>&1; then
        tail -n 60 "build/${task_name}_compilacao.log"
        exit 1
    fi
    cp -- "build/${task_name}.pdf" "pdfs/${task_name}.pdf"
done
echo 'PDFs disponíveis em material/pdfs/.'
