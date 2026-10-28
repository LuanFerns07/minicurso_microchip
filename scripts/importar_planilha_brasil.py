#!/usr/bin/env python3
"""Extrai apenas o índice necessário ao mapa; não copia a planilha de referência."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def read_sheet(z, name, strings):
    for row in ET.fromstring(z.read(name)).findall('.//s:sheetData/s:row', NS):
        result = {}
        for cell in row.findall('s:c', NS):
            v, inline = cell.find('s:v', NS), cell.find('s:is', NS)
            value = v.text if v is not None else ''.join(inline.itertext()) if inline is not None else ''
            if cell.get('t') == 's' and value:
                value = strings[int(value)]
            if value:
                result[''.join(c for c in cell.get('r') if c.isalpha())] = value.strip()
        if result:
            yield result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('planilha', type=Path)
    args = parser.parse_args()
    out = Path(__file__).resolve().parents[1] / 'dados'
    out.mkdir(exist_ok=True)
    with ZipFile(args.planilha) as z:
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(e.itertext()) for e in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        organizations = []
        for row in read_sheet(z, 'xl/worksheets/sheet1.xml', strings):
            if row.get('B') and row.get('A', '').replace('.', '', 1).isdigit():
                organizations.append({'id': int(float(row['A'])), 'organizacao': row['B'], 'tipo': row.get('D', ''), 'atuacao': row.get('C', ''), 'fonte': row.get('E', '')})
        names = {r['organizacao'] for r in organizations}
        memberships, cluster = [], None
        for row in read_sheet(z, 'xl/worksheets/sheet2.xml', strings):
            if row.get('A') and not row.get('B'):
                cluster = row['A']
            elif row.get('B') in names:
                assert cluster, row
                memberships.append({'polo': cluster, 'organizacao': row['B']})
    assert len(names) == len(organizations)
    assert {m['organizacao'] for m in memberships} == names
    for filename, rows in [('organizacoes_brasil.csv', organizations), ('presencas_brasil.csv', memberships)]:
        with (out / filename).open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    metadata = {'projeto': 'Brazil Silicon Roadmap', 'autor_creditado': 'Matheus Grossi',
                'repositorio': 'https://github.com/MattGrossi12/brazil_silicon_roadmap',
                'arquivo_fonte': args.planilha.name, 'consulta': '2026-10-28',
                'sha256_planilha': hashlib.sha256(args.planilha.read_bytes()).hexdigest(),
                'organizacoes': len(organizations), 'presencas_por_polo': len(memberships),
                'polos': len({m['polo'] for m in memberships}),
                'nota': 'Categorias e incertezas de atuação preservadas da planilha; polos agregados não são endereços individuais.'}
    (out / 'origem_brasil.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+'\n')
    print(f"{metadata['organizacoes']} organizações, {metadata['presencas_por_polo']} presenças e {metadata['polos']} polos.")

if __name__ == '__main__':
    main()
