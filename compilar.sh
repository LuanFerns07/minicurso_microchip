#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
mkdir -p build pdfs
python3 scripts/gerar_brasil.py
for task_source in slides/aula1.tex slides/aula2.tex slides/encerramento_aula3.tex slides/aula1_resumo.tex slides/aula2_resumo.tex slides/encerramento_aula3_resumo.tex slides/aula1_notas.tex slides/aula2_notas.tex slides/encerramento_aula3_notas.tex apoio/roadmap.tex apoio/exercicios.tex apoio/gabarito.tex apoio/guia_facilitadores.tex apoio/mapa_brasil.tex; do
    task_name="$(basename -- "$task_source" .tex)"
    echo "Compilando $task_name..."
    if ! latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=../build "$task_source" > "build/${task_name}_compilacao.log" 2>&1; then
        tail -n 60 "build/${task_name}_compilacao.log"
        exit 1
    fi
    cp -- "build/${task_name}.pdf" "pdfs/${task_name}.pdf"
done
echo 'PDFs disponíveis em material/pdfs/.'
