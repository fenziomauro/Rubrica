from model.Rubrica import Rubrica
rubricaAmici = Rubrica()
i = len(rubricaAmici)

while True:
    i = len(rubricaAmici)
    print("\n Ciao Utente. La tua rubrica al momento contiene ", str(i), "contatti")
    ordine = str(
        input("""
        Cosa vuoi fare?
        [a] Aggiungi contatto
        [c] Cancella contatto (usando la posizione partendo da 1)
        [r] Ricerca contatto (usando una chiave)
        [rp] Ricerca contatto (usando la posizione partendo da 1)
        [v] Visualizza l'intera rubrica
        //////////////////////////////
        [p] Popola la rubrica (con numeri fittizi)
        [u] Uscire.
    """))
    if ordine == "a":
        nome = str(input("Quale è il nome?"))
        cognome = str(input("quale è il cognome"))
        telefono = str(input("Quale è il telefono"))

        rubricaAmici.aggiungiContatto(nome, cognome, telefono)

    elif ordine == "c":
        pos = int(input("Indicami la posizione del contatto da cancellare:"))
        try:
            if pos > i:
                print("Questo contatto non esiste")
            else:
                rubricaAmici.eliminaContatto(pos)
        except ValueError:
            print("La posizione deve essere un numero intero")

    elif ordine == "r":
        key = str(input("Dammi la chiave:"))
        rubricaAmici.cercaContatto(key)
    elif ordine == "rp":
        try:
            pos = int(input("Dammi la posizione:"))
            rubricaAmici.getContatto(pos)
        except ValueError:
            print("La posizione deve essere un numero intero")
    elif ordine == "v":
        rubricaAmici.elencoContatti()

    elif ordine == "p":
        rubricaAmici.aggiungiContatto("Mauro", "Fenzio", "3451123")
        rubricaAmici.aggiungiContatto("Mario", "Rossi", "2457535")
        rubricaAmici.aggiungiContatto("Stefano", "Verdi", "345/34456")
        rubricaAmici.aggiungiContatto("Maria", "Stanton", "234233")

    elif ordine == "u":
        print("Ciao ciao")
        break
    else:
        print("Selezione errata")
