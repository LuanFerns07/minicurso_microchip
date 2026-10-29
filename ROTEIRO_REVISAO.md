# Roteiro atual e revisão do minicurso

## Percurso existente

Três encontros de 120 minutos, em português, com figuras e discussão. As etapas de uma animação aparecem como páginas consecutivas do PDF, mantendo o número do quadro. As versões `resumo` selecionam uma página por quadro. Os documentos de notas e o guia de condução foram removidos nesta revisão.

| Encontro | Roteiro | Tempo |
| --- | --- | --- |
| Aula 1 | Facilitadores e percurso; história, litografia e perspectivas; materiais; junção PN; pausa; MOSFET; CMOS e desenho físico; atividade e fechamento | 5 + 22 + 15 + 18 + 10 + 25 + 15 + 10 = 120 min |
| Aula 2 | Retomada; inversor, carga, atraso e energia; NAND; pausa; NOR; desenho e teste em duplas; composição e fechamento | 10 + 20 + 20 + 10 + 20 + 25 + 15 = 120 min |
| Aula 3 | Prática no Cadence Virtuoso ainda pendente; encerramento com trilhas de estudo e panorama brasileiro | 95 + 25 = 120 min previstos |

## Arquivos que controlam o conteúdo

- `slides/aula1.tex`: facilitadores, percurso, materiais, PN, MOSFET e CMOS.
- `slides/contexto_abertura.tex` e `slides/contexto_visuais.tex`: história, gráficos, litografia, limites de escala e integração 3D.
- `slides/assets/facilitadores/`: fotos extraídas dos currículos fornecidos.
- `slides/aula2.tex`: inversor, NAND, NOR e composição.
- `slides/encerramento_aula3.tex`: trilhas e encerramento; inclui a seção Brasil gerada.
- `slides/comum.tex` e `slides/visuais.tex`: comandos, circuitos e figuras compartilhados.
- `apoio/exercicios.tex` e `apoio/gabarito.tex`: atividades e respostas.
- `scripts/gerar_brasil.py` e `dados/*.csv`: origem dos arquivos gerados do mapa. Alterar o gerador ou os dados; a compilação sobrescreve os arquivos gerados.
- `dados/FONTES_CONTEXTO.md` e `dados/processos_historicos.csv`: fontes e valores dos gráficos da abertura.

## Verificações de conteúdo

1. Na abertura, distinguir quantidade de transistores, dimensão física, nome de geração de processo e resolução óptica. A curva de Moore é ideal e normalizada; a série histórica não mede uniformemente o comprimento de porta.
2. Usar a comparação bairros/andares para explicar proximidade e interconexões. CMOS 2.0 é uma proposta de integração heterogênea; produtos com memória empilhada já existem.
3. Conferir se as figuras de PN e MOSFET permitem explicar difusão, depleção, inversão e controle da condução.
4. Na aula 2, conferir se o participante consegue prever a saída pelo caminho elétrico antes da tabela-verdade.
5. Elaborar a prática apenas quando solicitado, com circuito, biblioteca/PDK, alimentação, estímulos e resultados definidos. Validar os 95 minutos com execução real.
6. O encerramento contém sete quadros de panorama Brasil, incluindo seis páginas regionais para consulta.
7. Sincronizar slides, resumos, atividades, gabarito e documentação após alterações. Preservar o Beamer UFC 4:3.

## Compilar no Windows

Com Python e MiKTeX (ou outra distribuição com pdfLaTeX) disponíveis no terminal:

```powershell
.\compilar.ps1
```

Para escolher o Python:

```powershell
.\compilar.ps1 -Python 'C:\caminho\python.exe'
```

O comando gera a seção Brasil em UTF-8, executa duas passagens de pdfLaTeX por documento e atualiza os **10 PDFs** em `pdfs/`. Registros e intermediários ficam em `build/`. Os pacotes LaTeX do projeto devem estar instalados. No Linux, use `bash compilar.sh`.
