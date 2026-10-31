# Micrografias selecionadas para a sequência de ampliação

## Estado desta edição

As fotografias de encapsulamento e sonda da apresentação sobre Titan foram retiradas. **Os dois novos arquivos de micrografia ainda não foram obtidos**: o download falhou por resolução de nomes no ambiente de execução. Os slides correspondentes só entram no PDF quando os arquivos científicos estiverem disponíveis localmente; não são usados desenhos sintéticos como substitutos de micrografias reais.

## Circuito integrado e interconexões

- Autoria: **NISE Network / Lawrence Hall of Science**.
- Recurso: [Zoom into a Microchip](https://www.nisenet.org/catalog/media/zoom_microchip_video), criado em 2013.
- Imagem estática identificada no recurso: `2000x.jpg`; destino no projeto: `slides/assets/microscopia/vlsi_nise.jpg`.
- Licença informada na página do recurso: [CC BY-NC-SA 3.0 US](https://creativecommons.org/licenses/by-nc-sa/3.0/us/). A atribuição e o link acompanham a imagem.
- O recurso original transita de câmera digital para microscopia eletrônica de varredura. Trata de um chip mais antigo; não será apresentado como um processo moderno de 2 nm. O processo específico da amostra não foi identificado.

## Transistores nanométricos

- Autoria: **imec**, artigo de Lynn Verschueren e Geert Hellings.
- Fonte: [Outer wall forksheet: bridging nanosheet and CFET](https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology), 11/06/2025.
- Figura 1: **TEM image of GAA nanosheet devices**.
- Destino no projeto: `slides/assets/microscopia/gaa_imec.jpg`.
- Direitos do titular. Figura científica identificada e creditada para o contexto didático; sem atribuição de uma licença aberta inexistente.

As amostras das duas fontes são diferentes. A sequência compara escalas e níveis de organização; não simula um zoom contínuo no mesmo chip. As imagens devem ser inspecionadas após a obtenção para preservar as barras de escala e conferir legibilidade, sem inventar dimensões para elementos não identificados.

## Obtenção e inclusão

As URLs exatas e os créditos estão em `micrografias_fontes.json`. O script de obtenção usa os bytes originais, verifica o formato JPEG e registra um SHA-256 dos arquivos recebidos:

```bash
python3 scripts/obter_micrografias.py
bash compilar.sh
python3 empacotar.py
```

No Windows, os mesmos arquivos são usados por `compilar.ps1`. A compilação continua funcionando sem internet, mas só inclui as micrografias que estiverem presentes. Os PDFs e ZIPs atuais não contêm esses dois arquivos pendentes.
