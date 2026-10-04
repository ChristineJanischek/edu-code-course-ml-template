punktzahlen = [8, 5, 10, 6]

def waehle_aufgabe(punkte):
    # TODO: dreistufige Entscheidung ergaenzen.
    if punkte < 6:
        return 'Grundlagen wiederholen'
    return 'Vertiefungsaufgabe bearbeiten'

for wert in punktzahlen:
    print(wert, waehle_aufgabe(wert))
