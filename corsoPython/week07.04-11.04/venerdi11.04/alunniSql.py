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
    self.subject = {1:"matematica",
                    2:"italiano",
                    3:'storia',
                    4:"informatica"
                    }
    
  #raccolta voti studente
  def load_votes(self):
    myDb = DbConnetion.db_connection(dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT materia,voto FROM voti WHERE studente_id = %s", (self.id,))
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    
    dict = {}
    for key,val in result:
      if key in dict:
        dict[key].append(val)
      else:
        dict[key] = [val]
    return dict
  
   # Aggiungi un voto per la materia
  
  #add valutation
  def add_valuation(self):
    while True:
      print("--- Lista Materie ---")
      for key, val in self.subject.items():
        print(f"{key}) {val}")
      try:
        subj = int(input("Inserisci numero materia da aggiungere ---> "))
        if subj in self.subject:
          voto = float(input(f"Inserisci voto studente per {self.subject.get(subj)} ---> "))
          myDb = DbConnetion.db_connection(dbName)
          cursor = myDb.cursor()
          query = "INSERT INTO voti (studente_id, materia, voto) VALUES (%s, %s, %s)"
          val = self.id, self.subject.get(subj), voto
          cursor.execute(query, val)
          myDb.commit()
          cursor.close()
          myDb.close()
          print('Voto inserito')
          if input("Vuoi inserire un altro voto? s/n  ---> ").lower().strip() == "n":
            break
        else:
          print("Materia inserita non valida")
      except ValueError:
        print("Errore: Assicurati che il voto sia un numero valido.")
      except Exception as e:
        print(f"Errore nell'esecuzione: {e}")

    # Modifica un voto esistente
  
  #edit valutation
  def edit_valuation(self):
    # Mostra le materie
    while True:
      print("--- Lista Materie ---")
      for key, val in self.subject.items():
        print(f"{key}) {val}")
      try:
        # Chiedi all'utente di scegliere una materia
        subj = int(input("Inserisci numero materia da modificare ---> "))
        if subj in self.subject:
          materia = self.subject.get(subj)
          # Trova i voti per la materia scelta
          myDb = DbConnetion.db_connection(dbName)
          cursor = myDb.cursor()
          query = "SELECT id, voto FROM voti WHERE studente_id = %s AND materia = %s"
          cursor.execute(query, (self.id, materia))
          result = cursor.fetchall()

          if result:
            # Visualizza i voti per la materia
            print(f"--- Voti per {materia} ---")
            for voto_id, voto in result:
              print(f"ID: {voto_id}, Voto: {voto}")
            
            # Chiedi all'utente di scegliere un voto da modificare
            voto_id = int(input("Inserisci ID del voto da modificare ---> "))
            nuovo_voto = float(input(f"Inserisci nuovo voto per {materia} ---> "))
            
            # Modifica il voto nel database
            update_query = "UPDATE voti SET voto = %s WHERE id = %s AND studente_id = %s"
            cursor.execute(update_query, (nuovo_voto, voto_id, self.id))
            myDb.commit()
            print("Voto modificato con successo.")
          else:
              print(f"Nessun voto trovato per la materia {materia}.")
          break
        else:
          print("Materia inserita non valida.")
      except ValueError:
        print("Errore: Assicurati che il numero della materia e il voto siano validi.")
      except Exception as e:
        print(f"Errore nell'esecuzione: {e}")
    myDb.close()
    cursor.close()
  
  #delete valutation
  def delete_valuation(self):
    # Mostra le materie
    while True:
      print("--- Lista Materie ---")
      for key, val in self.subject.items():
        print(f"{key}) {val}")
      try:
        # Chiedi all'utente di scegliere una materia
        subj = int(input("Inserisci numero materia da cancellare ---> "))
        if subj in self.subject:
          materia = self.subject.get(subj)
          # Trova i voti per la materia scelta
          myDb = DbConnetion.db_connection(dbName)
          cursor = myDb.cursor()
          query = "SELECT id, voto FROM voti WHERE studente_id = %s AND materia = %s"
          cursor.execute(query, (self.id, materia))
          result = cursor.fetchall()

          if result:
            # Visualizza i voti per la materia
            print(f"--- Voti per {materia} ---")
            for voto_id, voto in result:
              print(f"ID: {voto_id}, Voto: {voto}")
            
            # Chiedi all'utente di scegliere un voto da cancellare
            voto_id = int(input("Inserisci ID del voto da cancellare ---> "))
            
            # Elimina il voto nel database
            delete_query = "DELETE FROM voti WHERE id = %s AND studente_id = %s"
            cursor.execute(delete_query, (voto_id, self.id))
            myDb.commit()
            print("Voto cancellato con successo.")
          else:
              print(f"Nessun voto trovato per la materia {materia}.")
          
          break
        else:
            print("Materia inserita non valida.")
      except ValueError:
          print("Errore: Assicurati che il numero della materia sia valido.")
      except Exception as e:
          print(f"Errore nell'esecuzione: {e}")
    cursor.close()
    myDb.close()


class Register():
  def __init__(self):
    # Dizionario che contiene tutti gli studenti (id: Student)
    self.student = self.load_all_students()
  
  #ricarica 
  def reload_info(self):
    # Ricarica gli studenti dopo l'inserimento
      self.student = self.load_all_students()
      
  # Funzione per verificare se un id esiste
  def student_exists(self, student_id):
    return any(student.id == student_id for student in self.student)
  
  #trova studente nel dizionario dall id
  def get_student_by_id(self, student_id):
    for student in self.student:
        if student.id == student_id:
            return student
    return None
  
  #get all student from db
  def load_all_students(self):
    myDb = DbConnetion.db_connection(dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT id, nome, cognome FROM studenti")
    result = cursor.fetchall()
    cursor.close()
    myDb.close()
    return [Student(*i) for i in result]

  # Stampa le informazioni di tutti gli studenti nel registro
  def print_all_students(self):
    print("--- Elenco degli studenti ---\n")
    for student in self.student:
        print(f"ID: {student.id}")
        print(f"Nome: {student.name}")
        print(f"Cognome: {student.surname}")
        print(f"Voti: {student.votes}")
        print("-" * 30)  # Linea di separazione tra ogni studente
        
  #aggiungi voto
  def add_Vote(self):
    try:
      print("--- Menu Inserimento Voto ---")
      idStudents = int(input("Inserisci id studente per modificare voto ---> "))
      if self.student_exists(idStudents):
        student = self.get_student_by_id(idStudents)
        student.add_valuation()
        self.reload_info()
      else:
        print("Studente non trovato")
    except Exception as e:
      print(e)
      
  #modifica voto
  def modify_Vote(self):
    try:
      print("--- Menu Modifica Studenti ---")
      idStudents = int(input("Inserisci id studente per modificare voto ---> "))
      if self.student_exists(idStudents):
        student = self.get_student_by_id(idStudents)
        student.edit_valuation()
        self.reload_info()
      else:
        print("Studente non trovato")
    except Exception as e:
      print(e)

  # Cancella un voto per uno studente
  def delete_Vote(self):
    try:
      print("--- Menu Eliminazione Voto ---")
      idStudents = int(input("Inserisci id studente per cancellare voto ---> "))
      if self.student_exists(idStudents):
        student = self.get_student_by_id(idStudents)
        student.delete_valuation()
        self.reload_info()
      else:
        print("Studente non trovato")
    except Exception as e:
      print(e)

# Aggiungi uno studente al registro
  def add_student(self):
    try:
      print("--- Menu Inserimento Studenti ---")
      nome = input("Inserisci il nome dello studente ---> ")
      cognome = input("Inserisci il cognome dello studente ---> ")
      myDb = DbConnetion.db_connection(dbName)
      cursor = myDb.cursor()
      query = "INSERT INTO studenti (nome, cognome) VALUES (%s, %s)"
      cursor.execute(query, (nome, cognome))
      myDb.commit()
      cursor.close()
      myDb.close()
      print("Studente aggiunto con successo.")
      self.reload_info()
    except Exception as e:
      print(f"Errore nell'aggiunta dello studente: {e}")

  # Elimina uno studente dal registro
  def delete_student(self):
    try:
      print("--- Menu Eliminazione Studenti ---")
      idStudents = int(input("Inserisci ID studente da eliminare ---> "))
      if self.student_exists(idStudents):
        myDb = DbConnetion.db_connection(dbName)
        cursor = myDb.cursor()
        query = "DELETE FROM studenti WHERE id = %s"
        cursor.execute(query, (idStudents,))
        myDb.commit()
        cursor.close()
        myDb.close()
        print(f"Studente con ID {idStudents} eliminato con successo.")
        self.reload_info()
      else:
        print("Studente non trovato.")
    except Exception as e:
      print(f"Errore nell'eliminazione dello studente: {e}")

# ---------- MAIN ----------
def main():
  # Crea un'istanza del registro studenti
  register = Register()
  while True:
    ch = int(input("--- Menu ---\n 1) Visualizza studenti\n 2) Aggiungi studenti \n 3) Elimina studente \n 4) Add vote \n 5) Modify vote \n 6) Delete vote \n 7) Exit \n ---> "))
    
    # Gestione delle opzioni del menu
    match ch:
      case 1:
        register.print_all_students()
      case 2:
        register.add_student()
      case 3:
        register.delete_student()
      case 4:
        register.add_Vote()
      case 5:
        register.modify_Vote()
      case 6:
        register.delete_Vote()
      case _: 
        print('Fine programma...')
        break

    # Chiede all'utente se vuole tornare al menu
    if input("Vuoi tornare al menu? s/n ---> ").strip().lower() == "n":
      break

#inizalizzazione programma
create()
main()