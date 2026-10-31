#!/usr/bin/env python3
"""Obtém os arquivos científicos identificados, preservando os bytes da fonte."""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'dados/micrografias_fontes.json').read_text(encoding='utf-8'))
folder=ROOT/'slides/assets/microscopia'
folder.mkdir(parents=True,exist_ok=True)
failed=[]; provenance=[]
for item in manifest['imagens']:
    target=folder/item['arquivo']
    try:
        if not target.exists():
            req=Request(item['url'],headers={'User-Agent':'Mozilla/5.0'})
            with urlopen(req,timeout=30) as response:raw=response.read()
            if not raw.startswith(b'\xff\xd8') or len(raw)<1024:
                raise ValueError('O servidor não retornou uma imagem JPEG válida.')
            target.write_bytes(raw)
        raw=target.read_bytes()
        provenance.append({'arquivo':item['arquivo'],'url':item['url'],'sha256':hashlib.sha256(raw).hexdigest()})
        print(f'OK: {target.name}')
    except Exception as error:
        failed.append(item['arquivo'])
        print(f'Falha ao obter {item["arquivo"]}: {error}',file=sys.stderr)
if provenance:
    (ROOT/'dados/micrografias_obtidas.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sys.exit(bool(failed))
