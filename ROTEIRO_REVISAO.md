# Roteiro atual e revisão do minicurso

## Percurso existente

Três encontros de 120 minutos, em português, com figuras e discussão. As etapas de uma animação aparecem como páginas consecutivas do PDF, mantendo o número do quadro. As versões `resumo` selecionam uma página por quadro. Os documentos de notas e o guia de condução foram removidos nesta revisão.

| Encontro | Roteiro | Tempo |
| --- | --- | --- |
| Aula 1 | Facilitadores; panorama histórico e contagens por die; materiais; junção PN; pausa; MOSFET; inversor e layout; fabricação e litografia; limites e integração 3D; atividade | 5 + 12 + 12 + 16 + 10 + 23 + 10 + 12 + 12 + 8 = 120 min |
| Aula 2 | Retomada; inversor, carga, atraso e energia; NAND; pausa; NOR; desenho e teste em duplas; composição e fechamento | 10 + 20 + 20 + 10 + 20 + 25 + 15 = 120 min |
| Aula 3 | Prática no Cadence Virtuoso ainda pendente; encerramento com trilhas de estudo e panorama brasileiro | 95 + 25 = 120 min previstos |

## Arquivos que controlam o conteúdo

- `slides/aula1.tex`: facilitadores, percurso, materiais, PN, MOSFET e CMOS.
- `slides/contexto_abertura.tex` e `slides/contexto_visuais.tex`: história e gráficos de integração.
- `slides/fabricacao_aula1.tex` e `slides/fisica_fabricacao_visuais.tex`: estrutura física, fabricação, litografia, régua atômica e barreira de energia.
- `slides/perspectivas_aula1.tex` e `slides/cidade_visuais.tex`: limites e integração 3D, com cidade e prédio em corte.
- `slides/microscopia_trecho.tex` e `dados/CREDITOS_MICROGRAFIAS.md`: micrografias reais selecionadas, com obtenção ainda pendente.
- `scripts/gerar_integracao.py` e `dados/integracao_processadores.csv`: 13 chips e suas fontes.
- `slides/previa_portas.tex`: encerramento com chaves, diodos e MOSFETs em série/paralelo.
- `slides/assets/facilitadores/`: fotos extraídas dos currículos fornecidos.
- `slides/aula2.tex`: inversor, NAND, NOR e composição.
- `slides/encerramento_aula3.tex`: trilhas e encerramento; inclui a seção Brasil gerada.
- `slides/comum.tex` e `slides/visuais.tex`: comandos, circuitos e figuras compartilhados.
- `apoio/exercicios.tex` e `apoio/gabarito.tex`: atividades e respostas.
- `scripts/gerar_brasil.py` e `dados/*.csv`: origem dos arquivos gerados do mapa. Alterar o gerador ou os dados; a compilação sobrescreve os arquivos gerados.
- `dados/FONTES_CONTEXTO.md` e `dados/processos_historicos.csv`: fontes e valores dos gráficos da abertura.

## Verificações de conteúdo

1. Preservar as dependências: o público conhece material, junção, MOSFET e inversor antes do corte CMOS e da fabricação. A vista do circuito e a TEM nanométrica devem ser creditadas como amostras diferentes; só entram quando os arquivos reais estiverem locais.
2. Distinguir quantidade de transistores, tamanho de referência do átomo, espaçamento na rede, resolução óptica e nome do nó. A curva de Moore é ideal e normalizada. A régua de 8 nm compara comprimentos, não conta átomos de um transistor.
3. Manter a ordem régua atômica → bairros/prédio → CMOS 2.0, sem outros quadros entre esses assuntos. Usar a comparação bairros/andares para explicar proximidade e interconexões. CMOS 2.0 é uma proposta de integração heterogênea; produtos com memória empilhada já existem.
4. Conferir se as figuras de PN e MOSFET permitem explicar difusão, depleção, inversão e controle da condução.
5. Na aula 2, conferir se o participante consegue prever a saída pelo caminho elétrico antes da tabela-verdade.
6. Elaborar a prática apenas quando solicitado, com circuito, biblioteca/PDK, alimentação, estímulos e resultados definidos. Validar os 95 minutos com execução real.
7. O encerramento contém sete quadros de panorama Brasil, incluindo seis páginas regionais para consulta.
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

O comando gera a seção Brasil em UTF-8, executa duas passagens de pdfLaTeX por documento e atualiza os **11 PDFs** em `pdfs/`. Registros e intermediários ficam em `build/`. Os pacotes LaTeX do projeto devem estar instalados. No Linux, use `bash compilar.sh`.
