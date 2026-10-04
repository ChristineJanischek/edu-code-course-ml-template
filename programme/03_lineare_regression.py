from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

pfad = Path(__file__).resolve().parents[1] / 'notebooks' / 'daten' / 'haeuser.csv'
quelle = pd.read_csv(pfad)
# Arbeitskopie: unlesbare Preise dokumentieren, niemals raten oder Quelle überschreiben.
df = quelle.copy()
df['preis_euro'] = pd.to_numeric(df['preis_euro'], errors='coerce')
print('Ausgeschlossene Arbeitskopie-Faelle:', df.loc[df['preis_euro'].isna(), 'objekt_id'].tolist())
df = df.dropna(subset=['groesse_m2', 'preis_euro']).copy()
X = df[['groesse_m2']]
y = df['preis_euro']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modell = LinearRegression()
# TODO: trainieren, vorhersagen und MAE ausgeben.
print('Trainingsfaelle:', len(X_train), 'Testfaelle:', len(X_test))
