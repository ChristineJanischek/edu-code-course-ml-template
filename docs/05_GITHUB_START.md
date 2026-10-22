# Ferienstart: eigene Kopie, Codespaces oder lokal

## 1. Vorlage und Lernweg wählen

Öffne [das öffentliche ML-Template](https://github.com/ChristineJanischek/edu-code-course-ml-template). Wähle **Use this template → Create a new repository**, dein eigenes Konto und einen Namen. Du kannst deine Kopie privat anlegen. Du benötigst kein GitHub Classroom und keinen KI-Assistenten.

Öffne [Grundlagen Kapitel 1–12](GRUNDLAGEN.md) oder [Vertiefung Kapitel 13–22](VERTIEFUNG.md). Die vollständigen A4-/A5-Lernskripte liegen unter `01_Skript` in deiner Kopie. Kapitel 13 ist Datenerkundung. Der gesonderte Projektteil 23–28 ist nicht enthalten.

## 2. Im Browser starten

In deiner Kopie **Code → Codespaces → Create codespace on main** wählen. Einrichtung abwarten. Im Menü **Terminal → New Terminal** öffnen. Im Terminal die folgenden Zeilen einzeln eingeben:

```bash
.venv/bin/python tests/vorabcheck.py --notebook
.venv/bin/python tests/materialcheck.py
.venv/bin/python tests/smoke_test.py
```

Erwartet werden `VORABCHECK BESTANDEN`, `Materialcheck bestanden` und am Ende `SMOKE TEST BESTANDEN`. Die Ausgabe prüft den technischen Start; die TODO-Aufgaben bleiben deine Arbeit. Für Notebooks oben rechts **Select Kernel → Python Environments → Python (.venv)** wählen. Falls der Name abweicht, den Interpreter `.venv/bin/python` auswählen. Codespaces benötigt Internet und kann dem Kontingent deines Kontos unterliegen.

## 3. Lokal und offline arbeiten

**Code → Download ZIP**, vollständig entpacken, Projektordner in VS Code oder Thonny öffnen. Im Repo liegen `programme`, `notebooks` und `tests` direkt im Hauptordner; im Unterrichtspaket öffnest du dafür `02_Offlineprojekt`.

Vor den Ferien mit Internet eine eigene Umgebung vorbereiten. Windows:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe tests\vorabcheck.py
.venv\Scripts\python.exe tests\offline_python_check.py
.venv\Scripts\python.exe tests\smoke_test.py
```

macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python tests/vorabcheck.py
.venv/bin/python tests/offline_python_check.py
.venv/bin/python tests/smoke_test.py
```

Jupyter ist optional. Nur für Notebooks zusätzlich mit demselben Python `-m pip install -r requirements-notebook.txt` ausführen. Danach mit `-m jupyterlab` starten. Für normale Python-Dateien ist das nicht nötig. In VS Code/Thonny ebenfalls den Interpreter der `.venv` auswählen.

Wenn die drei Tests bestehen: Internetverbindung trennen und `tests/offline_python_check.py` sowie dein gewähltes Programm nochmals mit demselben Interpreter starten. Öffne auch dein PDF lokal. Erst dieser Lauf zeigt dir, dass dein eigener Rechner vorbereitet ist. Die erste Paketinstallation benötigt Internet; das heruntergeladene Projekt allein installiert kein Python. Wenn Pakete fehlen, [Fehlerhilfe](04_FEHLERHILFE.md) nutzen. Die Papieralternativen stehen im Skript.

## 4. Ergebnisse sichern

Speichere deine Dateien unter `abgaben/ML-Kxx-A01/` beziehungsweise `abgaben/ML-Kxx-V01/`. Originaldaten nicht überschreiben. Speichern mit Strg+S und anschließend über **Source Control** gezielt deine Abgabedateien vormerken, mit einer Nachricht committen und pushen. Alternativ die Befehle in [Konsole und Git](02_KONSOLE_UND_GITHUB.md) verwenden. Kontrolliere danach auf GitHub in deiner Kopie, ob die Dateien sichtbar sind. Vor dem Beenden eines Codespace immer sichern und pushen.

## Wenn du schon eine ältere Kopie hast

Ein Template ist eine unabhängige Kopie. `git pull` holt nur Änderungen aus deinem eigenen Repository und aktualisiert nicht automatisch die Vorlage. Sichere deine Abgaben zuerst. Lade die aktuelle Vorlage als ZIP in einen neuen Ordner und übernimm anschließend ausschließlich deine eigenen Abgaben. Überschreibe deine bisherige Arbeit nicht. Vergleiche Kapitel 13 mit dem aktuellen Skript, falls deine Kopie dort noch ein Abschlussprojekt zeigt.
