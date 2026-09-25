from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

pfad = Path('notebooks/daten/lernergebnisse.csv')
if not pfad.exists(): pfad = Path('daten/lernergebnisse.csv')
df = pd.read_csv(pfad)
X = df[['loesungsquote','versuche','bearbeitungszeit_min']]
y = df['empfehlung']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42, stratify=y)
# TODO: Baseline und Baum vergleichen; Fehlerfaelle deuten.
print('Klassen:', sorted(y.unique()))
