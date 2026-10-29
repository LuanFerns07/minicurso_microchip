# Roteiro atual e revisão do minicurso

## Percurso existente

O curso usa três encontros de 120 minutos. Os slides são visuais e as explicações detalhadas ficam nas notas. As etapas de uma animação aparecem como páginas consecutivas do PDF, mantendo o número do quadro.

| Encontro | Roteiro | Tempo |
| --- | --- | --- |
| Aula 1 | Apresentação; materiais, portadores e dopagem; junção PN; pausa; MOSFET; inversor CMOS; desenho e fechamento | 10 + 20 + 20 + 10 + 30 + 15 + 15 = 120 min |
| Aula 2 | Retomada; inversor, carga, atraso e energia; NAND; pausa; NOR; desenho e teste em duplas; composição e fechamento | 10 + 20 + 20 + 10 + 20 + 25 + 15 = 120 min |
| Aula 3 | Prática no Cadence Virtuoso ainda pendente; encerramento com trilhas de estudo e panorama brasileiro | 95 + 25 = 120 min previstos |

## Arquivos que controlam o conteúdo

- `slides/aula1.tex`: materiais, PN, MOSFET e introdução ao CMOS.
- `slides/aula2.tex`: inversor, NAND, NOR e composição.
- `slides/encerramento_aula3.tex`: trilhas e encerramento; inclui a seção Brasil gerada.
- `slides/comum.tex` e `slides/visuais.tex`: comandos, circuitos e figuras compartilhados.
- `apoio/guia_facilitadores.tex`: cronograma e orientações de condução.
- `apoio/exercicios.tex` e `apoio/gabarito.tex`: atividades e respostas.
- `scripts/gerar_brasil.py` e `dados/*.csv`: origem dos arquivos gerados do mapa. Alterar o gerador ou os dados, pois a compilação sobrescreve os arquivos gerados.

## Ordem proposta para revisão do conteúdo

1. Revisar a aula 1 com o PDF principal e as notas lado a lado: verificar se cada figura ajuda o participante a explicar como a porta controla a condução.
2. Revisar a aula 2: conferir se o participante consegue prever a saída pelo caminho elétrico antes de ver a tabela-verdade.
3. Definir a atividade de Virtuoso a partir dessa base: circuito, biblioteca/PDK, alimentação, estímulos e resultados esperados precisam ser acordados antes de escrever instruções específicas.
4. Montar os slides da prática com etapas curtas, verificações e perguntas de previsão. Os 95 minutos incluem abertura do ambiente e execução; validar esse tempo com uma execução real.
5. Ajustar o encerramento para o tempo disponível. Há sete quadros de panorama Brasil, incluindo seis páginas regionais; as notas já orientam a usar essas listas para consulta.
6. Sincronizar exercícios, gabarito, notas e guia depois de cada alteração de conteúdo.

## Pontos a resolver

- A aula 3 ainda não contém os slides da prática; seu PDF atual é somente o encerramento.
- Os valores de alimentação e limiar usados como exemplos conceituais não definem os parâmetros da tecnologia da prática.
- Não tratar os diagramas qualitativos dos slides como resultados de simulação.
- O formato atual é Beamer UFC 4:3. Preservar o tema ao revisar o conteúdo.

## Compilar no Windows

Com Python e MiKTeX (ou outra distribuição com pdfLaTeX) instalados e disponíveis no terminal:

```powershell
.\compilar.ps1
```

Para escolher um executável Python específico:

```powershell
.\compilar.ps1 -Python 'C:\caminho\python.exe'
```

O comando gera a seção Brasil em UTF-8, executa duas passagens de pdfLaTeX por documento e atualiza os 14 PDFs em `pdfs/`. Registros e intermediários ficam em `build/`. O ambiente precisa ter os pacotes LaTeX usados pelo projeto.
