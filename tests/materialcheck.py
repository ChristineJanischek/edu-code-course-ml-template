from pathlib import Path
import ast,json,csv,re
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
print("Materialcheck bestanden: 44 Aufträge, Python-/Notebook-Syntax, CSV und relative Anleitungslinks")
