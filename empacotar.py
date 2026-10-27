#!/usr/bin/env python3
"""Gera os pacotes de entrega sem redistribuir currículos ou PDFs de referência."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

material = Path(__file__).resolve().parent
raiz = material.parent

with ZipFile(raiz / 'minicurso_cmos_completo.zip', 'w', ZIP_DEFLATED) as pacote:
    pacote.write(raiz / 'README.md', 'README.md')
    for nome in ['README.md', 'compilar.sh', 'empacotar.py']:
        pacote.write(material / nome, f'material/{nome}')
    for pasta in ['slides', 'apoio', 'pdfs']:
        for arquivo in sorted((material / pasta).rglob('*')):
            if arquivo.is_file():
                pacote.write(arquivo, 'material/' + str(arquivo.relative_to(material)))
    for nome in ['README.md', 'CITATION.cff', 'CHANGELOG.md']:
        arquivo = material / 'template_original' / nome
        if arquivo.exists():
            pacote.write(arquivo, f'material/creditos_template/{nome}')

with ZipFile(raiz / 'minicurso_cmos_beamer.zip', 'w', ZIP_DEFLATED) as pacote:
    for arquivo in sorted((material / 'slides').rglob('*')):
        if arquivo.is_file():
            pacote.write(arquivo, str(arquivo.relative_to(material / 'slides')))
    pacote.writestr('main.tex', '\\input{aula1.tex}\n')
    pacote.writestr('LEIA_ME.md', '''# Do transistor ao chip — Beamer em português

Desenvolvimento e facilitação: Luan F. Nogueira e Luiz F. de Melo Soares.

Carregue o conteúdo deste ZIP no Overleaf e use pdfLaTeX. O arquivo `main.tex`
compila a aula 1 por padrão. Para mudar a apresentação, altere seu conteúdo:

- Aula 1: `\\input{aula1.tex}` — 38 slides.
- Aula 2: `\\input{aula2.tex}` — 39 slides principais e 3 opcionais.
- Encerramento da aula 3: `\\input{encerramento_aula3.tex}` — 12 slides.

Você também pode selecionar diretamente um desses arquivos como documento
principal. As versões `*_notas.tex` intercalam slides e notas dos facilitadores.
O arquivo `comum.tex` reúne os comandos de conteúdo e os circuitos. O tema
original está em `libs/ufc_format.cls`. Preserve a pasta `libs/`.
Não é necessário baixar imagens, fontes ou outros arquivos externos.

A prática da aula 3 no Virtuoso será elaborada posteriormente. Este pacote
contém apenas seu encerramento. Os materiais de apoio e PDFs prontos estão
no pacote completo `minicurso_cmos_completo.zip`.

Identidade visual: Template Beamer UFC, de Maurício Moreira Neto, na proporção
original 4:3 (128 × 96 mm). A classe, o tema e seus créditos foram preservados. Referências
conceituais e fontes das mini-fichas aparecem nos slides. Os currículos e PDFs
de referência não são redistribuídos neste ZIP.
''')
    arquivo = material / 'template_original' / 'CITATION.cff'
    if arquivo.exists():
        pacote.write(arquivo, 'CITATION_TEMPLATE.cff')

for nome in ['minicurso_cmos_completo.zip', 'minicurso_cmos_beamer.zip']:
    arquivo = raiz / nome
    print(f'{arquivo.name}: {arquivo.stat().st_size / 1024 / 1024:.2f} MiB')
