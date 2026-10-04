# Schnellstart

## Eigene GitHub Kopie

Öffne das Repository und wähle **Use this template → Create a new repository**. Benenne deine Arbeitskopie. Arbeite in deiner eigenen Kopie; GitHub Classroom und ein KI-Assistent sind nicht erforderlich.

In der eigenen Kopie: **Code → Codespaces → Create codespace on main**. Warte, bis die Einrichtung abgeschlossen ist. Öffne ein Terminal und führe `python tests/vorabcheck.py` und `python tests/materialcheck.py` aus. Wähle bei Notebooks den Kernel **Python (.venv)**. Codespaces benötigt ein Konto und kann dem Kontingent des Kontos unterliegen.

## Lokal ohne GitHub

Entpacke das Unterrichtspaket. Öffne `02_Offlineprojekt` in Thonny oder VS Code. Python mit pandas, matplotlib und scikit-learn muss verfügbar sein. Mit Internet kann die Lehrkraft die Pakete über `python -m pip install -r requirements.txt` vorbereiten; eine solche Installation ist noch kein Offline-Nachweis. Jupyter ist optional und wird über `requirements-notebook.txt` ergänzt.

Führe im Projektordner `python tests/vorabcheck.py`, `python tests/offline_python_check.py` und `python tests/smoke_test.py` aus. Im Repository zusätzlich `python tests/materialcheck.py`. Öffne anschließend den passenden [Grundlagenweg](GRUNDLAGEN.md) oder [Vertiefungsweg](VERTIEFUNG.md). Alle Pflichtaufträge verwenden lokale Materialien. Behalte die Originaldaten und speichere deine Bearbeitung in `abgaben/ML-Kxx-A01/` oder `abgaben/ML-Kxx-V01/`.

## Datenfehler erkennen

`haeuser.csv` und `haeuser_80.csv` enthalten in H009 absichtlich einen ungültigen Preis. `lerndaten_fehlerhaft.csv` ist eine Fehlerübung. Bearbeite eine Kopie und begründe jede Änderung; erfinde keine Ersatzwerte. Die Starter enthalten keine fertigen Aufgabenlösungen.
