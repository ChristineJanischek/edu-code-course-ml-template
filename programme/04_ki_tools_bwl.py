kriterien = {'fachliche Eignung': 25, 'Datenschutz': 20, 'Erklaerbarkeit': 15, 'Integration': 15, 'Kosten': 15, 'Anbieterabhaengigkeit': 10}
bewertungen = {'Regeln': [4,5,5,4,5,5], 'ML': [5,4,4,3,3,4], 'ML plus Sprachmodell': [5,2,2,3,2,2]}
# TODO: gewichtete Nutzwerte berechnen und eine Sensitivitaetsprobe dokumentieren.
print('Gewichtssumme:', sum(kriterien.values()))
