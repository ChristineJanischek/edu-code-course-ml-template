punktzahlen = [8, 5, 10, 6]

def waehle_aufgabe(punkte):
    # TODO: dreistufige Entscheidung ergaenzen.
    if punkte < 6:
        return 'Grundlagen'
    return 'Uebung oder Vertiefung'

for wert in punktzahlen:
    print(wert, waehle_aufgabe(wert))
