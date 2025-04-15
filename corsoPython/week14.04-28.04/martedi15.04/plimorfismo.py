#primo polimorfismo
# Definizione della classe base
class Animale:
    # Metodo che può essere sovrascritto dalle sottoclassi (polimorfismo)
    def emetti_suono(self):
        return 'Questo animale fa un suono' 

# Classe derivata da Animale
class Cane(Animale):
    # Override del metodo emetti_suono: comportamento specifico per il Cane
    def emetti_suono(self):
        return "Bau"

# Classe derivata da Animale
class Gatto(Animale):
    # Override del metodo emetti_suono: comportamento specifico per il Gatto
    def emetti_suono(self):
        return 'Miao'
    
#classe non derivata
class Pippo():
    # Override del metodo emetti_suono: comportamento specifico per il Gatto
    def emetti_suono(self):
        return 'Pippo'
# Funzione che accetta un oggetto di tipo Animale (o sottotipo)
def fai_parlare(animale):
    # Chiama il metodo emetti_suono dell'oggetto passato
    print(animale.emetti_suono())
# Creazione di un oggetto Cane
cane = Cane()
# Creazione di un oggetto Gatto
gatto = Gatto()
# Chiamata alla funzione con l'oggetto cane: stamperà "Bau"
fai_parlare(cane)
# Chiamata alla funzione con l'oggetto gatto: stamperà "Miao"
fai_parlare(gatto)
#proviamo con una classe che pero non eredita da animale
pippo = Pippo()
fai_parlare(pippo)

# In Python non esiste l'overloading dei metodi come in altri linguaggi (tipo Java o C++), 
# ma puoi ottenere un comportamento simile usando i parametri di default, come hai fatto tu.
# Definizione della classe Stampa
class Stampa:
    # Metodo mostra con due parametri opzionali, a e b
    def mostra(self, a = None, b = None):
        # Se entrambi i parametri sono forniti
        if a is not None and b is not None:
            print(a + b)
        # Se solo 'a' è fornito
        elif a is not None:
            print(a)
        # Se nessun parametro è fornito
        else:
            print("Niente da mostrare")
            
            



