from pathlib import Path
import pandas as pd

pfad = Path('notebooks/daten/lernergebnisse.csv')
if not pfad.exists(): pfad = Path('daten/lernergebnisse.csv')
df = pd.read_csv(pfad)
print(df.head())
# TODO: Problem, Features, Ziel, Baseline, Modell, Kennzahl und Abbruchregel umsetzen.
