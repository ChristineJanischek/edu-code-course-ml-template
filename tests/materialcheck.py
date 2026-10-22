from pathlib import Path
import ast,json,csv,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
expected={f"ML-K{n:02d}-{k}01.md" for n in range(1,23) for k in ("A","V")}
assert {p.name for p in (ROOT/"aufgaben").glob("*.md")}==expected
for p in (ROOT/"programme").glob("*.py"): ast.parse(p.read_text())
for p in (ROOT/"notebooks").glob("*.ipynb"):
 d=json.loads(p.read_text()); assert d["nbformat"]==4
 for c in d["cells"]:
  if c["cell_type"]=="code":ast.parse("".join(c["source"]))
for p in (ROOT/"notebooks/daten").glob("*.csv"):
 with p.open(newline="") as h:assert list(csv.DictReader(h))
for p in [ROOT/"README.md",*(ROOT/"docs").glob("*.md")]:
 for target in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)",p.read_text()):
  if not target.startswith(("http:","https:")):assert (p.parent/target).exists(),(p,target)
manifest=json.loads((ROOT/'materialstand.json').read_text(encoding='utf-8'))
assert len(manifest['files'])==48, '44 Aufgaben und 4 PDFs erforderlich'
assert {r['path'] for r in manifest['files'] if r['path'].startswith('aufgaben/')}=={'aufgaben/'+name for name in expected}
for row in manifest['files']:
 p=ROOT/row['path']
 assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'], ('Materialstand weicht ab',row['path'])
assert 'Datensteckbrief' in (ROOT/'aufgaben/ML-K13-A01.md').read_text(encoding='utf-8')
assert 'Abschlussprojekt Lernagent' not in (ROOT/'aufgaben/ML-K13-A01.md').read_text(encoding='utf-8')
assert not any(re.search(r'loesung|erwartungshorizont|punkteschluessel|musterklassenarbeit',p.name,re.I) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts)
print("Materialcheck bestanden: 44 Aufträge, Python-/Notebook-Syntax, CSV, relative Anleitungslinks, 48 kanonische Hashes und Rollentrennung")
