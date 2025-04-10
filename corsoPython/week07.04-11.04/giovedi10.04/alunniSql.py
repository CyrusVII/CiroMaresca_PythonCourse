
class Student():
  
  def __init__(self,name,surname):
    # Inizializza lo studente con nome, cognome e un dizionario di voti per materia
    self.name = name
    self.surname = surname
    self.valutation = {
            "math": [],
            "italian": [],
            "english": [],
            "history": [],
            "geography": [],
            "science": [],
            "physics": [],
            "art": [],
            "physical education": [],
            "technology": []
        } 
  
  # Verifica se la materia inserita esiste nel dizionario dei voti
  def exist_valutation(self,key):
    if key in self.valutation:
      return True
    return False
  
  # Aggiunge un singolo voto per ciascuna materia (utile per una valutazione completa)
  def add_all_valutation(self):
    print("--- Menu per aggiungere un voto per materia ---")
    print(f"Studente {self.name} {self.surname}: ")
    for key,val in self.valutation.items():
      while True:
        try:
          vote = float(input(f"Inserisci il voto per {key} ---> "))
          self.valutation[key].append(vote)
          break
        except ValueError:
          print('Voto inserito non valido. Riprova')
    
  # Aggiunge uno o più voti a una materia specifica scelta dall'utente
  def add_one_valutation(self):
    while True:
      print("--- Menu per aggiungere un voto ---")
      print(f"Studente {self.name} {self.surname}: ")
      self.print_subject()
      subject = input("\n-----\n Inserisci nome materia per cui aggiungere voti ---> ").lower().strip()
      if self.exist_valutation(subject):
        break
    quantity = int(input(f"Quanti voti vuoi aggiungere per {subject} ---> "))
    while True:
      try:
        if quantity == 1:
            vote = int(input(f"Inserisci il voto per {subject} ---> "))
            self.valutation[subject].append(vote)
            break
        else:
          for i in range(quantity):
            while True:
              vote = float(input(f"Inserisci il voto per {subject} ---> "))
              self.valutation[subject].append(vote)
              break
          break
      except ValueError:
            print('Voto inserito non valido. Riprova')
  
  # Stampa tutte le informazioni dello studente, voti per materia e relativa media
  def print_info(self,id):
    print(f"---\n{id}) {self.name} {self.surname}:")
    for key,val in self.valutation.items():
      print (f"{key} : {val} / Media : {self.med_vote_for_subject(val)}")
      
  # Mostra solo l'elenco delle materie disponibili
  def print_subject(self):
    print("--- Materie ---")
    for key in self.valutation.keys():
      print(key, end=" / ")
  
  # Calcola la media dei voti per una specifica materia
  def med_vote_for_subject(self,val):
    if len(val) != 0:
      return sum(val) / len(val)
    else:
      return 0
  
  # Calcola la media generale di tutte le materie per lo studente
  def med_all_vote(self):
    total = 0
    number_of_vote = 0
    for key,val in self.valutation.items():
      total += sum(val)
      number_of_vote += len(val)
    if number_of_vote != 0:
      return round(total / number_of_vote, 1)
    return 0

class Register():
  def __init__(self):
    # Dizionario che contiene tutti gli studenti (id: Student)
    self.student = {}
  
  # Permette l'aggiunta di uno o più studenti al registro
  def add_student(self):
    n = int(input("Quanti studenti vuoi aggiungere ---> "))
    for i in range(n):
      name = input("Inserisci nome studente ---> ").capitalize()
      surname = input("Inserisci cognome studente ---> ").capitalize()
      student = Student(name,surname)
      # Genera un nuovo ID incrementale
      if self.student:
        new_id = max(self.student.keys()) + 1
      else:
        new_id = 1
      self.student[new_id] = student
      print("--- Studente aggiunto ---")
  
  # Calcola e stampa la media complessiva della classe (tutti gli studenti)
  def med_of_class(self):
    tot = 0
    for key,val in self.student.items():
      tot += val.med_all_vote()
    print(f"La media complessiva di classe è: {tot / max(self.student.keys())}")
    
  # Identifica lo studente con la media più alta
  def best_student(self):
    best_med = -1
    best_student = None
        
    for student_id, student in self.student.items():
      student_med = student.med_all_vote() 
      if student_med > best_med:
        best_med = student_med
        best_student = student
        
    if best_student:
      print(f"Il miglior studente è {best_student.name} {best_student.surname} con una media di {best_med}")
    else:
      print("Nessun studente trovato.")

  # Stampa le informazioni di tutti gli studenti nel registro
  def print_all_student(self):
    for key,val in self.student.items():
      val.print_info(key)
      
# ---------- MAIN ----------
def main():
  # Crea un'istanza del registro studenti
  register = Register()
  print("--- Benvenuto/a! Aggiungiamo i tuoi studenti ---")
  register.add_student()
  while True:
    ch = int(input("--- Menu ---\n 1) Visualizza studenti\n 2) Aggiungi studenti \n 3) Aggiungi 1 voto per materia a uno studente\n "
                  "4) Aggiungi voto per specifica materia \n 5) Miglior studente \n 6) Media classe \n 7) Exit \n ---> "))
    
    # Gestione delle opzioni del menu
    match ch:
      case 1:
        register.print_all_student()
      case 2:
        register.add_student()
      case 3:
        key = int(input("---\n Inserisci id studente per cui aggiungere voti ---> "))
        if key in register.student:
          register.student[key].add_all_valutation()
        else:
          print("---\nStudente non trovato")
      case 4:
        key = int(input("---\n Inserisci id studente per cui aggiungere voti ---> "))
        if key in register.student:
          register.student[key].add_one_valutation()
        else:
          print("---\nStudente non trovato")
      case 5:
        register.best_student()
      case 6:
        register.med_of_class()
      case _: 
        print('Fine programma...')
        break

    # Chiede all'utente se vuole tornare al menu
    if input("Vuoi tornare al menu? s/n ---> ").strip().lower() == "n":
      break

#inizalizzazione programma
main()