# Do transistor ao chip

Oficinas em português, com **duas horas por encontro**. Desenvolvimento e facilitação: **Luan F. Nogueira e Luiz F. de Melo Soares**. O Beamer UFC permanece no modelo original **4:3 (128 × 96 mm)**.

Os terminais MOS são nomeados **Source, Gate e Drain**; “portas lógicas” continua designando os circuitos digitais.

## Apresentar e consultar

| Material | Quadros | Páginas com as etapas |
| --- | ---: | ---: |
| [Aula 1 — Do silício ao MOSFET](pdfs/aula1.pdf) | 42 | 60 |
| [Aula 2 — Portas CMOS](pdfs/aula2.pdf) | 28 | 44 |
| [Encerramento da aula 3 — Caminhos e Brasil](pdfs/encerramento_aula3.pdf) | 8 | 8 |
| [Consulta — organizações no Brasil](pdfs/consulta_brasil.pdf) | 8 | 8 |

Os quadros privilegiam figuras, desenhos e discussão. A aula 1 segue um percurso contínuo: facilitadores e história → contagens reais, VLSI e composição NMOS/PMOS → SoC → transporte de dados e CMOS 2.0 → materiais e junção PN → MOSFET e inversor CMOS → estrutura física e fabricação → litografia, escala atômica e limites físicos. O bloco de fabricação vem depois dos dispositivos que ele precisa construir. As etapas visuais de um mesmo quadro preservam o número do rodapé: avance pelo PDF em modo de apresentação para animar o processo.

- [Aula 1 resumida](pdfs/aula1_resumo.pdf), [aula 2 resumida](pdfs/aula2_resumo.pdf) e [encerramento resumido](pdfs/encerramento_aula3_resumo.pdf): uma página de síntese por quadro.
- [Atividades](pdfs/exercicios.pdf) e [gabarito](pdfs/gabarito.pdf).
- [Roadmap de estudos](pdfs/roadmap.pdf): A4 horizontal, com cinco trilhas e sugestões de projetos.
- [Consulta Brasil](pdfs/consulta_brasil.pdf): relação completa por polo; leitura complementar à aula 3.
- [Histórico de integração: gráfico e tabela](pdfs/integracao_processadores.pdf): A4 horizontal, 13 chips com contagens e processos documentados.
- [Microeletrônica no Brasil — mapa e organizações](pdfs/mapa_brasil.pdf): pôster vetorial A3 horizontal.

A prática da aula 3 no **Cadence Virtuoso será elaborada posteriormente**. O encerramento tem **8 slides, para cerca de 15 minutos**, reservando **105 minutos** à futura prática. As seis páginas de listas regionais passaram para uma apresentação de consulta, preservando a relação integral de organizações e os créditos. O tempo da prática será validado quando seu roteiro for elaborado.

## O que é animado

- Histórico de contagens por die: marcos Intel, SoCs Apple M1–M4 e GPU NVIDIA A100.
- Deslocamento de uma lacuna após o movimento de um elétron.
- Difusão, recombinação e surgimento da depleção na junção PN.
- Mudança da largura de depleção em polarização direta e reversa.
- Depleção da superfície do NMOS, formação do canal e condução.
- Caminhos de carga/descarga do inversor.
- Estados 00 → 01 → 11 → 10 de NAND e NOR, com transistores habilitados em verde.
- Substituição do resistor R pela rede PMOS complementar na construção da NAND.
- Medição de atraso a 50%, comparação de cargas e carga/descarga da capacitância.
- Previsão e revelação do traço Y da NAND antes da prática.
- De Morgan com revelação da rede dual.
- Revelação de respostas e composição AND/OR.
- Formação conceitual de regiões, Gates e interconexões de um inversor planar.
- Exposição, revelação e gravação em litografia.
- Tunelamento por uma barreira de energia espessa e por uma mais fina.
- Transporte de dados entre bairros e entre andares de um prédio em corte, no panorama inicial, após VLSI e antes de CMOS 2.0; os bairros são formados por casas térreas.
- Prévia série/paralelo: chaves A/B → diodos → MOSFETs com controle externo A/B, antes das referências.

As animações são etapas vetoriais do Beamer, reproduzidas como páginas consecutivas. A versão `resumo` seleciona uma etapa de síntese; a versão principal contém toda a sequência.

## Âmbito Brasil

Os dados vêm da planilha PT-BR fornecida pelo usuário, vinculada ao **Brazil Silicon Roadmap, de Matheus Grossi**: <https://github.com/MattGrossi12/brazil_silicon_roadmap>.

Esta edição contém **54 organizações, 73 presenças em 13 polos**. Um nome pode aparecer em mais de um polo. Empresas e centros/grupos de pesquisa são distinguidos; o levantamento inclui projeto, ferramentas EDA, integração, fabricação e eletrônica aplicada. As incertezas sobre a atuação local são preservadas nos dados derivados.

O mapa foi redesenhado em TikZ com contorno simplificado de [johan/world.geo.json](https://github.com/johan/world.geo.json/blob/master/countries/BRA.geo.json). Os pontos são esquemáticos e representam polos agregados, incluindo regiões de interior; não representam endereços. A imagem enviada não é usada na apresentação. Créditos completos em [dados/CREDITOS_MAPA.md](dados/CREDITOS_MAPA.md).

## Editar e compilar

Com TeX Live e suporte a português, Beamer, TikZ, Circuitikz, PGFPlots, adjustbox, multicol, tcolorbox e latexmk:

```bash
bash compilar.sh
```

No Windows, com Python e pdfLaTeX disponíveis no terminal, execute `.\compilar.ps1`. Para selecionar o Python, use `.\compilar.ps1 -Python 'C:\caminho\python.exe'`. Consulte [o roteiro de revisão](ROTEIRO_REVISAO.md) para a organização do conteúdo.

O script usa os dados locais para gerar a seção Brasil e o gráfico de integração e compila os 12 PDFs em `pdfs/`. Registros e arquivos intermediários ficam em `build/`. A compilação não depende de acesso à internet.

- `slides/aula1.tex`, `slides/aula2.tex`, `slides/encerramento_aula3.tex`: apresentações.
- `slides/visuais.tex`: desenhos parametrizados e cores de estados.
- `slides/contexto_abertura.tex` e `slides/contexto_visuais.tex`: panorama histórico e gráficos.
- `slides/fabricacao_aula1.tex` e `slides/fisica_fabricacao_visuais.tex`: estrutura CMOS, fabricação, litografia e escalas físicas.
- `slides/perspectivas_aula1.tex` e `slides/cidade_visuais.tex`: limites, tunelamento, bairros e prédio em corte.
- `slides/microscopia_trecho.tex`: inclusão das micrografias reais quando os arquivos locais estiverem disponíveis.
- `scripts/obter_micrografias.py` e `dados/micrografias_fontes.json`: fontes de imagem e obtenção opcional.
- `slides/integracao_*.tex` e `dados/integracao_processadores.csv`: gráfico e contagens.
- `slides/previa_portas.tex`: circuitos série/paralelo do fechamento da aula 1.
- `slides/portas_visuais.tex`: construção da NAND, falhas, energia e estímulos da aula 2.
- `slides/trilhas_visuais.tex`: diagramas das cinco trilhas e integração de funções da aula 3.
- `slides/consulta_brasil.tex`: apresentação complementar com todas as organizações por polo.
- `slides/assets/facilitadores/`: fotografias extraídas dos currículos.
- `dados/FONTES_CONTEXTO.md` e `dados/processos_historicos.csv`: bibliografia e dados dos gráficos da abertura.
- `slides/comum.tex`: comandos compartilhados; o tema está na classe original `slides/libs/ufc_format.cls`.
- `slides/*_resumo.tex`: ativa o modo `handout` para produzir a síntese.
- `dados/*.csv`: índice derivado da planilha necessário ao mapa.
- `scripts/gerar_brasil.py`: recompõe mapa, listas e pôster a partir dos CSVs.
- `scripts/importar_planilha_brasil.py`: atualiza os CSVs a partir de uma planilha local indicada como argumento.
- `apoio/`: materiais para impressão.

Para atualizar os pacotes de entrega depois de compilar:

```bash
python3 empacotar.py
```

O ZIP Beamer contém os fontes e as figuras necessários ao Overleaf. Use pdfLaTeX e escolha a apresentação principal, ou sua versão `resumo`.

## Git e fontes de referência

O repositório Git local está nesta pasta (`material/`) na área de trabalho; os ZIPs de entrega não incluem a pasta `.git`. Para acompanhar o histórico a partir da pasta acima:

```bash
git -C material status
git -C material log --oneline
```

São versionados os fontes, os scripts, as figuras necessárias à compilação e os dados derivados do mapa. Os PDFs de entrega são versionados, conforme a organização incorporada ao repositório. ZIPs, currículos completos, planilhas originais, referências em PDF, textos extraídos e a cópia integral do template original ficam fora do versionamento. O brasão e o fundo de `slides/libs/` são dependências visuais do template.

Referências técnicas: Fathi Salem, *ECE 410: VLSI Design*; J.-M. Dutertre, *Digital Design (Introduction to)*, 2022; [Steve Ward — CMOS](https://computationstructures.org/notes/cmos/notes.html); [MIT 6.004](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/). Mini-fichas e fotos extraídas dos currículos fornecidos. Fontes primárias da contextualização histórica: [dados/FONTES_CONTEXTO.md](dados/FONTES_CONTEXTO.md). Template UFC: Maurício Moreira Neto; [créditos](CREDITOS_TEMPLATE.md).

Os diagramas de dispositivos e as analogias são qualitativos, sem resultados medidos ou simulados; as réguas de comprimentos indicam suas escalas. Os exemplos de tensões não definem um PDK. As legendas indicam as simplificações dos modelos. No gráfico histórico, referências de processo e nomes comerciais recentes são distinguidos; não se trata de uma medida uniforme do comprimento do transistor.

## Ritmo da aula 1

Apresentação e percurso: 5 min; panorama, VLSI e integração 3D: 18 min; materiais: 12 min; junção PN e discussão: 16 min; pausa: 10 min; MOSFET: 23 min; CMOS e desenho físico: 10 min; fabricação e litografia: 12 min; limites físicos: 6 min; atividade e fechamento: 8 min. Total: **120 minutos**. Os PDFs de notas e o guia de condução foram retirados; permanecem as apresentações, resumos, atividades e gabarito.

## Ritmo das aulas 2 e 3

Na aula 2: retomada e níveis lógicos (10 min); inversor, carga, atraso e energia (20 min); da carga resistiva à NAND (20 min); pausa (10 min); NOR e redes duais (20 min); desenho e teste entre duplas (25 min); composição, previsão das ondas e fechamento (15 min). Total: **120 minutos**.

A aula 3 reserva **105 minutos à prática** e **15 ao encerramento**: síntese do percurso (2 min), cinco trilhas (5 min), integração no produto (2 min), âmbito Brasil (3 min) e próximo projeto/créditos (3 min). A apresentação de consulta Brasil não integra esse tempo; pode ser explorada depois da oficina.

## Micrografias pendentes

As fotografias anteriores do componente Titan foram retiradas. A vista de circuito do NISE Network e a TEM de transistores GAA do imec foram identificadas, mas o download está bloqueado neste ambiente. **Elas ainda não aparecem nos PDFs e ZIPs desta edição.** Créditos, URLs e obtenção estão em [dados/CREDITOS_MICROGRAFIAS.md](dados/CREDITOS_MICROGRAFIAS.md). O histórico e seus critérios estão em [dados/FONTES_INTEGRACAO.md](dados/FONTES_INTEGRACAO.md). Com os arquivos disponíveis, a compilação inclui mais dois quadros.
