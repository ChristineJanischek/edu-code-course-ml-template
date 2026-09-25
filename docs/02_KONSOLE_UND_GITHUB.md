# Anhang – Konsole, Git und GitHub Schritt für Schritt

**Konsole:** Ein Textfenster für Befehle. Unter Windows gehen Eingabeaufforderung (CMD) und PowerShell. Eine Zeile eingeben, mit Enter ausführen, die Rückmeldung lesen. Die Beispiele stehen in einem persönlichen Projektordner, nicht im Systemordner. `ADRESSE` und `DEIN-PFAD` sind Platzhalter; sie werden nicht wörtlich eingegeben.

| Befehl | Zweck | Woran du Erfolg erkennst |
| --- | --- | --- |
| `pwd` (PowerShell), `cd` (CMD) | aktuellen Ordner anzeigen | Der Projektordner ist erkennbar. |
| `dir` | Dateien im aktuellen Ordner anzeigen | `requirements.txt` und `notebooks` sind sichtbar. |
| `cd DEIN-PFAD` | in einen bestimmten Ordner wechseln | `dir` zeigt anschließend die Projekteinträge. Bei Leerzeichen den Pfad in Anführungszeichen setzen. |
| `cd ..` | eine Ordnerebene zurück | der angezeigte Pfad wird kürzer. |
| `py -3 -m venv .venv` | eigene Python-Umgebung erstellen | der Ordner `.venv` entsteht. |
| `.venv\Scripts\python.exe -m pip install -r requirements.txt` | Projektpakete in der Projektumgebung installieren | am Ende keine Fehlermeldung. Internet oder eine schulische Paketquelle ist dafür nötig. |
| `.venv\Scripts\python.exe tests\vorabcheck.py` | Voraussetzungen und CSV-Daten prüfen | die Meldung `VORABCHECK BESTANDEN` erscheint. |
| `.venv\Scripts\jupyter-lab.exe` | Notebook-Oberfläche im Browser starten | der Browser zeigt JupyterLab. Die Konsole geöffnet lassen. |

`git` verwaltet Dateistände auf deinem Computer. **GitHub** speichert ein Repository online; zum lokalen Bearbeiten ist es nicht nötig. Erst wenn ihr gemeinsam die Konten eingerichtet habt:

| Befehl | Zweck |
| --- | --- |
| `git --version` | prüfen, ob Git installiert ist. |
| `git clone ADRESSE` | das **eigene** auf GitHub aus der Vorlage erzeugte Repository herunterladen. |
| `git status` | sehen, welche Dateien geändert wurden und was vorgemerkt ist. |
| `git add abgaben/ML-K10-A01` | nur die eigene Abgabe für den nächsten Speicherstand vormerken. |
| `git commit -m "ML-K10-A01 bearbeitet"` | den vorgemerkten Stand lokal mit einer verständlichen Nachricht speichern. |
| `git push` | den gespeicherten Stand ins **eigene** GitHub-Repository übertragen; Anmeldung gegebenenfalls im Browser abschließen. |
| `git pull` | Änderungen aus dem eigenen Online-Repository vor der Weiterarbeit holen. |

**Arbeitsfolge:** zuerst `git status`, dann gezielt `git add`, nochmals `git status`, dann `git commit`, schließlich `git push`. Auf GitHub prüfen, ob die Abgabe im eigenen Repository sichtbar ist. Niemals Kennwörter, Zugangstoken oder echte Leistungsdaten in Dateien oder Chatnachrichten eintragen. Wenn die Anmeldung noch fehlt, lokal weiterarbeiten und später übertragen.

**Begriffshilfe:** Repository = Projektordner mit Versionsgeschichte; Template = Vorlage für eine eigenständige Kopie; Commit = gespeicherter lokaler Dateistand; Push = lokaler Stand nach GitHub; Pull = Änderungen von GitHub zum Computer; Notebook = Dokument aus Text- und ausführbaren Codezellen; Kernel = Python-Prozess, der Notebook-Zellen ausführt.

Quellen für die Bedienung: [GitHub: Vorlage erstellen](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository), [Repository aus Vorlage erzeugen](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template), [Python-Umgebungen](https://docs.python.org/3/tutorial/venv.html), [Jupyter-Installation](https://jupyter.org/install).
