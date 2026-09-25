# BKWI2 · BPE 7.1 · vorhandener Auftrag für Wochen 1–2

**Woche 1:** Auswertung großer Datenmengen, geeignete Grafik, sinnvolle Verdichtung und Deutung. **Woche 2:** die bereits eingesetzte Python-Bibliothek in Notebook und Code nachvollziehen. Die fachliche Aufgabenstellung `ML-K10-A01` bleibt in `aufgaben/ML-K10-A01.md` und im Lernskript unverändert; diese Seite erklärt nur den Arbeitsweg ohne KI-Hilfe.

1. Vorabcheck ausführen und `notebooks/08_grosse_daten_visualisieren.ipynb` öffnen. Die Daten liegen in `notebooks/daten/lernergebnisse.csv` (synthetisch).
2. Die vorhandene Zelle zunächst unverändert starten. Notiere: Welche Datei wird geladen? Wofür stehen `thema`, `punkte`, `size`, `mean`, `median`? Was zeigt die gedruckte Tabelle nicht?
3. Lies im Skript die vorhandenen Abschnitte „Vom Auftrag zur Grafik“, „Aggregieren, ohne Wichtiges zu verstecken“ und „View zuerst: Dashboard des Lernagenten“. Leite daraus die zwei im Originalauftrag geforderten Ansichten ab.
4. Arbeite die TODO-Stelle selbst ab. Nutze als Nachschlagehilfe den Abschnitt „Mini-Glossar für das Notebook“ unten und den fachlichen Denkimpuls des Originalskripts: **Frage → Kennzahl → Gruppierung → Diagramm → Aussage → Grenze.**
5. Speichere das Ergebnis in `abgaben/ML-K10-A01/`. Die vorhandene Aufgabe verlangt pro Ansicht Frage, Grafik, Aussage, Grenze und Handlungsempfehlung. Prüfe zusätzlich einen Fehler- oder Grenzfall und erkläre ihn in eigenen Worten.

## Mini-Glossar für das Notebook

| Vorhandener Ausdruck | Bedeutung in diesem Projekt |
| --- | --- |
| `from pathlib import Path` | Werkzeug für Dateipfade, unabhängig von einzelnen Schrägstrich-Konventionen. |
| `Path('notebooks/daten/lernergebnisse.csv')` | relativer Pfad aus dem Projekt-Hauptordner. Wenn das Notebook aus `notebooks/` gestartet wird, greift der vorhandene Ersatzpfad `daten/lernergebnisse.csv`. |
| `pd.read_csv(pfad)` | CSV-Daten in eine Tabelle (`DataFrame`) einlesen. |
| `df.groupby('thema')` | Zeilen nach Thema gruppieren. |
| `.agg(anzahl=('punkte','size'), mittelwert=('punkte','mean'), median=('punkte','median'))` | pro Thema Anzahl, arithmetisches Mittel und Median der Punkte ermitteln. |
| `print(summary)` | die Gruppenergebnisse als Text ausgeben. |
| `import matplotlib.pyplot as plt` | Grafikwerkzeug importieren; das Notebook enthält noch keinen fertigen Diagrammcode. |

## Syntaxhilfe für eigene Grafiken (Beispieldaten)

Diese kleine Übung nutzt andere Daten als der Auftrag. Führe sie in **einer neuen Codezelle** aus, erkläre jede Zeile und übertrage erst danach das Muster auf deine Fragestellung:

```python
demo = pd.DataFrame({"gruppe": ["A", "A", "B", "B"], "wert": [3, 5, 2, 8]})
demo.groupby("gruppe")["wert"].mean().plot(kind="bar")
plt.xlabel("Gruppe")
plt.ylabel("Mittlerer Wert")
plt.title("Beispiel: Gruppenvergleich")
plt.show()
```

`pd.DataFrame` baut die kleine Übungstabelle; `groupby` fasst gleiche Gruppennamen zusammen; `mean` berechnet pro Gruppe den Mittelwert; `plot(kind="bar")` zeichnet Balken. `xlabel`, `ylabel` und `title` beschriften die Grafik, `show()` zeigt sie an. Für eine Verteilung kann `demo["wert"].plot(kind="hist")` hilfreich sein. Eine Grafik zur eigenen Aufgabe braucht zusätzlich eine passende Frage, die Bedeutung ihrer Werte und eine Grenze der Aussage. Kopiere das Demo nicht als Abgabe.

**Arbeitsregel:** Der Median und die Anzahl ergänzen den Mittelwert. Denke bei einer Managementgrafik daran, dass ein Durchschnitt Unterschiede innerhalb einer Gruppe verdecken kann. Du brauchst keine Copilot-Lizenz; frage zuerst im Skript, in der Tabelle und im Glossar nach. Bei einem technischen Fehler gib der Lehrkraft die genaue Fehlermeldung und den zuletzt ausgeführten Befehl.
