from pathlib import Path
import pandas as pd

pfad = Path(__file__).resolve().parents[1] / 'notebooks' / 'daten' / 'lerndaten_lernagent.csv'
daten = pd.read_csv(pfad)
print(daten.head())
print(daten.shape)
# TODO: Datentypen, fehlende Werte und Wertebereiche pruefen.
