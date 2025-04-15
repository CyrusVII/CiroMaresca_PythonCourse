# creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.
# 1. Classe ContoBancario:
# • Attributi privati:
# • __titolare (stringa che rappresenta il nome del titolare del conto)
# ■ __saldo (decimale che rappresenta il saldo del conto)
# • Metodi pubblici:
# ■ deposita(importo): aggiunge un importo al saldo solo se l'importo è
# positivo.
# • preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
# ■ visualizza_saldo(): restituisce il saldo corrente senza permettere la sua
# modifica diretta.
# 2. Gestione dei Metodi e Sicurezza:
# I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
# Aggiungere metodi "getter" e "setter" per gli attributi come _titolare,
# applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).

class User:
    def __init__(self, nome, cognome, username, password, pin, saldo=0.0):
        self._nome = nome
        self._cognome = cognome
        self.__username = username
        self.__password = password
        self._pin = pin
        self._saldo = saldo

    def verifica_password(self, password):
        return self.__password == password

    def get_username(self):
        return self.__username

    def get_nome(self):
        return self._nome

    def get_pin(self):
        return self._pin

    def get_saldo(self):
        return self._saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            return True
        return False

    def preleva(self, importo):
        if 0 < importo <= self._saldo:
            self._saldo -= importo
            return True
        return False

class ContoBancario:
    def __init__(self):
        self.__utenti_registrati = {}
        self.utente = None  # Utente attualmente loggato
        
    def add_user(self,key,val):
        self.__utenti_registrati[key] = val
        
    # Metodo di registrazione
    def register(self):
        print("== Registrazione ==")
        nome = input("Nome: ")
        cognome = input("Cognome: ")
        username = input("Username: ")

        if username in self.__utenti_registrati:
            print("⚠️ Username già in uso.")
            return

        password = input("Password: ")
        pin = input("PIN (4 cifre): ")

        if not pin.isdigit() or len(pin) != 4:
            print("⚠️ PIN non valido.")
            return

        nuovo_utente = User(nome, cognome, username, password, pin)
        self.add_user(username,nuovo_utente)
        print("✅ Registrazione completata con successo.")

    def login(self):
        print("== Login ==")
        username = input("Username: ")
        password = input("Password: ")

        utente = self.__utenti_registrati.get(username)
        if utente is None:
            print("❌ Utente non trovato.")
            return

        if utente.verifica_password(password):
            self.utente = utente
            print(f"✅ Benvenuto, {utente.get_nome()}!")
        else:
            print("❌ Password errata.")
            self.utente = None

    def deposita(self):
        if not self.utente:
            print("⚠️ Effettua il login prima.")
            return
        try:
            importo = float(input("Importo da depositare: "))
            if self.utente.deposita(importo):
                print(f"💰 Deposito di €{importo:.2f} effettuato con successo.")
            else:
                print("⚠️ Importo non valido.")
        except ValueError:
            print("⚠️ Inserisci un numero valido.")

    def preleva(self):
        if not self.utente:
            print("⚠️ Effettua il login prima.")
            return
        try:
            importo = float(input("Importo da prelevare: "))
            pin = input("Inserisci PIN: ")
            if pin != self.utente.get_pin():
                print("❌ PIN errato.")
                return
            if self.utente.preleva(importo):
                print(f"💸 Prelievo di €{importo:.2f} effettuato con successo.")
            else:
                print("❌ Fondi insufficienti o importo non valido.")
        except ValueError:
            print("⚠️ Inserisci un numero valido.")

    def visualizza_saldo(self):
        if not self.utente:
            print("⚠️ Effettua il login prima.")
            return
        print(f"📄 Saldo attuale: €{self.utente.get_saldo():.2f}")


#funzione main per avviare il programma
def main():
    banca = ContoBancario()
    #carico un account di prova
    us = User("Ciro","Maresca","csy","123","1234",300.0)
    banca.add_user(us.get_username(),us)
    while True:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Registrati")
        print("2. Login")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case '1':
                banca.register()
            case '2':
                banca.login()
                if banca.utente:
                    while True:
                        print("\n--- Area Personale ---")
                        print("1. Deposita")
                        print("2. Preleva")
                        print("3. Visualizza Saldo")
                        print("4. Logout")
                        opzione = input("Scegli: ")

                        match opzione:
                            case '1':
                                try:
                                    banca.deposita()
                                except ValueError:
                                    print("⚠️ Inserisci un numero valido.")
                            case '2':
                                try:
                                    banca.preleva()
                                except ValueError:
                                    print("⚠️ Inserisci un numero valido.")
                            case '3':
                                banca.visualizza_saldo()
                            case '4':
                                banca.utente = None
                                print("🔓 Logout effettuato.")
                                break
                            case _:
                                print("❌ Opzione non valida.")
            case '3':
                print("👋 Arrivederci!")
                break
            case _:
                print("❌ Scelta non valida.")


# Avvia il programma
if __name__ == "__main__":
    main()
