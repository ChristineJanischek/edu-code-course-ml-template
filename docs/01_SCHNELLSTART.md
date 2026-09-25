# Schnellstart – ohne KI und zunächst auch ohne GitHub

**Voraussetzungen:** Python 3 mit `venv`, Zugriff auf die Python-Pakete für die einmalige Installation, ein Browser und Schreibrechte in deinem Arbeitsordner. Git brauchst du erst beim späteren Veröffentlichen; das Projekt selbst kann lokal entpackt starten. Auf Schulgeräten kann die Lehrkraft/IT die Pakete vorinstallieren oder eine schulinterne Paketquelle bereitstellen.

## 1. Projekt holen

- Ohne Konto: die Repository-ZIP entpacken und in den Ordner `ML_R8_GitHub_Template` wechseln.
- Mit Konto: auf der Vorlagenseite **Use this template → Create a new repository** wählen; anschließend die eigene Repository-Adresse kopieren und `git clone ADRESSE` ausführen.
- In beiden Fällen: alle folgenden Befehle im **Projekt-Hauptordner** ausführen. Dort müssen `requirements.txt` und die Ordner `notebooks`, `programme`, `aufgaben` sichtbar sein.

## 2. Einmalig auf Windows einrichten (Eingabeaufforderung oder PowerShell)

```text
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe tests\vorabcheck.py
```

Der erste Befehl erstellt eine getrennte Python-Umgebung, der zweite installiert Pakete **in diese Umgebung**, der dritte prüft Pakete, Beispieldaten und Notebooks. Falls `py` nicht vorhanden ist, kann `python -m venv .venv` funktionieren. Die Installation benötigt einmalig Internet oder eine von der Schule vorbereitete Paketquelle.

## 3. Jupyter starten

```text
.venv\Scripts\jupyter-lab.exe
```

Im Browser `notebooks/08_grosse_daten_visualisieren.ipynb` öffnen. Die Zellen von oben nach unten mit **Shift+Enter** ausführen. Eine Codezelle erst verändern, wenn du ihre Ein- und Ausgaben beschreiben kannst. Das Fenster der Konsole während der Arbeit geöffnet lassen. Mit **Strg+C** dort Jupyter beenden.

## Alternative mit Python-Dateien

In Thonny die Datei `programme/08_grosse_daten_visualisieren.py` öffnen. Python-Pakete müssen auch dort im verwendeten Interpreter vorhanden sein. Wird Thonnys eigene Python-Umgebung verwendet, prüft die Lehrkraft, wie die Pakete dort installiert werden. Der fachliche Auftrag ist derselbe.

## Mac oder Linux

Im Projektordner: `python3 -m venv .venv`, danach `.venv/bin/python -m pip install -r requirements.txt`, `.venv/bin/python tests/vorabcheck.py` und `.venv/bin/jupyter lab`.

## Was du abgibst

Die Aufgabe steht in `aufgaben/ML-K10-A01.md`. Eigene Notebooks, Grafiken und eine kurze Deutung im Ordner `abgaben/ML-K10-A01/` speichern. Nur synthetische Daten verwenden. Die Befehle zum Speichern bei GitHub erklärt der [Konsolen-Anhang](02_KONSOLE_UND_GITHUB.md).
