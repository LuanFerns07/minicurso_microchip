# Fontes e imagens da aula 1

Consulta em **29 de outubro de 2026**. Os links aparecem também junto às figuras na apresentação. Diagramas, gráficos e analogia urbana foram desenhados para o minicurso. As fotografias documentais do chip foram extraídas de uma apresentação científica identificada abaixo; os retratos vêm dos currículos fornecidos.

## História e Lei de Moore

- [Computer History Museum — The Silicon Engine: Timeline](https://www.computerhistory.org/siliconengine/timeline/): transistor de contato pontual em 1947, circuitos integrados em 1958–59, demonstração do MOS em 1960 e CMOS em 1963. A linha do tempo é seletiva e não tem espaçamento proporcional aos anos.
- [Intel — The Intel 4004](https://www.intel.com/content/www/us/en/history/virtual-vault/articles/the-intel-4004.html): marco do microprocessador em 1971.
- [Intel — Moore’s Law](https://www.intel.com/content/www/us/en/newsroom/resources/moores-law.htm): previsão de duplicação anual em 1965, revisada em 1975 para aproximadamente dois anos. O gráfico da aula é **uma curva matemática ilustrativa**, com quantidade relativa 1, 2, 4, 8 e 16 nos anos relativos 0, 2, 4, 6 e 8. Não é uma série medida nem uma previsão garantida de frequência ou desempenho.

## Miniaturização

- [Intel — Microprocessor Quick Reference Guide](https://www.intel.com/pressroom/kits/quickreffam.htm): referências históricas de fabricação para 4004, 8086, 386 DX, Pentium, Pentium 4 e Atom Z500. Valores selecionados em `processos_historicos.csv`.
- [TSMC — Relatório anual 2020](https://investor.tsmc.com/static/annualReports/2020/english/index.html): início da produção em volume do N5 em 2020.
- [TSMC — Relatório anual 2025](https://investor.tsmc.com/static/annualReports/2025/english/index.html): início da produção em volume do N2 no quarto trimestre de 2025.

O gráfico usa eixo vertical logarítmico e mostra **referências de gerações de processo**. Não deve ser lido como comprimento de porta medido de modo uniforme. Os pontos recentes N5 e N2 são nomes comerciais, desenhados vazados e separados da linha histórica. Não se pode calcular a redução real de área ou comprimento do transistor dividindo esses números. Dimensões de porta, passo dos contatos, passo de metal, resolução óptica e nome do nó são grandezas diferentes.

## Fabricação, litografia e estruturas de transistor

- [ASML — How microchips are made](https://www.asml.com/en/technology/all-about-microchips/how-microchips-are-made) e [Six crucial steps in semiconductor manufacturing](https://www.asml.com/en/company/stories/2021/semiconductor-manufacturing-process-steps): deposição, resiste, exposição, revelação, gravação e implantação. O corte CMOS mostra grupos de estruturas de um processo planar bulk; não fornece uma sequência fabricável ou um conjunto de máscaras.

- [ASML — Lithography principles](https://www.asml.com/en/technology/lithography-principles): exposição de resiste, formação de padrões e fabricação em camadas.
- [ASML — Light and lasers](https://www.asml.com/en/technology/lithography-principles/light-and-lasers): DUV ArF com 193 nm e EUV com 13,5 nm.
- [ASML — Lenses and mirrors](https://www.asml.com/en/technology/lithography-principles/lenses-and-mirrors): lentes em DUV e espelhos em EUV.
- [ASML — 5 things you should know about High NA EUV](https://www.asml.com/en/company/stories/2024/5-things-high-na-euv): abertura numérica e resoluções das plataformas EUV NXE e EXE. Os valores nominais de resolução de 13 nm e 8 nm não são dimensões de transistores de nós comerciais com nomes semelhantes.
- [ASML — High NA EUV reaches new readiness milestone, 15/07/2026](https://www.investor.asml.com/news-releases/news-release-details/high-na-euv-reaches-new-readiness-milestone): adoção em camadas selecionadas de um subconjunto de produtos, sem pressupor adoção generalizada.
- [imec — Introducing 2D-material based devices in the logic scaling roadmap](https://www.imec-int.com/en/articles/introducing-2d-material-based-devices-logic-scaling-roadmap): dificuldades de controle do canal ao reduzir dimensões.
- [imec — Outer wall forksheet: bridging nanosheet and CFET](https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology): porta envolvendo os canais nos dispositivos GAA.

A sequência de litografia usa um resiste positivo e uma camada a gravar, sem modelar uma máquina específica. A figura de transistor mostra cortes transversais ao canal: porta azul, canal verde e dielétrico branco. Empilhamento de canais dentro de um transistor e empilhamento de circuitos completos representam escalas de integração distintas.

## Escala atômica e tunelamento

- [Royal Society of Chemistry — Silicon](https://periodic-table.rsc.org/element/14/silicon): raio covalente de 1,14 Å = 0,114 nm. O diâmetro de referência utilizado é **0,228 nm**, calculado como duas vezes esse raio. O tamanho do átomo depende da definição; ele não tem uma borda rígida.
- [NIST — Certification of SRM 640g](https://www.nist.gov/publications/certification-standard-reference-materialr-640g-line-position-and-line-shape-standard): parâmetro da rede do silício de aproximadamente **0,543 nm**. Para a estrutura cúbica do diamante, a separação entre vizinhos mais próximos é calculada por `a × sqrt(3) / 4`, aproximadamente **0,235 nm**. Não confundir essa separação com o parâmetro da célula unitária ou com o diâmetro covalente.
- [ASML — TWINSCAN EXE:5000](https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5000): resolução nominal de **8 nm**, luz EUV de **13,5 nm** e NA de 0,55. A régua compara comprimentos, não capacidades de um transistor: `8 / 0,235 ≈ 34` separações entre vizinhos, numa linha ilustrativa. O nó N2 não é representado como comprimento físico de porta.
- [NIST — Challenges of High-kappa Gate Dielectrics for Future MOS Devices](https://www.nist.gov/publications/challenges-high-kappa-gate-dielectrics-future-mos-devices): aumento de tunelamento em dielétricos muito finos.
- [Intel — Gate Dielectric Scaling for High-Performance CMOS: from SiO2 to High-K](https://www.intel.com/content/dam/doc/guide/gate-dielectric-scaling-for-cmos-guide.pdf): uso de high-k para manter acoplamento elétrico com maior espessura física. A sequência de barreira mantém energia e altura fixas e reduz apenas a espessura. As setas são qualitativas, sem escala de probabilidade ou corrente. Não é um gráfico de corrente medido.

## Limites e integração 3D

- [imec — The CMOS 2.0 Revolution](https://www.imec-int.com/en/articles/cmos-20-revolution): restrições de interconexão, energia, custo e escalabilidade; co-otimização de sistema e tecnologia.
- [imec — A path to high-density front- and backside wafer connectivity](https://www.imec-int.com/en/articles/path-high-density-front-and-backside-wafer-connectivity): camadas funcionais heterogêneas, conexões 3D densas e alimentação pelo verso como caminhos para CMOS 2.0.
- [imec — University consortium around next-generation chips, 12/03/2026](https://www.imec-int.com/en/press/imec-launches-university-consortium-around-next-generation-chips): iniciativa de pesquisa envolvendo ferramentas de projeto e arquitetura.

A comparação **bairros → andares do mesmo prédio** é uma analogia própria para aproximar memória e processamento. Ela não afirma que toda memória antes estava fora do chip, que a comunicação passa a ter custo zero ou que todo empilhamento 3D é CMOS 2.0. Produtos com memória empilhada já existem; a proposta CMOS 2.0 amplia a partição e integração heterogênea dentro do sistema. A ordem das camadas no desenho é ilustrativa. Fabricação, calor, teste e ferramentas continuam sendo desafios.

## Facilitadores e fotografias

Fotos extraídas diretamente dos currículos locais fornecidos, sem geração ou alteração dos retratos:

- `slides/assets/facilitadores/luan.png`: imagem do currículo `CV_Luan.pdf`.
- `slides/assets/facilitadores/luiz.jpg`: imagem do currículo `CV_Luiz_SOARES_Analog_IC_Design.pdf`.

Os textos resumem os percursos documentados e não pressupõem que todos os cursos estejam concluídos. Os currículos completos e os contatos pessoais não integram os pacotes nem o repositório.

## Fotografias de componentes e microscopia óptica

**Crédito:** Thomas Roche, Victor Lomné, Camille Mutschler e Laurent Imbert, *A Side Journey to Titan — Revealing and Breaking NXP’s P5x ECDSA Implementation on the Way*, apresentação das Journées SIF, **15/10/2021**. Instituições: NinjaLab e LIRMM / Univ. Montpellier / CNRS. Registro do evento: [Journées sécurité SIF](https://archive.socinfo.fr/les-journees-sif/journees-securite-14-et-15-octobre-2/). Projeto e artigo dos mesmos autores: [USENIX Security 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/roche).

As três figuras foram extraídas dos objetos de imagem do PDF local da apresentação, preservando os pixels, as proporções e as anotações originais. O documento completo não foi copiado para o repositório.

| Arquivo | Origem no PDF da apresentação SIF | O que mostra |
| --- | --- | --- |
| `slides/assets/microscopia/titan_placa.png` | Página 6, quadro 5/23 | Placa com o encapsulamento NXP A7005 e outros componentes identificados pelos autores. |
| `slides/assets/microscopia/titan_aberto.png` | Página 8, quadro 7/23 | Encapsulamento aberto, revelando o die de silício. |
| `slides/assets/microscopia/titan_microscopio.png` | Página 9, quadro 8/23 | Observação óptica do chip e da sonda do experimento original. |

São fotografias documentais de um exemplo de 2021, não micrografias de um processo de 2 nm. A imagem óptica não resolve canais de transistores individuais. A aula usa as fotos para distinguir placa, encapsulamento e die; os cortes de dispositivos e as escalas nanométricas são explicados nos diagramas seguintes. Não foram geradas imagens sintéticas de microscópio. Os créditos acompanham a reprodução na apresentação.
