from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

pfad = Path('notebooks/daten/lerndaten_lernagent.csv')
if not pfad.exists(): pfad = Path('daten/lerndaten_lernagent.csv')
df = pd.read_csv(pfad)
X = df[['loesungsquote','versuche','bearbeitungszeit_min']]
y = df['empfehlung']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=42, stratify=y)
# TODO: beide Modelle trainieren und fair vergleichen.
print(y.value_counts())
