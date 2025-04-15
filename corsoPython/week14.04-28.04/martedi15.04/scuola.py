# Sistema di gestione studenti
# Immagina di dover creare un sistema di gestione per una scuola che deve mantenere le informazioni sugli studenti, i professori e le lezioni. 
# Seguendo il paradigma della programmazione orientata agli oggetti (00P), dovrai implementare le classi necessarie usando incapsulamento, ereditarietà e polimorfismo.
# Specifiche
# 1. Classe Persona:
# • Crea una classe base chiamata Persona che rappresenti una persona generica.
# • Attributi:
# ■ nome: stringa
# eta: intero
# • Metodi:
# .__init__(self, nome, eta): costruttore che inizializza nome ed eta.
# • presentazione (self): metodo che stampa una frase con il nome e l'età della persona.
# • Regola 1 - Incapsulamento: Gli attributi nome ed eta devono essere privati. Usa getter e setter per accedere e modificare il nome e l'età.
# 2. Classe Studente:
# Crea una sottoclasse di Persona chiamata Studente.
# Attributi:
# voti: lista di interi che rappresentano i voti dello studente.
# • Metodi: о
# .__init__(self, nome, eta, voti): costruttore che inizializza il nome, l'età e i voti dello studente.
# calcola_media (self): metodo che restituisce la media dei voti.
# Override del metodo presentazione (self) per includere la media dei voti nella presentazione.
# Regola 2 - Ereditarietà: Studente eredita dalla classe Persona.
# 3. Classe Professore:
# • Crea una sottoclasse di Persona chiamata Professore.
# • Attributi:
# materia: stringa che rappresenta la materia insegnata.
# 。 Metodi:
# .__init__(self, nome, eta, materia): costruttore che inizializza il nome, l'età e la materia insegnata dal professore. 
# Override del metodo presentazione (self) per includere la materia nella presentazione.
# Regola 3 Polimorfismo: Sia la classe Studente che la classe Professore devono fornire una versione specifica del metodo presentazione, rendendolo polimorfico.

# 1. Classe Persona
class Persona:
    def __init__(self, nome, eta):
        self.__nome = nome  # Incapsulamento, nome privato
        self.__eta = eta  # Incapsulamento, eta privata

    # Getter per il nome
    def get_nome(self):
        return self.__nome
    
    # Setter per il nome
    def set_nome(self, nome):
        self.__nome = nome

    # Getter per l'età
    def get_eta(self):
        return self.__eta
    
    # Setter per l'età
    def set_eta(self, eta):
        self.__eta = eta

    # Metodo di presentazione
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni.")

# 2. Classe Studente (Sottoclasse di Persona)
class Studente(Persona):
    def __init__(self, nome, eta, voti):
        super().__init__(nome, eta)  
        self.__voti = voti  

    # Getter per i voti
    def get_voti(self):
        return self.__voti

    # Setter per i voti
    def set_voti(self, voti):
        self.__voti = voti

    # Metodo per calcolare la media dei voti
    def calcola_media(self):
        if len(self.__voti) == 0:
            return 0
        return sum(self.__voti) / len(self.__voti)

    # Override del metodo presentazione
    def presentazione(self):
        media = self.calcola_media()
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. La mia media dei voti è {media:.2f}.")

# 3. Classe Professore (Sottoclasse di Persona)
class Professore(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)  
        self.__materia = materia  

    # Getter per la materia
    def get_materia(self):
        return self.__materia

    # Setter per la materia
    def set_materia(self, materia):
        self.__materia = materia

    # Override del metodo presentazione
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.get_nome()} e ho {self.get_eta()} anni. Insegno {self.get_materia()}.")

# Creazione di un oggetto di tipo Persona
persona = Persona("Giovanni", 40)
persona.presentazione()

# Creazione di un oggetto di tipo Studente
studente = Studente("Maria", 20, [28, 30, 27, 29])
studente.presentazione()

# Creazione di un oggetto di tipo Professore
professore = Professore("Dott. Rossi", 45, "Matematica")
professore.presentazione()
