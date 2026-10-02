# Lokal arbeiten, auch ohne Jupyter

Die konkrete Ausstattung des Informatik-Sticks wird im Unterricht geprüft. Gehe zunächst davon aus, dass VS Code und Python verfügbar sind; ob Jupyter und alle Pakete im verwendeten Python-Interpreter installiert sind, zeigt erst der Test am Gerät.

1. Repository-ZIP herunterladen und lokal entpacken. Den Ordner in VS Code öffnen.
2. Im Terminal des Projekt-Hauptordners `python tests/offline_python_check.py` ausführen. Auf Windows kann `py -3 tests\offline_python_check.py` nötig sein. Der Check prüft Python-Pakete und CSV, ohne Jupyter vorauszusetzen.
3. Wenn der Check besteht: `python programme/02_daten_erkunden.py` ausführen. Erst die CSV-Kopfzeile und dann die Programmausgabe mit dem Informationsblatt vergleichen.
4. Die Word-Arbeitsvorlage lässt sich auch ohne Programmlauf ausfüllen. Eigene Dateien unter `abgaben/ML-Kxx-A01/` speichern.

Wenn `ModuleNotFoundError` erscheint, den Namen des fehlenden Pakets und den verwendeten Python-Interpreter notieren. Die Lehrkraft/IT kann vorhandene Schul-Pakete zuordnen. Eine Netzwerk- oder Jupyter-Installation ist für den ersten fachlichen Schritt nicht erforderlich.
