import DbConnetion
dbName = "studentsregister"
def create():
  conn = DbConnetion.db_connection(dbName)
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS studenti (
      id INT AUTO_INCREMENT PRIMARY KEY,
      nome VARCHAR(255),
      cognome VARCHAR(255)
  )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS voti (
      id INT AUTO_INCREMENT PRIMARY KEY,
      studente_id INT,
      materia VARCHAR(255),
      voto FLOAT,
      FOREIGN KEY (studente_id) REFERENCES studenti(id) ON DELETE CASCADE
  )
  """)

  conn.commit()
  cursor.close()
  conn.close()
    
class Student():
  def __init__(self,id,name,surname):
    self.id = id
    self.name = name
    self.surname = surname
    self.votes = self.load_votes()
  
  #raccolta voti studente
  def load_votes():
    myDb = DbConnetion.db_connection(dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT materia,voto FROM voti WHERE studente_id = %s", (self.id,))
  # Verifica se la materia inserita esiste nel dizionario dei voti
  def exist_valutation(self,key):
    pass
  
  # Aggiunge un singolo voto per ciascuna materia (utile per una valutazione completa)
  def add_all_valutation(self):
    pass
    
  # Aggiunge uno o più voti a una materia specifica scelta dall'utente
  def add_one_valutation(self):
    pass
  
  # Stampa tutte le informazioni dello studente, voti per materia e relativa media
  def print_info(self,id):
    pass
      
  # Mostra solo l'elenco delle materie disponibili
  def print_subject(self):
    pass
  
  # Calcola la media dei voti per una specifica materia
  def med_vote_for_subject(self,val):
    pass
  
  # Calcola la media generale di tutte le materie per lo studente
  def med_all_vote(self):
    pass

class Register():
  def __init__(self):
    # Dizionario che contiene tutti gli studenti (id: Student)
    self.student = self.load_all_students()
  
  #get all student from db
  def load_all_students(self):
    myDb = DbConnetion.db_connection(dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT id, nome, cognome FROM studenti")
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    return [Student(*i) for i in result]

  # Permette l'aggiunta di uno o più studenti al registro
  def add_student(self):
    pass
  
  # Calcola e stampa la media complessiva della classe (tutti gli studenti)
  def med_of_class(self):
    pass
    
  # Identifica lo studente con la media più alta
  def best_student(self):
    pass

  # Stampa le informazioni di tutti gli studenti nel registro
  def print_all_students(self):
    print("--- Elenco degli studenti ---")
    for student in self.student:
      print(f"ID: {student.id}, Nome: {student.name}, Cognome: {student.surname}")

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
        pass
      case 2:
        pass
      case 3:
        pass
      case 4:
        pass
      case 5:
        pass
      case 6:
        pass
      case _: 
        print('Fine programma...')
        break

    # Chiede all'utente se vuole tornare al menu
    if input("Vuoi tornare al menu? s/n ---> ").strip().lower() == "n":
      break

#inizalizzazione programma
create()
DbConnetion.db_connection(dbName)
register = Register()
register.load_all_students()
register.print_all_students()
#main()