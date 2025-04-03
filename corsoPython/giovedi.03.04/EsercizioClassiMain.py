class Libro:
    def __init__(self, titolo, autore, pagine):
        #Inizializza un libro con titolo, autore e numero di pagine.
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        #Restituisce una descrizione del libro.
        return f"Il libro è '{self.titolo}' ed è stato scritto da {self.autore}, con {self.pagine} pagine."


class Main:
    def __init__(self):
        #Costruttore della classe Main. Inizializza la classe senza nessun oggetto.
        self.libro = None

    def crea_libro(self, titolo, autore, pagine):
        #Crea un oggetto Libro e lo assegna all'attributo libro.
        self.libro = Libro(titolo, autore, pagine)

    def esegui_metodi_libro(self):
        #Verifica se esiste un oggetto libro e chiama il metodo descrizione.
        if self.libro:  # Se l'oggetto libro esiste
            print(self.libro.descrizione())
        else:
            print("Nessun libro creato.")

# Esecuzione del codice
main = Main()  # Crea un oggetto Main
main.crea_libro("La programmazione di Mirko", "Mirko", 22)  # Crea un libro
main.esegui_metodi_libro()  # Chiama il metodo descrizione del libro
print()


