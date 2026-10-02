"""Minimal Python/CSV check when the notebook kernel is unavailable."""
from pathlib import Path
import csv
import pandas
import matplotlib
import sklearn

ROOT=Path(__file__).resolve().parents[1]
for name in ('lerndaten_lernagent.csv','lernergebnisse.csv'):
    path=ROOT/'notebooks/daten'/name
    with path.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames and next(reader,None),name
print('OFFLINE-PYTHON-CHECK BESTANDEN; Jupyter nicht erforderlich')
