"""Technische Eingangskontrolle des ML-Repositorys, ohne Aufgaben zu lösen."""
from pathlib import Path
import csv
import importlib
import json
import sys

root = Path(__file__).resolve().parents[1]
errors = []
for module in ("pandas", "matplotlib", "sklearn", "jupyterlab"):
    try:
        importlib.import_module(module)
    except ImportError:
        errors.append(f"Paket fehlt: {module}")
for notebook in sorted((root / "notebooks").glob("*.ipynb")):
    try:
        data = json.loads(notebook.read_text(encoding="utf-8"))
        if data.get("nbformat") != 4 or not data.get("cells"):
            errors.append(f"Notebook unvollständig: {notebook.name}")
    except (ValueError, OSError) as exc:
        errors.append(f"Notebook nicht lesbar: {notebook.name}: {exc}")
for name in ("lernergebnisse.csv", "lerndaten_lernagent.csv"):
    path = root / "notebooks" / "daten" / name
    try:
        with path.open(encoding="utf-8-sig", newline="") as file:
            rows = list(csv.DictReader(file))
        if not rows:
            errors.append(f"Keine Daten: {name}")
        for index, row in enumerate(rows, start=2):
            try:
                float(row["loesungsquote"])
            except (ValueError, KeyError, TypeError):
                errors.append(f"Numerische Lösungsquote beschädigt: {name}, Zeile {index}")
    except OSError as exc:
        errors.append(f"CSV nicht lesbar: {name}: {exc}")
if errors:
    print("VORABCHECK FEHLGESCHLAGEN")
    for error in errors:
        print("-", error)
    sys.exit(1)
print("VORABCHECK BESTANDEN: Pakete, Notebooks und CSV-Daten geprüft")
