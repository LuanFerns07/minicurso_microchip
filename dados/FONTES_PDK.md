# gpdk045, dimensões W/L e corrente de Drain

Consulta das fontes em 31/10/2026. O trecho compartilhado entre aula 1 e roteiro visual contém três quadros. Não foram acrescentadas novas simulações nem redistribuídos os PDFs de referência.

- [Cadence — Basics of PDK, resposta de Andrew Beckett](https://community.cadence.com/cadence_technology_forums/f/custom-ic-design/36796/basics-of-pdk/1349734): natureza genérica do gpdk045 e composição de um PDK, incluindo símbolos, modelos, células parametrizadas e regras de verificação. O GPDK serve a ensino e demonstração; é diferente de um processo de fabricação contratado.
- [Cadence — GPDK045 Reference Manual, revisão 6.0, hospedado em Princeton](https://www.princeton.edu/~nverma/cadence_23.1/gpdk045_v_6_0/docs/gpdk045_pdk_referenceManual.pdf): referência do kit e dos dispositivos. Os modelos g45n1svt/g45p1svt correspondem aos dispositivos usados nas capturas. A tensão de 1 V nos slides é a aplicada na montagem do minicurso, não uma declaração de limite absoluto ou classificação de todos os dispositivos do kit.
- [MIT 6.101, aula 6, Spring 2020, pp. 19–20](https://web.mit.edu/6.101/www/s2020/handouts/L06.pdf): aproximação de canal longo, dependência W/L e limitações da lei quadrática em canais curtos.
- [Quick Start local](../praticas/QUICK_START.md): gpdk045, Virtuoso Studio IC23.1, nmos1v/pmos1v, alimentação aplicada de 1 V e dimensões iniciais W = 120 nm, L = 45 nm, um finger e multiplicador 1.

## Desenhos e comparação

Os três inversores representam pares PMOS/NMOS com 120/45, 240/45 e 120/90 nm. Cada par usa as mesmas dimensões para P e N, acompanhando o ponto de partida da prática. Isso não garante correntes P/N iguais. As variações são exemplos propostos, sem resultados simulados ou aprovação de regras de geometria. A representação preserva as razões das dimensões de canal entre os exemplos; contatos e espaçamentos são conceituais.

## Equação e hipóteses

A expressão apresentada é `I_DS ≈ (mu_n C_ox / 2) (W/L) (V_GS − V_TN)^2`, para um NMOS de canal longo em inversão forte e saturação, com corpo no Source, `V_GS > V_TN` e `V_DS >= V_GS − V_TN`. Mobilidade constante, ausência de modulação de comprimento e demais simplificações estão implícitas nesse modelo ideal. Não foram inventados valores de mobilidade, Cox, limiar ou corrente absoluta para o PDK instalado.

Com os demais fatores constantes, as razões W/L são 8/3, 16/3 e 4/3, dando correntes relativas ideais 1, 2 e 1/2. A tabela se refere a um transistor polarizado, e não calcula consumo estático de uma porta. Em 45 nm, a simulação usa os modelos do PDK; as razões exatas não são garantidas. Aumentar W também altera capacitâncias, portanto corrente maior isoladamente não determina o atraso de um circuito.
