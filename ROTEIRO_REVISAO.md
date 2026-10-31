# Roteiro atual e revisão do minicurso

## Percurso existente

Três encontros de 120 minutos, em português, com figuras e discussão. As etapas de uma animação aparecem como páginas consecutivas do PDF, mantendo o número do quadro. As versões `resumo` selecionam uma página por quadro. Os documentos de notas e o guia de condução foram removidos nesta revisão.

| Encontro | Roteiro | Tempo |
| --- | --- | --- |
| Aula 1 | Fundamentos com PN em um quadro; pausa antes das referências; caracterização DC de NMOS/PMOS | 65 + 5 + 50 = 120 min |
| Aula 2 | Construção CMOS; pausa antes das referências; prática de inversor, NAND e NOR | 55 + 5 + 60 = 120 min |
| Aula 3 | Preparação; pausa e referências; layout/DRC/LVS; retomada das trilhas e Brasil | 5 + 5 + 95 + 15 = 120 min |

## Arquivos que controlam o conteúdo

- `slides/aula1.tex`: facilitadores, percurso, materiais, PN, MOSFET e CMOS.
- `slides/contexto_abertura.tex` e `slides/contexto_visuais.tex`: história e gráficos de integração.
- `slides/fabricacao_aula1.tex` e `slides/fisica_fabricacao_visuais.tex`: estrutura física, fabricação, litografia, régua atômica e barreira de energia.
- `slides/perspectivas_aula1.tex` e `slides/cidade_visuais.tex`: limites e integração 3D, com cidade e prédio em corte.
- `slides/microscopia_trecho.tex` e `dados/CREDITOS_MICROGRAFIAS.md`: micrografias reais selecionadas, com obtenção ainda pendente.
- `scripts/gerar_integracao.py` e `dados/integracao_processadores.csv`: 13 chips e suas fontes.
- `slides/previa_portas.tex`: encerramento com chaves, diodos e MOSFETs em série/paralelo.
- `slides/assets/facilitadores/`: fotos extraídas dos currículos fornecidos.
- `slides/aula2.tex` e `slides/portas_visuais.tex`: série/paralelo, inversor, R → rede PMOS, NAND/NOR e previsão das ondas.
- `slides/encerramento_aula3.tex` e `slides/trilhas_visuais.tex`: 3 slides de preparação/pausa/referências e 8 slides de encerramento, trilhas e Brasil.
- `slides/praticas_cmos.tex` e `slides/praticas_aula*.tex`: roteiro visual dos três módulos, com 44 capturas originais.
- `praticas/QUICK_START.md`: fonte das etapas e parâmetros; manter as pendências de documentação identificadas.
- `slides/consulta_brasil.tex`: capa, panorama e seis páginas regionais, para consulta fora dos 15 minutos finais.
- `slides/comum.tex` e `slides/visuais.tex`: comandos, circuitos e figuras compartilhados.
- `apoio/exercicios.tex` e `apoio/gabarito.tex`: atividades e respostas.
- `scripts/gerar_brasil.py` e `dados/*.csv`: origem dos arquivos gerados do mapa. Alterar o gerador ou os dados; a compilação sobrescreve os arquivos gerados.
- `dados/FONTES_CONTEXTO.md` e `dados/processos_historicos.csv`: fontes e valores dos gráficos da abertura.

## Verificações de conteúdo

1. Preservar as dependências: o público conhece material, junção, MOSFET e inversor antes do corte CMOS e da fabricação. A vista do circuito e a TEM nanométrica devem ser creditadas como amostras diferentes; só entram quando os arquivos reais estiverem locais.
2. Distinguir quantidade de transistores, tamanho de referência do átomo, espaçamento na rede, resolução óptica e nome do nó. A curva de Moore é ideal e normalizada. A régua de 8 nm compara comprimentos, não conta átomos de um transistor.
3. No panorama, manter a ordem VLSI → NMOS/PMOS até SoC → bairros/prédio → CMOS 2.0. A régua atômica permanece após litografia, junto aos limites físicos. Nomear os terminais MOS como Source, Gate e Drain. Usar a comparação bairros de casas/andares para explicar proximidade e interconexões. CMOS 2.0 é uma proposta de integração heterogênea; produtos com memória empilhada já existem.
4. Conferir se as figuras de PN e MOSFET permitem explicar difusão, depleção, inversão e controle da condução.
5. Na aula 2, conferir se o participante consegue prever a saída pelo caminho elétrico antes da tabela-verdade.
6. Manter o roteiro visual alinhado ao Quick Start. Usar as curvas e os transientes registrados; não declarar DRC/LVS aprovados sem os relatórios. A aula 2 não inclui a curva DC do inversor, e a aula 3 termina em DRC/LVS, sem extração e simulação após extração.
7. Os oito slides de encerramento continuam após a prática; os três slides iniciais da aula 3 incluem a pausa de 5 minutos antes das referências. Há um panorama Brasil no encerramento. A apresentação de consulta Brasil preserva as seis páginas regionais com todas as organizações. O levantamento não foi alterado nesta revisão.
8. Sincronizar slides, resumos, atividades, gabarito e documentação após alterações. Preservar o Beamer UFC 4:3.

## Compilar no Windows

Com Python e MiKTeX (ou outra distribuição com pdfLaTeX) disponíveis no terminal:

```powershell
.\compilar.ps1
```

Para escolher o Python:

```powershell
.\compilar.ps1 -Python 'C:\caminho\python.exe'
```

O comando gera a seção Brasil em UTF-8, executa duas passagens de pdfLaTeX por documento e atualiza os **13 PDFs** em `pdfs/`. Registros e intermediários ficam em `build/`. Os pacotes LaTeX do projeto devem estar instalados. No Linux, use `bash compilar.sh`.
