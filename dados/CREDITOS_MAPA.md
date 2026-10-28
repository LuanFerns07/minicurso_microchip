# Âmbito Brasil — origem dos dados e do desenho

- Levantamento: **Matheus Grossi, Brazil Silicon Roadmap**,
  <https://github.com/MattGrossi12/brazil_silicon_roadmap>.
- Base desta edição: planilha `road_map_table_PT-BR.xlsx`, fornecida pelo usuário
  em 28/10/2026. Ela contém 54 organizações e 73 associações a 13 polos.
  Os números se referem a essa planilha, não ao resumo de outra versão do site.
- Os CSVs são o índice derivado usado na apresentação; a planilha original não
  integra o repositório. A classificação e as incertezas da atuação ficam preservadas.
- “Empresa” e “centro/grupo de pesquisa” são distinguidos; constar do levantamento
  não significa que a organização projete circuitos integrados no Brasil.
- Contorno geográfico simplificado:
  <https://github.com/johan/world.geo.json/blob/master/countries/BRA.geo.json>.
  O mapa foi redesenhado em TikZ; não usa a fotografia nem a composição visual do roadmap.
- Marcadores indicam polos da planilha, de forma esquemática, e não endereços.
  Polos definidos como “interior” são tratados como áreas agregadas.
- Desenho e composição didática: Luan F. Nogueira e Luiz F. de Melo Soares.

Para atualizar a extração, execute:

```bash
python3 scripts/importar_planilha_brasil.py /caminho/road_map_table_PT-BR.xlsx
python3 scripts/gerar_brasil.py
```
