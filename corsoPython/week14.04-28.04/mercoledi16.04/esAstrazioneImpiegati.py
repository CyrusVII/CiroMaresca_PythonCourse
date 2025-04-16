# Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico. 
# Esistono diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati hanno alcune caratteristiche comuni, come il nome, il cognome e lo stipendio. 
# Inoltre, ogni impiegato ha un metodo per calcolare il suo stipendio mensile, che può variare a seconda del ruolo.
# Obiettivi:
# 1. Creare una classe astratta Impiegato con:
# • Un costruttore che accetta nome, cognome e stipendio base.
# • Un metodo astratto calcola_stipendio() che dovrà essere implementato dalle classi derivate.
# 2. Creare due classi derivate:
# O ImpiegatoFisso: riceve lo stipendio base senza modifiche.
# • ImpiegatoAProvvigione: riceve lo stipendio base più un bonus basato sulle
# vendite.
# 3. Implementare una funzione che stampi le informazioni degli impiegati e il loro stipendio calcolato.
from abc import ABC, abstractmethod

class Impiegato(ABC):
    def __init__(self, nome, cognome, stipendio_base, vendite, email, password):
        pass

    @abstractmethod
    def calcola_stipendio(self):
        pass

    @abstractmethod
    def get_password(self):
        pass

    @abstractmethod
    def get_stipendio(self):
        pass

    @abstractmethod
    def aggiungi_vendite(self, add):
        pass


class ImpiegatoFisso(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, email, password):
        self._nome = nome
        self._cognome = cognome
        self.__stipendio_base = stipendio_base
        self._vendite = vendite
        self._email = email
        self.__password = password

    def get_password(self):
        return self.__password

    def get_stipendio(self):
        return self.__stipendio_base

    def calcola_stipendio(self):
        return self.get_stipendio()

    def aggiungi_vendite(self, add):
        self._vendite += add


class ImpiegatoApprovigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite, email, password):
        self._nome = nome
        self._cognome = cognome
        self.__stipendio_base = stipendio_base
        self._vendite = vendite
        self._email = email
        self.__password = password

    def get_password(self):
        return self.__password

    def get_stipendio(self):
        return self.__stipendio_base

    def calcola_stipendio(self):
        return self.get_stipendio() + (self._vendite * 0.01 * self.get_stipendio())

    def aggiungi_vendite(self, add):
        self._vendite += add


class Admin:
    def __init__(self, nome, password):
        self.__nome = nome
        self.__password = password

    def valid_password(self, password):
        return self.__password == password

    def valid(self, name):
        return self.__nome == name


class Gestione:
    def __init__(self):
        self.users = {}
        self.admins = {}
        

    def login(self):
        #creo un admin per fare prove
        self.admins["admin1"] = Admin("admin1", "admin123")
        print("=== LOGIN ===")
        tipo = input("Sei un admin o un impiegato? (admin/impiegato): ").strip().lower()
        match tipo:
            case "admin":
                nome = input("Nome admin: ")
                password = input("Password: ")
                admin = self.admins.get(nome)
                if admin and admin.valid(nome) and admin.valid_password(password):
                    print("Login Admin riuscito!\n")
                    self.menu_admin()
                else:
                    print("Credenziali admin non valide.\n")
            case "impiegato":
                email = input("Email: ")
                password = input("Password: ")
                impiegato = self.users.get(email)
                if impiegato and impiegato.get_password() == password:
                    print("Login Impiegato riuscito!\n")
                    self.menu_impiegato(impiegato)
                else:
                    print("Credenziali impiegato non valide.\n")
            case _:
                print("Tipo utente non riconosciuto.\n")

    # === MENU ADMIN ===
    def menu_admin(self):
        while True:
            print("\n--- MENU ADMIN ---")
            print("1. Crea Impiegato")
            print("2. Elimina Impiegato")
            print("3. Elenco Impiegati")
            print("4. Logout")
            scelta = input("Scelta: ")
            match scelta:
                case "1":
                    self.crea_impiegato()
                case "2":
                    self.elimina_impiegato()
                case "3":
                    self.lista_impiegati()
                case "4":
                    print("Logout effettuato.\n")
                    self.login()
                case _:
                    print("Scelta non valida.")

    # === MENU IMPIEGATO ===
    def menu_impiegato(self, impiegato):
        while True:
            print("\n--- MENU IMPIEGATO ---")
            print("1. Visualizza Stipendio")
            print("2. Aggiungi Vendite")
            print("3. Logout")
            scelta = input("Scelta: ")
            match scelta:
                case "1":
                    print(f"Stipendio calcolato: €{impiegato.calcola_stipendio():.2f}")
                case "2":
                    try:
                        valore = float(input("Inserisci valore vendite da aggiungere: "))
                        impiegato.aggiungi_vendite(valore)
                        print("Vendite aggiornate.")
                    except ValueError:
                        print("Valore non valido.")
                case "3":
                    print("Logout effettuato.\n")
                    self.login()
                case _:
                    print("Scelta non valida.")

    # === METODI ADMIN ====
    def crea_impiegato(self):
        print("\n--- Crea nuovo impiegato ---")
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        email = input("Email: ")
        password = input("Password: ")
        try:
            stipendio_base = float(input("Stipendio base: "))
            vendite = float(input("Vendite iniziali: "))
        except ValueError:
            print("Valore numerico non valido.")
            return

        tipo = input("Tipo impiegato (fisso/approvigione): ").strip().lower()

        if email in self.users:
            print("Un impiegato con questa email esiste già.")
            return

        if tipo == "fisso":
            self.users[email] = ImpiegatoFisso(nome, cognome, stipendio_base, vendite, email, password)
        elif tipo == "approvigione":
            self.users[email] = ImpiegatoApprovigione(nome, cognome, stipendio_base, vendite, email, password)
        else:
            print("Tipo non valido.")
            return

        print("Impiegato creato con successo.")

    def elimina_impiegato(self):
        print("\n--- Elimina impiegato ---")
        email = input("Inserisci email dell'impiegato da eliminare: ")
        if email in self.users:
            del self.users[email]
            print("Impiegato eliminato.")
        else:
            print("Impiegato non trovato.")

    def lista_impiegati(self):
        print("\n--- Elenco Impiegati ---")
        if not self.users:
            print("Nessun impiegato registrato.")
            return
        for email, imp in self.users.items():
            print(f"{email} | {imp._nome} {imp._cognome} | Stipendio base: €{imp.get_stipendio():.2f}")


        print("\n--- Elenco Impiegati ---")
        if not self.users:
            print("Nessun impiegato registrato.")
            return
        for email, imp in self.users.items():
            tipo = "Fisso" if isinstance(imp, ImpiegatoFisso) else "Approvigione"
            print(f"{imp._nome} {imp._cognome} ({tipo}) - Email: {email}")
            
gestion = Gestione()
gestion.login()