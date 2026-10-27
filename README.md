# Do transistor ao chip

Minicurso em português, com três encontros de 1h30. Desenvolvimento e facilitação: **Luan F. Nogueira e Luiz F. de Melo Soares**.

## PDFs para uso

- [Aula 1 — Do silício ao MOSFET](pdfs/aula1.pdf): 38 slides, incluindo mini-fichas dos facilitadores, fundamentos, exercícios e referências.
- [Aula 2 — Do MOSFET às portas lógicas](pdfs/aula2.pdf): 39 slides principais e 3 de aprofundamento opcional (AOI21 e XOR).
- [Encerramento da aula 3 — Para onde seguir?](pdfs/encerramento_aula3.pdf): 12 slides sobre digital, analógica, sinais mistos, RF integrada, arquitetura de computadores e outros desdobramentos.
- [Roadmap em uma página](pdfs/roadmap.pdf): versão A4 horizontal para distribuir ou imprimir.
- [Folhas de atividades](pdfs/exercicios.pdf) e [gabarito comentado](pdfs/gabarito.pdf).
- [Guia dos facilitadores](pdfs/guia_facilitadores.pdf): cronograma, condução, critérios de aprendizagem, limites do modelo e mini-fichas ampliadas.
- PDFs com slides e notas intercaladas: [aula 1](pdfs/aula1_notas.pdf), [aula 2](pdfs/aula2_notas.pdf) e [encerramento](pdfs/encerramento_aula3_notas.pdf).

A prática no **Cadence Virtuoso está reservada para elaboração posterior**. O arquivo de encerramento contém apenas o bloco final da aula 3, para ser usado depois da prática; ele não constitui uma aula prática completa. O guia reserva até 20 minutos finais ao roadmap e 70 minutos à futura prática. A proposta original de protoboard foi substituída por essa orientação.

## Editar e compilar

Os arquivos principais são `slides/aula1.tex`, `slides/aula2.tex` e `slides/encerramento_aula3.tex`. A classe `slides/libs/ufc_format.cls` define o tema original. `slides/comum.tex` reúne os comandos de conteúdo e os esquemas compartilhados. As notas são os comandos `\note{...}` junto aos slides; os arquivos `*_notas.tex` ativam sua exibição. Os materiais para impressão ficam em `apoio/`.

Com uma distribuição TeX Live que tenha suporte a português, Beamer, TikZ, Circuitikz, tcolorbox, adjustbox e latexmk, execute nesta pasta:

```bash
bash compilar.sh
```

O script compila os dez PDFs em `pdfs/` e mantém arquivos intermediários e registros em `build/`. Pode ser executado novamente após alterações. Para atualizar os ZIPs de entrega, execute `python3 empacotar.py` depois da compilação.

Para compilar só uma apresentação, a partir de `material/`:

```bash
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error -outdir=../build slides/aula1.tex
```

Para usar o Beamer no Overleaf, carregue **o conteúdo do ZIP `minicurso_cmos_beamer.zip`**. Selecione `aula1.tex`, `aula2.tex` ou `encerramento_aula3.tex` como documento principal e use pdfLaTeX. Os arquivos compartilhados e `libs/` já estão na posição necessária nesse ZIP. Os materiais para impressão são compilados pelo script local; sua árvore de diretórios é preservada no pacote completo.

## Escolhas didáticas

- Percurso: materiais e portadores → junção PN → MOSFET → inversor → redes duais → NAND/NOR → universalidade → próximos caminhos.
- Aulas 1 e 2 incluem uma pausa de 5 minutos e atividades dentro dos 90 minutos; o guia detalha os blocos de tempo. A versão ampliada inclui formação de canal, corpo, dimensões W/L, regimes de operação, margens de ruído, formas de onda e exemplos resolvidos. Os conceitos adicionais devem ser apresentados de forma breve, com os detalhes das notas disponíveis para consulta.
- AOI21 e XOR são opcionais; não acrescentar sua exposição aos 90 minutos previstos.
- Termos usuais em inglês são acompanhados de tradução ou explicação. Algumas referências externas estão em inglês, como sinalizado nos slides; o conteúdo autoral é em português.
- Esquemas de três terminais omitem o corpo, explicitando sua conexão nos textos. Usa-se o modelo introdutório bulk, com corpos NMOS em GND e PMOS em VDD.
- Tensões de 1,2 V e limiares de 0,4 V são exemplos didáticos; não definem um processo, PDK ou laboratório. Curvas são qualitativas, não resultados medidos ou simulados.
- A formação nas mini-fichas é descrita como percurso; não se presume conclusão de curso nem vínculo profissional atual. Não foram incluídos contatos pessoais dos currículos.

## Referências e identidade visual

- `card_minicurso_semicondutores_3_dias.pdf`: planejamento original fornecido, adaptado à prática no Virtuoso.
- Fathi Salem, Michigan State University: *ECE 410: VLSI Design — Course Lecture Notes*, arquivo `LECTURE_logic_gate.pdf`. As referências 2.x são as páginas impressas no material.
- J.-M. Dutertre: *Digital Design (Introduction to)*, Cours 3A ISMIN, 2022, arquivo `figures_course_digital_design.pdf`.
- `CV_Luan.pdf` e `CV_Luiz_SOARES_Analog_IC_Design.pdf`: fontes das mini-fichas.
- Maurício Moreira Neto: *Template Beamer UFC*, ZIP fornecido. A classe `ufc_format.cls` é idêntica à do ZIP. Os slides usam a proporção original **4:3 (128 × 96 mm)**, com capa, fundo, brasão, navegação por seções, rodapé, fontes e blocos definidos pelo próprio template. Diagramas e tabelas foram ajustados à área de conteúdo, sem alterar o tema. O template declara não ser um documento oficial da UFC.
- [Steve Ward — CMOS, Computation Structures](https://computationstructures.org/notes/cmos/notes.html).
- [MIT OpenCourseWare — 6.004 Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/).
- [Cadence — Integrated Circuit Design](https://www.cadence.com/en_US/home/explore/what-is-ic-design.html).
- [Synopsys — Mixed-Signal Integrated Circuit](https://www.synopsys.com/glossary/what-is-mixed-signal-integrated-circuit.html).
- [Synopsys — RF Circuit Design](https://www.synopsys.com/glossary/what-is-rf-circuit-design.html).

As fontes externas foram consultadas em outubro de 2026. A sequência do roadmap e os projetos sugeridos são uma proposta didática dos facilitadores. Os diagramas são vetoriais, desenhados em TikZ/Circuitikz a partir dos conceitos das referências. Os currículos e PDFs de referência não são redistribuídos nos ZIPs de entrega.
