from model.Contatto import Contatto

class Rubrica:
    def __init__(self):
        self._Rubrica = []

    def aggiungiContatto(self, nome, cognome, telefono):
        self._Rubrica.append(Contatto(nome, cognome, telefono))
        print("Contatto ",nome," ",cognome, " inserito")

    # restituisce una stringa con l'elenco delle voci della rubrica separate
    # da ", "; l'elenco inizia con "(" e termina con ")"
    def elencoContatti(self):
        str=""
        for contatto in self._Rubrica:
             str += contatto.nome + " " + contatto.cognome + " " + contatto.telefono + ","
        str="(" + str[:len(str)-1]+ ')'
        print(str)


    def getContatto(self, position):
       try:
            s=self._Rubrica[position-1]#Lo uso per trasforare l'indice da 1 a 0
            print("Il contatto nella rubrica alla posizione "+str(position)+" é:\n", s.nome, s.cognome, s.telefono)
       except IndexError:
           print("La posizione inserita è oltre il limite della rubrica")



    def eliminaContatto(self, position):
       try:
            s=self._Rubrica[position-1]#Lo uso per trasformare l'indice da 1 a 0
            self._Rubrica.remove(s)
            print("Cancellato" )
       except IndexError:
            print("La posizione è oltre il limite della rubrica")

    def cercaContatto(self, key):
        for contatto in self._Rubrica:
            if contatto.nome.lower() == key.lower() or contatto.cognome.lower() == key.lower() or contatto.telefono.lower() == key.lower():
                print(contatto.nome, contatto.cognome, contatto.telefono)
                break
        else:
                print("Contatto non trovato")



    def __len__(self):
        return len(self._Rubrica)


