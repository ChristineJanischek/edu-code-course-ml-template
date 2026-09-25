# Fehlerhilfe ohne KI-Assistent

| Beobachtung | Prüfen und beheben |
| --- | --- |
| `py` wird nicht erkannt | Python ist noch nicht installiert oder der Launcher fehlt. Die Lehrkraft/IT prüft die Python-Installation. Alternativ `python -m venv .venv` testen. |
| `git` wird nicht erkannt | Git ist noch nicht installiert. Lokal ohne GitHub arbeiten; Installation mit der Schule abstimmen. |
| `No module named pandas` oder `matplotlib` | Wahrscheinlich wurde eine andere Python-Umgebung verwendet. Vom Projektordner aus `.venv\Scripts\python.exe -m pip install -r requirements.txt` starten und denselben Interpreter für den Vorabcheck nutzen. |
| `jupyter-lab.exe` fehlt | Die Paketinstallation ist nicht abgeschlossen; `requirements.txt` enthält JupyterLab. Die Lehrkraft/IT prüft Netz- oder Paketquellenzugriff. |
| `FileNotFoundError` bei CSV | Der Projektordner muss vollständig entpackt sein. Im Notebook gibt es zwei Pfadvarianten, je nachdem, von welchem Ordner Jupyter gestartet wurde. `dir notebooks\daten` im Projektordner prüfen. |
| Jupyter zeigt einen anderen Ordner | Jupyter schließen und im Projekt-Hauptordner neu starten. |
| CSV-Zahlenspalte enthält `R8` | Das wäre ein Fehler eines alten Pakets. Der Vorabcheck dieser Vorlage erkennt ihn; die Lehrkraft soll die Vorlage erneut verteilen. Die Datei `lerndaten_fehlerhaft.csv` enthält darüber hinaus **absichtlich** Datenqualitätsfehler für eine andere Aufgabe. |
| `git push` fragt nach Anmeldung | Über das von Git bereitgestellte Browserfenster beim **eigenen** Konto anmelden. Kein Passwort oder Token in Aufgaben-, Notebook- oder Chatdateien kopieren. |

Vor jeder technischen Fehlersuche: in `dir` prüfen, ob du im richtigen Projektordner stehst; dann die genaue Fehlermeldung lesen und den letzten Befehl notieren. Keine fremden Befehle unbesehen ausführen.
