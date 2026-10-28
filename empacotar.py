#!/usr/bin/env python3
"""Gera entregas portáteis sem referências originais, currículos ou histórico Git."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

material = Path(__file__).resolve().parent
raiz = material.parent

with ZipFile(raiz/'minicurso_cmos_completo.zip', 'w', ZIP_DEFLATED) as pacote:
    pacote.write(raiz/'README.md', 'README.md')
    for nome in ['README.md','compilar.sh','empacotar.py','CREDITOS_TEMPLATE.md','CITATION_TEMPLATE.cff']:
        pacote.write(material/nome, f'material/{nome}')
    for pasta in ['slides','apoio','pdfs','dados','scripts']:
        for arquivo in sorted((material/pasta).rglob('*')):
            if arquivo.is_file() and '__pycache__' not in arquivo.parts:
                pacote.write(arquivo,'material/'+str(arquivo.relative_to(material)))

with ZipFile(raiz/'minicurso_cmos_beamer.zip','w',ZIP_DEFLATED) as pacote:
    for arquivo in sorted((material/'slides').rglob('*')):
        if arquivo.is_file():
            pacote.write(arquivo,str(arquivo.relative_to(material/'slides')))
    pacote.writestr('main.tex','\\input{aula1.tex}\n')
    for nome in ['CITATION_TEMPLATE.cff','CREDITOS_TEMPLATE.md']:
        pacote.write(material/nome,nome)
    pacote.write(material/'dados/CREDITOS_MAPA.md','CREDITOS_MAPA.md')
    pacote.writestr('LEIA_ME.md', '''# Do transistor ao chip — oficinas visuais de duas horas

Luan F. Nogueira e Luiz F. de Melo Soares. Template UFC original 4:3.

Use pdfLaTeX no Overleaf. `main.tex` compila a aula 1. Para trocar:

- `\\input{aula1.tex}`: 25 quadros; 34 páginas com etapas.
- `\\input{aula2.tex}`: 27 quadros; 37 páginas com etapas.
- `\\input{encerramento_aula3.tex}`: 17 quadros, incluindo âmbito Brasil.

Você também pode selecionar diretamente um desses arquivos como principal.
`*_resumo.tex` produz uma página de síntese por quadro.
`*_notas.tex` inclui orientações para os facilitadores.

A animação ocorre ao avançar as páginas: depleção, ativação do MOSFET,
estados do inversor e das portas NAND/NOR. As figuras vetoriais estão em
`visuais.tex`. Preserve `libs/` e os arquivos `brasil_*.tex`.

Brasil: dados do Brazil Silicon Roadmap, de Matheus Grossi, via planilha
PT-BR fornecida. Mapa redesenhado; 54 organizações, 73 presenças em 13 polos.
Os pontos são esquemáticos por polo, não endereços. Consulte CREDITOS_MAPA.md.

O pacote compila sem baixar imagens ou dados externos. Os materiais de apoio,
o mapa A3 e os dados derivados estão no pacote completo. A prática no Virtuoso
será elaborada posteriormente.
''')

for nome in ['minicurso_cmos_completo.zip','minicurso_cmos_beamer.zip']:
    arquivo=raiz/nome
    print(f'{arquivo.name}: {arquivo.stat().st_size/1024/1024:.2f} MiB')
