# Histórico de integração: fontes e critérios

Seleção didática de **13 chips, de 1971 a 2024**, consultada em 29/10/2026. Os valores completos, o processo, a classe do dispositivo, a revisão escolhida e o link de cada linha estão em [integracao_processadores.csv](integracao_processadores.csv).

## O que o gráfico representa

O eixo vertical mostra **transistores por die**, em escala logarítmica; o horizontal, o ano de lançamento. Não representa o total em uma placa de computador. As contagens são os números publicados pelos fabricantes ou autores do projeto, geralmente arredondados. A linha dos marcos Intel apenas guia o olhar; não é um ajuste estatístico da Lei de Moore.

O primeiro avanço apresenta oito marcos Intel. O segundo mantém esses pontos em cinza e acrescenta Apple M1–M4 e NVIDIA A100/GA100, com uma tabela de contagens e processos. A mesma escala é mantida nos dois avanços.

## Fontes primárias

- [Intel — Microprocessor Quick Reference Guide](https://www.intel.com/pressroom/kits/quickreffam.htm): 4004, 8086, 386 DX, Pentium, Pentium 4 e Core 2 Duo. Há revisões com processos e contagens diferentes; a tabela fixa uma configuração em cada caso.
- [Intel — Multicore Architecture Briefing, 2008](https://www.intel.com/pressroom/archive/releases/2008/20080317fact.htm): Nehalem, 45 nm e 731 milhões de transistores.
- [A 22nm IA multi-CPU and GPU System-on-Chip, ISSCC 2012](https://ieeexplore.ieee.org/document/6176876/): Ivy Bridge, aproximadamente 1,4 bilhão de transistores na configuração maior. DOI: 10.1109/ISSCC.2012.6176876.
- [Apple — M1, 2020](https://www.apple.com/newsroom/2020/11/apple-unleashes-m1/): 16 bilhões, processo de 5 nm.
- [Apple — M2, 2022](https://www.apple.com/newsroom/2022/06/apple-unveils-m2-with-breakthrough-performance-and-capabilities/): 20 bilhões, segunda geração de 5 nm.
- [Apple — M3, 2023](https://www.apple.com/newsroom/2023/10/apple-unveils-m3-m3-pro-and-m3-max-the-most-advanced-chips-for-a-personal-computer/): M3 base com 25 bilhões, processo de 3 nm.
- [Apple — M4, 2024](https://www.apple.com/newsroom/2024/05/apple-introduces-m4-chip/): M4 base com 28 bilhões, segunda geração de 3 nm.
- [NVIDIA — Ampere Architecture In-Depth, 2020](https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth/): GA100 usado no A100, 54,2 bilhões, TSMC 7 nm N7. A memória HBM externa ao die não entra nessa contagem.
- [Apple Developer — Apple silicon](https://developer.apple.com/documentation/apple-silicon): identificação da arquitetura arm64; “Apple” indica o projetista dos SoCs e “Arm” a arquitetura, não um segundo fabricante do mesmo chip.

## Limites da comparação

CPU, SoC e GPU têm funções, áreas e proporções de memória diferentes. O total do SoC inclui CPU, GPU, caches, interfaces e aceleradores. A contagem não permite inferir diretamente desempenho ou transistores por mm². Não foram misturadas contagens de pacotes multidie com contagens de dies individuais.

A coluna **processo**, às vezes chamada informalmente de litografia, é a designação nominal publicada. Não é o comprimento de onda da luz nem uma medida uniforme do comprimento da porta. Não foram inferidas variantes TSMC N5P/N3B/N3E quando o comunicado citado informa somente a geração em nanômetros.

O gráfico e a tabela são regenerados por `python3 scripts/gerar_integracao.py`. Os fontes gerados estão em `slides/integracao_visual.tex`, `slides/integracao_trecho.tex` e `apoio/integracao_processadores.tex`.
