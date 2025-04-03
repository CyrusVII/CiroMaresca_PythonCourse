# Le classi sono un'astrazione dei concetti del mondo reale.
# • In Python, una classe è un modello per la creazione di oggetti.
# • Un oggetto è un'istanza di una classe, cioè una copia univoca della classe che ha le sue proprietà uniche.
# • Le classi sono definite usando la parola chiave class, seguita dal nome della classe.
# Le classi possono contenere metodi e attributi.
# • Gli attributi sono variabili associate a una classe.
# • Gli attributi rappresentano le proprietà di un oggetto.
# • Gli attributi di classe sono condivisi tra tutte le istanze della classe.
# i metdoi sono funzione associate a una classe che rappresentano il comportamento di un ogetto

#Creazione di una classe
class Automobile:  # Dichiarazione della classe
    numero_di_ruote = 4  # Attributo di classe

    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo di istanza
        self.modello = modello  # Attributo di istanza

    def stampa_info(self):  # Metodo di istanza
        print("L'automobile è una", self.marca, self.modello)

#dichiarazione ogetto classe
Auto1 = Automobile('Fiat','500')
Auto2 = Automobile('BMW','X3')

#chiamat di un metodo nella classe tramite ogetto istanziato
# Auto1.stampa_info()
# print(Auto1.numero_di_ruote)
# Auto2.stampa_info()
# print(Auto2.numero_di_ruote)


#il costruttore e un metodo speciale che viene evocato a presindere vuoto
#in python il costruttore si dichiara __init__
#serve a inizializzare l oggetto impostando attributi e valori iniziali
class Persona:
  def __init__(self, nome, eta):
    self.nome = nome
    self.eta = eta
    
#creiamo l ogetto
p = Persona('Pippo',30)
p.maggiorenne = True #aggiungo una variabile all ogetto runtime
print(p.nome)
print(p.eta)
print(p.maggiorenne)

#dimostrazione metodo statico
class Calcolatrice:  # Dichiarazione della classe
    @staticmethod  # Decoratore per definire un metodo statico
    def somma(a, b):
        return a + b  # Restituisce la somma dei due numeri

# Chiamata al metodo statico senza creare un'istanza della classe
# risultato = Calcolatrice.somma(5, 4)
# print(risultato)  # Output: 9

#-------
class Contatore:  
    numero_istanze = 0  # Attributo di classe: conta il numero di istanze create

    def __init__(self):  
        # Ogni volta che viene creata un'istanza, incrementiamo il contatore
        Contatore.numero_istanze += 1  

    @classmethod  # Decoratore per definire un metodo di classe
    def mostra_numero_istanze(cls): # In un metodo di classe (@classmethod), usiamo cls invece di self perché il metodo opera sulla classe stessa, non sulle singole istanze.
        # Metodo di classe che stampa il numero di istanze create
        print(f"Sono state create {cls.numero_istanze} istanze.")  

# Creazione di alcune istanze della classe Contatore
C1 = Contatore()  # Incrementa numero_istanze a 1
C2 = Contatore()  # Incrementa numero_istanze a 2

# Chiamata al metodo di classe senza creare un'istanza
Contatore.mostra_numero_istanze()  # Output: Sono state create 2 istanze.


