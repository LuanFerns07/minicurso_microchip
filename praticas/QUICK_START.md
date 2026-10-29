# Quick Start — Práticas de CMOS no Cadence Virtuoso

Documento em construção a partir das montagens e capturas reais do minicurso. Este roteiro é separado das apresentações existentes.

## Percurso das três aulas

| Aula | Prática | Células previstas |
| --- | --- | --- |
| 1 | Caracterização de NMOS e PMOS: corrente em função das tensões | `a1_tb_nmos`, `a1_tb_pmos` |
| 2 | Redes pull-up/pull-down, inversor, NAND e NOR | `a2_inv`, `a2_nand2`, `a2_nor2` e respectivos testbenches |
| 3 | Layout de um inversor, verificações e comparação com a simulação após extração | `a3_inv`, `a3_tb_inv` |

Ambiente observado nas capturas: Virtuoso Studio IC23.1, biblioteca tecnológica `gpdk045`. O fluxo de simulação será documentado no ADE Assembler, conforme a sessão utilizada nas capturas. O ADE Explorer também aparece como opção de abertura, mas seus passos específicos não foram registrados. Os próximos módulos serão preenchidos à medida que forem executados; o primeiro resultado registrado é a família de curvas DC do NMOS, descrita ao final desta etapa. As variáveis e a parametrização de vgs estão documentadas; ainda faltam as capturas da configuração dos modelos e da seleção da saída para completar o passo a passo.

## Aula 1 — Preparar o teste do NMOS

**Objetivo desta etapa:** criar o schematic e selecionar os componentes necessários à polarização independente da porta e do dreno.

### 1. Criar a biblioteca

No Library Manager, abra **File → New → Library**. Use o nome `minicurso_cmos` e vincule a biblioteca à tecnologia existente `gpdk045`.

A captura registra o acesso ao menu. A janela de vinculação tecnológica ainda precisa ser capturada para completar esta etapa.

![Acesso ao comando de criação de biblioteca](imagens/01-nova-biblioteca.png)

### 2. Criar a célula de teste

Abra **File → New → Cell View**.

![Acesso ao comando de criação de célula](imagens/02-nova-celula.png)

Preencha conforme a captura:

| Campo | Valor |
| --- | --- |
| Library | `minicurso_cmos` |
| Cell | `a1_tb_nmos` |
| View | `schematic` |
| Type | `schematic` |
| Open with | `Schematics L` |

Clique em **OK**.

![Configuração da célula a1_tb_nmos](imagens/03-configuracao-celula.png)

Confira no título do editor a biblioteca, a célula e a vista abertas.

![Editor com o schematic vazio](imagens/04-schematic-vazio.png)

### 3. Inserir o transistor

Com o foco na área do schematic, pressione **i** (bindkey para inserir instância neste ambiente). Na janela **Add Instance**, selecione a biblioteca `gpdk045`, célula `nmos1v` e vista `symbol`. Posicione uma instância e pressione **Esc** para encerrar a inserção.

Parâmetros observados na captura, mantidos como ponto de partida:

| Parâmetro | Valor |
| --- | --- |
| Model Name | `g45n1svt` |
| Length | `45n` (45 nm) |
| Finger Width / Total Width | `120n` (120 nm) |
| Fingers | `1` |
| Multiplier | `1` |

![Seleção do NMOS e parâmetros do dispositivo](imagens/05-nmos1v.png)

O símbolo possui quatro terminais. Na orientação mostrada: porta à esquerda, dreno acima, fonte abaixo e corpo à direita. A ligação do corpo será explícita no circuito de teste.

### 4. Inserir as fontes DC

Pressione **i** novamente. Selecione `analogLib` → `vdc` → `symbol`.

![Seleção da fonte de tensão contínua](imagens/06-fonte-vdc.png)

Para as curvas do NMOS, use duas fontes independentes: uma entre porta e referência, outra entre dreno e referência. Os valores e as variáveis de varredura serão registrados na próxima etapa, após conferir as propriedades das fontes e o ADE.

### 5. Inserir os símbolos de referência

Em **Add Instance**, selecione `analogLib` → `gnd` para a referência de terra. A captura específica de seleção de `gnd` ainda precisa ser acrescentada.

A seleção de `analogLib` → `vdd` está registrada abaixo. Esse símbolo identifica uma rede de alimentação; **não gera tensão**. A tensão é aplicada por uma fonte, como `vdc`. O símbolo `vdd` é opcional neste teste com duas fontes independentes.

![Seleção do símbolo de alimentação vdd](imagens/07-simbolo-vdd.png)

### 6. Próxima montagem: conexões a conferir

| Terminal | Conexão planejada |
| --- | --- |
| Fonte (S) | Terra |
| Corpo (B) | Terra, junto à fonte |
| Porta (G) | Terminal positivo da fonte de controle |
| Dreno (D) | Terminal positivo da fonte de polarização do dreno |
| Terminais negativos das duas fontes | Terra |

Com fonte e corpo em terra, a tensão da porta corresponde a VGS e a do dreno corresponde a VDS. Essa montagem permite variar uma tensão enquanto a outra permanece fixa.

**Checkpoint:** capturar o circuito completamente conectado e as propriedades das duas fontes. Depois conferir o schematic, configurar os modelos e executar a primeira análise DC no ADE Explorer.

### 7. Configurar os componentes, a alimentação e conferir as ligações

Use a montagem abaixo como referência. Fonte e corpo do NMOS compartilham o terra; porta e dreno são polarizados por fontes independentes.

![Montagem do NMOS com fontes de polarização e referência de alimentação](imagens/11-montagem-nmos-com-referencia-vdd.png)

| Fonte | Campo DC voltage | Função |
| --- | --- | --- |
| `V0` | `vgs` | Polarizar a porta em relação ao terra |
| `V3` | `vds` | Polarizar o dreno em relação ao terra |
| `V2` | `1` (1 V) | Estabelecer a alimentação demonstrativa da rede `vdd` |

As expressões `vgs` e `vds` serão definidas no ADE. A janela de propriedades abaixo corresponde a **V2**, configurada em **1 V**.

![Propriedades da fonte V2 de 1 V](imagens/09-propriedades-vdc.png)

**Por que manter V2 e o símbolo vdd?** A fonte estabelece a diferença de potencial em relação ao terra; os símbolos identificam e conectam redes. Em circuitos maiores, repetir os símbolos de alimentação apropriados permite distribuir VDD e terra sem desenhar fios atravessando todo o schematic. Conferir os nomes efetivos das redes, incluindo a indicação de rede global (`!`) quando aplicável: um pino local e uma rede global de nomes parecidos não são necessariamente a mesma conexão.

Neste teste, V2 e o símbolo `vdd` são mantidos para essa explicação didática. A rede VDD não está ligada à porta nem ao dreno do NMOS; portanto, V2 não determina os valores de `vgs` ou `vds`.

As propriedades de `NM0` confirmam `gpdk045/nmos1v`, modelo `g45n1svt`, comprimento `45n`, largura total `120n`, um finger e multiplicador 1. Manter esses valores nesta primeira montagem. O campo `Bodytie Type = None` não substitui a conexão explícita do terminal de corpo no schematic.

![Propriedades do NMOS NM0](imagens/10-propriedades-nmos.png)

**Checkpoint antes do ADE:** confirmar as conexões dos terminais negativos das fontes ao terra e a união entre fonte e corpo do NMOS; executar **Check and Save** e examinar os avisos; conferir as propriedades de V0 e V3. A proximidade gráfica não garante continuidade elétrica. Depois abrir o **ADE Assembler** para configurar modelos, variáveis e análise DC. Ainda não há simulação validada.

### 8. Abrir o ADE Assembler

No editor de schematic, abra **Launch → ADE Assembler**. O menu também oferece **ADE Explorer**; neste roteiro, acompanhar as telas do Assembler utilizadas na prática.

![Menu Launch com ADE Explorer e ADE Assembler](imagens/12-launch-ade.png)

A tela inicial apresenta a sessão de simulação, com a aba `maestro` e o painel **Data View**. Na captura inicial, ainda não há testes configurados.

![Tela inicial do ADE Assembler](imagens/13-inicio-assembler.png)

### 9. Criar o teste do NMOS

Na página inicial, a seção **Tests** oferece o link para definir um novo teste. Criar um teste associado ao schematic `minicurso_cmos/a1_tb_nmos`. A janela intermediária de criação e seleção do design ainda precisa ser capturada para completar o passo a passo.

O painel **Data View** organiza testes, variáveis globais, parâmetros e corners. Variáveis globais devem ser usadas quando se deseja compartilhar valores entre testes; para a primeira caracterização, registrar as variáveis no próprio teste.

![Organização do painel Data View](imagens/14-data-view.png)

Após a criação, a captura mostra o teste `minicurso_cmos_a1_tb_nmos_1`, com **Simulator = spectre**, a seção **Analyses** e a seção **Design Variables**.

![Primeiro teste com Spectre e áreas de análises e variáveis](imagens/15-primeiro-teste.png)

### 10. Definir as variáveis e parametrizar VGS

Em **Design Variables**, registrar as variáveis com os mesmos nomes usados nas fontes do schematic: `vds` e `vgs`.

Na captura, `vds` tem valor de referência **500m** (0,5 V). Durante a análise DC do ponto 11, esse valor é substituído pelos pontos da varredura de **0 a 1 V** definida na própria análise.

Para `vgs`, abrir o editor de parametrização da variável e preencher a janela **Parameterize**:

| Campo | Valor registrado |
| --- | --- |
| Especificação | `From/To` |
| Step Type | `Auto` |
| From | `100m` (0,10 V) |
| To | `700m` (0,70 V) |
| Total Steps | `5` |

![Variáveis do teste e parametrização de vgs](imagens/19-variaveis-varredura-vgs.png)

Confirmar em **OK**. A família de curvas registrada no ponto 13 confirma cinco valores: **0,10; 0,25; 0,40; 0,55 e 0,70 V**.

As duas varreduras têm funções distintas: para cada valor parametrizado de **VGS**, executar a análise DC variando **VDS** de 0 a 1 V. Assim, cada curva mostra ID em função de VDS para um VGS fixo. Salvar a configuração da sessão para reutilizar o teste.

O menu de análises também oferece transiente (`tran`), para observar a evolução no tempo, e AC, para resposta de pequenos sinais em frequência. Nesta etapa, utilizar **DC com varredura**, conforme o ponto 11.

### 11. Configurar a varredura DC de VDS

Na janela **Choosing Analyses**, selecionar **dc** e preencher conforme a captura:

| Campo | Configuração registrada |
| --- | --- |
| Save DC Operating Point | Marcado |
| Sweep Variable | `Design Variable` |
| Variable Name | `vds` |
| Sweep Range | `Start-Stop` |
| Start / Stop | `0` / `1` V |
| Sweep Type | `Automatic` |
| Enabled | Marcado |

Confirmar em **OK**. A janela de seleção de análise aparece com o título **ADE Explorer**, embora a sessão principal registrada seja do Assembler; esta captura documenta o formulário efetivamente utilizado.

![Configuração da análise DC, variando vds de 0 a 1 V](imagens/16-analise-dc-vds.png)

Esta análise varia a tensão da fonte de dreno. Para gerar uma família de curvas, repetir a análise para diferentes valores de `vgs`. A legenda do resultado registra **0,10; 0,25; 0,40; 0,55 e 0,70 V**. A parametrização adicional de `vgs` está documentada no ponto 10; a janela DC acima define a varredura de `vds`.

### 12. Selecionar a corrente de saída e executar

O menu de adição de saídas oferece **Signal** e **Expression**, entre outras opções. Para esta caracterização, adicionar como saída a corrente no terminal de dreno de `NM0`; no gráfico enviado, ela aparece como **`/NM0/D`**. Selecionar o terminal para medir corrente, distinguindo-o da seleção de uma rede para medir tensão. A etapa de seleção no schematic e a tabela final de saídas ainda precisam de captura.

![Menu de saídas e controles de execução](imagens/17-saidas-e-execucao.png)

Após conferir análise, variáveis, modelos e saída, executar a simulação pelo botão triangular verde. O botão quadrado é o controle de parada. Salvar a configuração da sessão para repetir o teste.

### 13. Interpretar a família de curvas do NMOS

![Corrente de dreno em função de vds para cinco valores de vgs](imagens/18-curvas-id-vds.png)

O gráfico registrado apresenta:

- **Eixo horizontal:** `vds`, de 0 a 1 V.
- **Eixo vertical:** corrente no dreno, em microampères.
- **Cinco curvas:** uma para cada valor de `vgs` indicado na legenda.
- **Tendência observada:** a corrente aumenta ao elevar `vgs`. Para `vgs = 0,70 V`, a curva chega aproximadamente a 10 µA em `vds = 1 V`.

Para cada curva, observar o crescimento inicial da corrente e a mudança de inclinação ao aumentar VDS. A curva de maior corrente continua crescendo de modo perceptível na região de VDS elevado: não esperar um patamar perfeitamente horizontal nem usar esse gráfico isolado para extrair um limiar exato. A identificação quantitativa da região de operação deve ser apoiada pelos parâmetros de ponto de operação do modelo, se for incluída na prática.

**Perguntas para a turma:** qual curva corresponde à maior condução? O que muda ao elevar VGS mantendo VDS fixo? A corrente fica rigorosamente constante depois da mudança de inclinação? As curvas próximas do eixo permitem concluir que a corrente é exatamente zero?

**Checkpoint:** o primeiro resultado de simulação foi registrado. As variáveis e as duas varreduras já estão documentadas nos pontos 10 e 11. Para fechar sua reprodução no roteiro, acrescentar a configuração dos modelos e a seleção da corrente de dreno. Depois preparar a curva **ID × VGS**, mantendo VDS fixo, antes de passar ao PMOS.

## Aula 1 — PMOS

Na célula `a1_tb_pmos`, foi repetido o procedimento de montagem e simulação DC utilizado no NMOS, adaptando as ligações e as polaridades para o PMOS.

![Montagem do teste do PMOS](imagens/20-montagem-pmos.png)

O transistor `PM0` utiliza o modelo `g45p1svt`, com **L = 45 nm**, **W = 120 nm** e multiplicador **1**, conforme as anotações do schematic. Fonte e corpo estão ligados à rede VDD, alimentada por `V2 = 1 V`. As fontes de controle usam **`vsg`** e **`vsd`**:

- **VSG = VS − VG:** fonte de controle com terminal positivo na fonte do PMOS e negativo na porta.
- **VSD = VS − VD:** fonte de polarização com terminal positivo na fonte do PMOS e negativo no dreno.

Repetir a análise DC com `vsd` variando de **0 a 1 V** e a parametrização de `vsg` nos mesmos cinco valores utilizados para o NMOS: **0,10; 0,25; 0,40; 0,55 e 0,70 V**. O procedimento é o mesmo, substituindo os nomes das variáveis e respeitando as polaridades acima. A captura do resultado mostra a família em função de `vsd`; os valores individuais de `vsg` não estão expandidos na legenda dessa imagem.

![Família de curvas DC do PMOS em função de vsd](imagens/21-curvas-pmos.png)

**Atenção à corrente selecionada:** no NMOS, o resultado registrado foi `/NM0/D`; neste PMOS, a saída exibida é **`/PM0/S`**, corrente no terminal de fonte, em µA. Manter essa identificação na comparação: não apresentar a curva positiva do PMOS como uma corrente de dreno com a mesma convenção de sinal do NMOS.

**O que observar:** aumentar VSG aumenta a condução do PMOS, assim como aumentar VGS aumenta a condução do NMOS. Comparar a forma das curvas considerando os terminais medidos e as polaridades. Não exigir correntes idênticas dos dois dispositivos apenas por terem o mesmo W e L.

## Aula 2 — Portas CMOS

A desenvolver: inversor, interpretação das redes pull-up e pull-down, curva de transferência DC e resposta temporal; depois NAND e NOR com todas as combinações de entrada.

## Aula 3 — Do schematic ao layout

A desenvolver em uma célula de inversor com um NMOS e um PMOS: identificação das camadas e conexões, DRC, LVS e comparação com o circuito extraído. Registrar a ferramenta de extração e a vista produzida quando o fluxo local for confirmado. A abertura do layout, isoladamente, não constitui uma simulação após extração.
