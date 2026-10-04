from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

pfad = Path(__file__).resolve().parents[1] / 'notebooks' / 'daten' / 'lerndaten_lernagent.csv'
df = pd.read_csv(pfad)
X = df[['versuche','hilfen','bearbeitungszeit_min','punkte']]
# TODO: skalieren, drei Cluster bilden und vorsichtig beschreiben.
print(X.describe())
