# Schnellstart – ohne KI

Du kannst mit GitHub Codespaces direkt in einer vorbereiteten Umgebung starten oder das Projekt lokal ohne GitHub-Konto verwenden. Keine der beiden Varianten benötigt Copilot.

## Weg A: GitHub Codespaces

Dieser Weg setzt ein GitHub-Konto voraus. Codespaces-Verfügbarkeit und Nutzungskontingente hängen vom Konto und den Schulregeln ab.

1. Auf der Vorlagenseite **Use this template → Create a new repository** wählen und das eigene Repository erstellen.
2. Im neuen Repository **Code → Codespaces → Create codespace on main** wählen.
3. Warten, bis die Einrichtung abgeschlossen ist. Python 3.12 und Git werden angezeigt und geprüft; `.venv` wird erstellt und auf Schreibbarkeit geprüft. Die Python- und Jupyter-Erweiterungen sowie die Pakete aus `requirements.txt` werden eingerichtet. Im Terminal muss `VORABCHECK BESTANDEN` erscheinen.
4. JupyterLab im Projekt-Hauptordner starten:

	```bash
	.venv/bin/jupyter lab --ip=0.0.0.0 --port=8888 --no-browser
	```

	Den weitergeleiteten Port **8888** in der Ports-Ansicht öffnen. Falls Jupyter nach einem Token fragt, den Token aus der Terminalausgabe verwenden.

5. `notebooks/08_grosse_daten_visualisieren.ipynb` öffnen und den Kernel **Python (.venv)** auswählen. Die vorhandene Zelle ausführen; sie lädt die synthetische CSV aus dem Projektordner. Die TODO-Stelle bleibt offen. Das erfolgreiche Öffnen und Ausführen im Browser prüft zugleich den Browserzugriff.

Wenn der Vorabcheck fehlschlägt, die vollständige Meldung notieren und die [Fehlerhilfe](04_FEHLERHILFE.md) verwenden. Ohne Internetzugriff auf die Paketquelle kann Codespaces die Pakete nicht automatisch installieren.

## Weg B: lokal ohne GitHub-Konto

### 1. Projekt holen

Die Repository-ZIP entpacken und in den Projektordner wechseln. Alle Befehle im **Projekt-Hauptordner** ausführen. Dort müssen `requirements.txt` und die Ordner `notebooks`, `programme`, `aufgaben` sichtbar sein.

### 2. Einmalig auf Windows einrichten (Eingabeaufforderung oder PowerShell)

```text
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m ipykernel install --sys-prefix --name ml-template --display-name "Python (.venv)"
.venv\Scripts\python.exe tests\vorabcheck.py
```

Der erste Befehl erstellt eine getrennte Python-Umgebung, der zweite installiert Pakete **in diese Umgebung**, der dritte registriert ihren Notebook-Kernel, der vierte prüft Pakete, Beispieldaten und Notebooks. Falls `py` nicht vorhanden ist, kann `python -m venv .venv` funktionieren. Die Installation benötigt einmalig Internet oder eine von der Schule vorbereitete Paketquelle. Bei einem lokalen Ordner mit bereitgestellten Paketdateien kann die IT-Anweisung zum Beispiel `-m pip install --no-index --find-links "PFAD_ZUM_PAKETORDNER" -r requirements.txt` vorgeben. Wenn Pakete bereits in einer Schul-Python-Umgebung installiert sind, vor dem Überspringen der Installation mit der Lehrkraft/IT klären, welcher Interpreter samt `ipykernel` verwendet werden soll.

### 3. Jupyter starten

```text
.venv\Scripts\jupyter-lab.exe
```

Im geöffneten Browser `notebooks/08_grosse_daten_visualisieren.ipynb` öffnen. Oben rechts den Kernel **Python (.venv)** auswählen und die Zellen von oben nach unten mit **Shift+Enter** ausführen. Eine Codezelle erst verändern, wenn du ihre Ein- und Ausgaben beschreiben kannst. Das Fenster der Konsole während der Arbeit geöffnet lassen. Mit **Strg+C** dort Jupyter beenden.

### Alternative mit Python-Dateien

In Thonny die Datei `programme/08_grosse_daten_visualisieren.py` öffnen. Python-Pakete müssen auch dort im verwendeten Interpreter vorhanden sein. Wird Thonnys eigene Python-Umgebung verwendet, prüft die Lehrkraft, wie die Pakete dort installiert werden. Der fachliche Auftrag ist derselbe.

### Mac oder Linux

Im Projektordner: `python3 -m venv .venv`, danach `.venv/bin/python -m pip install -r requirements.txt`, `.venv/bin/python -m ipykernel install --sys-prefix --name ml-template --display-name 'Python (.venv)'`, `.venv/bin/python tests/vorabcheck.py` und `.venv/bin/jupyter lab`. Im Notebook den Kernel **Python (.venv)** auswählen.

### Was du abgibst

Die Aufgabe steht in `aufgaben/ML-K10-A01.md`. Eigene Notebooks, Grafiken und eine kurze Deutung im Ordner `abgaben/ML-K10-A01/` speichern. Nur synthetische Daten verwenden. Die Befehle zum Speichern bei GitHub erklärt der [Konsolen-Anhang](02_KONSOLE_UND_GITHUB.md).

## Vor dem Unterricht: kurzer Pilotlauf

Eine Schülerin oder ein Schüler ohne Copilot sollte den Ablauf selbstständig testen:

1. Das Projekt und die Aufgabe `ML-K10-A01` finden.
2. Das Mini-Glossar in [BKWI2 · BPE 7](03_BKWI2_WOCHE_1_2.md) verwenden.
3. Notebook 08 öffnen, die vorhandene Zelle ausführen und prüfen, dass die CSV-Tabelle erscheint. Die TODO-Stelle nicht bearbeiten.
4. Ein eigenes Ergebnis lokal unter `abgaben/ML-K10-A01/` speichern.
5. Bei einem Fehler die genaue Meldung und den zuletzt ausgeführten Schritt notieren und der Lehrkraft melden.

GitHub-Veröffentlichung kann anschließend folgen; für den lokalen ZIP-Weg sind GitHub-Konto und Git nicht erforderlich.
