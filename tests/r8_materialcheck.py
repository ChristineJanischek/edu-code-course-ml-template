"""Check R8 material links and chapter files without producing solutions."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
tasks=sorted((ROOT/'aufgaben').glob('ML-K??-A01.md'))
assert len(tasks)==22, f'Expected 22 tasks, found {len(tasks)}'
for n,path in enumerate(tasks,1):
    assert path.name==f'ML-K{n:02d}-A01.md'
    content=path.read_text(encoding='utf-8')
    assert re.search(rf'Kapitel {n}\.1 und {n}\.2',content)
    assert len(content)>300
for module in ('Grundlagen_BKWI1','Vertiefung_BKWI2'):
    for size in ('A4_Desktop','A5_Mobil'):
        stem=f'ML_R8_{module}_{size}_Prueffassung'
        for ext in ('docx','pdf'): assert (ROOT/'lernskripte'/f'{stem}.{ext}').is_file()
for doc in ('01_SCHNELLSTART','03_BKWI2_WOCHE_1_2','05_DIGITALE_SCHULTASCHE_OFFLINE','06_R8_KAPITELZUORDNUNG'):
    text=(ROOT/'docs'/f'{doc}.md').read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)#]+)(?:#[^)]+)?\)',text):
        if not target.startswith(('http:','https:')):assert (ROOT/'docs'/target).exists(),target
print('R8-MATERIALCHECK BESTANDEN: 22 Aufgaben und acht Skriptdateien')
