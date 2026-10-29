#!/usr/bin/env python3
"""Gera entregas portáteis sem referências originais, currículos ou histórico Git."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

material = Path(__file__).resolve().parent
raiz = material.parent

with ZipFile(raiz/'minicurso_cmos_completo.zip', 'w', ZIP_DEFLATED) as pacote:
    pacote.writestr('README.md', '''# Do transistor ao chip

Oficinas em português, com duas horas por encontro.
Desenvolvimento: Luan F. Nogueira e Luiz F. de Melo Soares.

- [Aula 1](material/pdfs/aula1.pdf)
- [Aula 2](material/pdfs/aula2.pdf)
- [Encerramento da aula 3](material/pdfs/encerramento_aula3.pdf)
- [Mapa do Brasil](material/pdfs/mapa_brasil.pdf)
- [Fontes, instruções de compilação e demais materiais](material/README.md)

O modelo Beamer UFC mantém o formato original 4:3.
''')
    for nome in ['README.md','compilar.sh','compilar.ps1','ROTEIRO_REVISAO.md','empacotar.py','CREDITOS_TEMPLATE.md','CITATION_TEMPLATE.cff']:
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
    pacote.write(material/'dados/FONTES_CONTEXTO.md','FONTES_CONTEXTO.md')
    pacote.write(material/'dados/processos_historicos.csv','processos_historicos.csv')
    for nome in ['FONTES_INTEGRACAO.md','CREDITOS_MICROGRAFIAS.md','integracao_processadores.csv','micrografias_fontes.json']:
        pacote.write(material/'dados'/nome,nome)
    pacote.writestr('LEIA_ME.md', '''# Do transistor ao chip — oficinas visuais de duas horas

Luan F. Nogueira e Luiz F. de Melo Soares. Template UFC original 4:3.

Use pdfLaTeX no Overleaf. `main.tex` compila a aula 1. Para trocar:

- `\\input{aula1.tex}`: 42 quadros; 60 páginas nesta edição com etapas.
- `\\input{aula2.tex}`: 27 quadros; 37 páginas com etapas.
- `\\input{encerramento_aula3.tex}`: 17 quadros, incluindo âmbito Brasil.

Você também pode selecionar diretamente um desses arquivos como principal.
`*_resumo.tex` produz uma página de síntese por quadro.

A animação ocorre ao avançar as páginas: depleção, ativação do MOSFET,
estados do inversor e das portas NAND/NOR. O panorama inclui VLSI, bairros de casas,
prédio e CMOS 2.0. Os terminais MOS são Source, Gate e Drain. As figuras vetoriais estão em
`visuais.tex`. A abertura histórica usa `contexto_abertura.tex` e
`contexto_visuais.tex`. A fabricação e as perspectivas usam `fabricacao_aula1.tex`,
`perspectivas_aula1.tex`, `fisica_fabricacao_visuais.tex` e `cidade_visuais.tex`.
Preserve também `assets/`, `libs/` e `brasil_*.tex`.
Os retratos vêm dos currículos. As fotos antigas do componente foram retiradas.
As duas micrografias reais selecionadas ainda não foram obtidas por bloqueio
de download e não aparecem nesta edição. Veja CREDITOS_MICROGRAFIAS.md.
Com os arquivos locais, `microscopia_trecho.tex` inclui dois quadros adicionais.
Consulte FONTES_CONTEXTO.md
para as fontes da história, gráficos, litografia e CMOS 2.0.

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
