from model.Rubrica import Rubrica
rubricaAmici = Rubrica()
i=len(rubricaAmici)
#Supponendo che il programma verrà usato da un utente tutti gli inici partono da 1
print("Ciao Utente. La tua rubrica al momento contiene ",str(i),"contatti")


rubricaAmici.aggiungiContatto("Mauro", "Fenzio", "3451123")
rubricaAmici.aggiungiContatto("Mario", "Rossi", "2457535")
rubricaAmici.aggiungiContatto("Stefano", "Verdi", "345/34456")
rubricaAmici.aggiungiContatto("Maria", "Stanton", "234233")

#rubricaAmici.elencoContatti()
#rubricaAmici.getContatto(1)
#rubricaAmici.eliminaContatto(2)
#rubricaAmici.elencoContatti()
#rubricaAmici.cercaContatto("mauro")
#rubricaAmici.cercaContatto("Ubaldo")