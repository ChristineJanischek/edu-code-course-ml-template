from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

pfad = Path('notebooks/daten/lernergebnisse.csv')
if not pfad.exists(): pfad = Path('daten/lernergebnisse.csv')
df = pd.read_csv(pfad)
summary = df.groupby('thema').agg(anzahl=('punkte','size'), mittelwert=('punkte','mean'), median=('punkte','median'))
print(summary)
# TODO: eine Detail- und eine Managementgrafik mit Aussage und Grenze erzeugen.
