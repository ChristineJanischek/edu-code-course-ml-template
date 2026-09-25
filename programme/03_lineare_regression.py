from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

pfad = Path('notebooks/daten/haeuser.csv')
if not pfad.exists(): pfad = Path('daten/haeuser.csv')
df = pd.read_csv(pfad)
X = df[['groesse_m2']]
y = df['preis_euro']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modell = LinearRegression()
# TODO: trainieren, vorhersagen und MAE ausgeben.
print('Trainingsfaelle:', len(X_train), 'Testfaelle:', len(X_test))
