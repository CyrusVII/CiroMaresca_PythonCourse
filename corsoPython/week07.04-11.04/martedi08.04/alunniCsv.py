import csv
import os

# Funzione per verificare se esiste il file CSV degli studenti
def file_exist():
    file_path = 'csvFolder/alunni.csv'
    return os.path.exists(file_path)

# Classe per rappresentare uno studente
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # Dizionario per contenere i voti per materia
        self.valutation = {
            "math": [],
            "italian": [],
            "english": [],
            "history": [],
        }

    # Verifica se una materia esiste nella lista delle valutazioni
    def exist_valutation(self, key):
        return key in self.valutation

    # Aggiunge un voto per ogni materia
    def add_all_valutation(self):
        print("--- Menu per aggiungere un voto per materia ---")
        print(f"Studente {self.name} {self.surname}: ")
        for key in self.valutation:
            while True:
                try:
                    vote = float(input(f"Inserisci il voto per {key} ---> "))
                    self.valutation[key].append(vote)
                    break
                except ValueError:
                    print('Voto inserito non valido. Riprova')

    # Aggiunge più voti per una materia specifica
    def add_one_valutation(self):
        while True:
            print("--- Menu per aggiungere un voto ---")
            print(f"Studente {self.name} {self.surname}: ")
            self.print_subject()
            subject = input("\n-----\n Inserisci nome materia per cui aggiungere voti ---> ").lower().strip()
            if self.exist_valutation(subject):
                break
        quantity = int(input(f"Quanti voti vuoi aggiungere per {subject} ---> "))
        for _ in range(quantity):
            while True:
                try:
                    vote = float(input(f"Inserisci il voto per {subject} ---> "))
                    self.valutation[subject].append(vote)
                    break
                except ValueError:
                    print('Voto inserito non valido. Riprova')

    # Stampa le informazioni dello studente con la media per materia
    def print_info(self, id):
        print(f"---\n{id}) {self.name} {self.surname}:")
        for key, val in self.valutation.items():
            print(f"{key} : {val} / Media : {self.med_vote_for_subject(val)}")

    # Stampa l'elenco delle materie
    def print_subject(self):
        print("--- Materie ---")
        for key in self.valutation.keys():
            print(key, end=" / ")

    # Calcola la media dei voti per una materia
    def med_vote_for_subject(self, val):
        return sum(val) / len(val) if val else 0

    # Calcola la media generale di tutte le materie
    def med_all_vote(self):
        total = sum(sum(val) for val in self.valutation.values())
        number_of_votes = sum(len(val) for val in self.valutation.values())
        return round(total / number_of_votes, 1) if number_of_votes > 0 else 0

# Classe che gestisce il registro degli studenti
class Register:
    def __init__(self):
        self.student = {}  # Dizionario degli studenti con ID come chiave
        self.ensure_csv_folder()  # Crea la cartella csvFolder se non esiste
        self.load_from_csv()  # Carica gli studenti dal file CSV

    # Crea la cartella csvFolder se non esiste
    def ensure_csv_folder(self):
        if not os.path.exists("csvFolder"):
            os.makedirs("csvFolder")

    # Aggiunge nuovi studenti al registro
    def add_student(self):
        n = int(input("Quanti studenti vuoi aggiungere ---> "))
        for _ in range(n):
            name = input("Inserisci nome studente ---> ").capitalize()
            surname = input("Inserisci cognome studente ---> ").capitalize()
            student = Student(name, surname)
            new_id = max(self.student.keys(), default=0) + 1
            self.student[new_id] = student
            print("--- Studente aggiunto ---")

    # Calcola la media complessiva della classe
    def med_of_class(self):
        if not self.student:
            print("Nessuno studente disponibile.")
            return
        tot = sum(s.med_all_vote() for s in self.student.values())
        print(f"La media complessiva di classe è: {tot / len(self.student):.2f}")

    # Trova lo studente con la media più alta
    def best_student(self):
        if not self.student:
            print("Nessuno studente disponibile.")
            return
        best = max(self.student.items(), key=lambda x: x[1].med_all_vote())
        student = best[1]
        print(f"Il miglior studente è {student.name} {student.surname} con una media di {student.med_all_vote()}")

    # Stampa tutti gli studenti presenti nel registro
    def print_all_student(self):
        if not self.student:
            print("Nessuno studente registrato.")
        for key, val in self.student.items():
            val.print_info(key)

    #aggiungi all vote for 1 student
    def all_vote_for_one(self):
        key = int(input("Inserisci id studente per cui aggiungere voti ---> "))
        if key in self.student:
            self.student[key].add_all_valutation()
        else:
            print("Studente non trovato")
    
    #metod voti per una materia
    def vote_for_one_subject(self):
        key = int(input("Inserisci id studente per cui aggiungere voti ---> "))
        if key in self.student:
            self.student[key].add_one_valutation()
        else:
            print("Studente non trovato")
    
    # Salva i dati degli studenti nel file CSV
    def save_to_csv(self):
        with open('csvFolder/alunni.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            if self.student:
                subjects = list(next(iter(self.student.values())).valutation.keys())
                header = ["id", "name", "surname"] + subjects
                writer.writerow(header)
                for student_id, student in self.student.items():
                    row = [student_id, student.name, student.surname]
                    for subject in subjects:
                        row.append(",".join(map(str, student.valutation[subject])))
                    writer.writerow(row)
            else:
                pass  

    # Carica i dati degli studenti dal file CSV
    def load_from_csv(self):
        if not file_exist():
            return
        with open('csvFolder/alunni.csv', 'r') as file:
            reader = csv.reader(file)
            try:
                header = next(reader)
            except StopIteration:
                print("Il file CSV è vuoto.")
                return
            
            subjects = header[3:]
            for row in reader:
                student_id = int(row[0])
                name = row[1]
                surname = row[2]
                student = Student(name, surname)
                for i, subject in enumerate(subjects):
                    votes_str = row[3 + i]
                    votes = list(map(float, votes_str.split(","))) if votes_str else []
                    student.valutation[subject] = votes
                self.student[student_id] = student
    
    #metodo per eliminare alunno
    def delete_student(self):
        n = int(input("Id studente da eliminare ---> "))
        self.student.pop(n)
    
    #delete vote metodo
    def delete_modify_vote(self):
        key = int(input("Inserisci id studente per cui eliminare/modificare un voto ---> "))
        if key in self.student:
            student = self.student[key]
            print(f"--- {student.name} {student.surname} ---")
            student.print_subject()
            subject = input("\nInserisci la materia da cui eliminare/modificare un voto ---> ").lower().strip()
            ch = input("Vuoi rimuovere o modificare un voto? r/m --> ").lower().strip()
            if student.exist_valutation(subject):
                if student.valutation[subject]:
                    print(f"Voti attuali per {subject}: {student.valutation[subject]}")
                    try:
                        vote_to_remove = float(input("Inserisci il voto da eliminare/modificare ---> "))
                        if vote_to_remove in student.valutation[subject]:
                            match ch:
                                case "r":
                                    student.valutation[subject].remove(vote_to_remove)
                                    print("Voto eliminato con successo.")
                                case "m":
                                    student.valutation[subject].remove(vote_to_remove)
                                    try:
                                        new_vote = float(input("Inserisci il nuovo voto ---> "))
                                        student.valutation[subject].append(new_vote)
                                        print("Voto modificato con successo.")
                                    except ValueError:
                                        print("Input non valido. Inserisci un numero.")
                        else:
                            print("Il voto specificato non esiste.")
                    except ValueError:
                        print("Input non valido. Inserisci un numero.")
                else:
                    print(f"Nessun voto presente per la materia {subject}.")
            else:
                print("Materia non trovata.")
        else:
            print("Studente non trovato.")

# Funzione principale del programma
def main(): 
    register = Register()
    
    # Menu di interazione con l'utente
    while True:
        try:
            ch = int(input("--- Menu ---\n 1) Visualizza studenti\n 2) Aggiungi studenti \n 3) Aggiungi 1 voto per materia a uno studente\n"
                        " 4) Aggiungi voto per specifica materia \n 5) Miglior studente \n "
                        "6) Media classe \n 7) Elimina studente \n 8) Delete modify vote \n 0) Exit \n ---> "))
        except ValueError:
            print("Input non valido. Inserisci un numero.")
            continue
        try:
            match ch:
                case 1:
                    register.print_all_student()
                case 2:
                    register.add_student()
                case 3:
                    register.all_vote_for_one()
                case 4:
                    register.vote_for_one_subject()
                case 5:
                    register.best_student()
                case 6:
                    register.med_of_class()
                case 7:
                    register.delete_student()
                case 8:
                    register.delete_modify_vote()
                case 0:
                    print("Fine programma...")
                    break
                case _ :
                    print("Opzione non valida")

            if input("Vuoi tornare al menu? s/n ---> ").strip().lower() == "n":
                register.save_to_csv()
                break
        except:
            print("Errore, ma i dati sono stati salvati")
            register.save_to_csv()
            continue

# Avvio del programma
main()

