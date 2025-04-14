import DbConnetion as db

# Classe base
class Animale:
  def __init__(self, nome, eta):
    self.nome = nome
    self.eta = eta
    self.create_table()

  def create_table(self):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS animali (
        id INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(255) NOT NULL,
        nome VARCHAR(255) NOT NULL,
        eta INT,
        vario VARCHAR(255)
    )
    ''')
  
  def fai_suono(self):
    print(f"{self.nome} emette un suono generico.")
  
  def inserisci_db(self):
    tipo = "non specificato"
    cursor.execute('''
      INSERT INTO animali (tipo, nome, eta,vario)
      VALUES (%s, %s, %s, %s)
    ''', (tipo, self.nome, self.eta,None))
    myDb.commit()
    print(f"{self.nome} è stato inserito nel database come {tipo}.") 

# Classe figlia: Leone
class Leone(Animale):
  def __init__(self, nome, eta, branco):
    super().__init__(nome, eta)
    self.branco = branco  

  def fai_suono(self):
    print(f"{self.nome} ruggisce: ROAR!")

  def caccia(self):
    print(f"{self.nome} sta cacciando con il branco." if self.branco else f"{self.nome} caccia da solo.")
    
  def inserisci_db(self):
    tipo = "Leone"
    cursor.execute('''
      INSERT INTO animali (tipo, nome, eta, vario)
      VALUES (%s, %s, %s, %s)
    ''', (tipo, self.nome, self.eta, self.branco))
    myDb.commit()
    print(f"{self.nome} è stato inserito nel database come {tipo}.") 

# Classe figlia: Giraffa
class Giraffa(Animale):
  def __init__(self, nome, eta, altezza):
    super().__init__(nome, eta)
    self.altezza = altezza 

  def fai_suono(self):
    print(f"{self.nome} emette un lieve muggito.")

  def mangia_foglie(self):
      print(f"{self.nome} mangia foglie dagli alberi alti grazie alla sua altezza di {self.altezza} metri.")
      
  def inserisci_db(self):
    tipo = "Giraffa"
    cursor.execute('''
      INSERT INTO animali (tipo, nome, eta, vario)
      VALUES (%s, %s, %s, %s)
    ''', (tipo, self.nome, self.eta, self.altezza))
    myDb.commit()
    print(f"{self.nome} è stato inserito nel database come {tipo}.") 

# Classe figlia: Pinguino
class Pinguino(Animale):
  def __init__(self, nome, eta, specie):
    super().__init__(nome, eta)
    self.specie = specie

  def fai_suono(self):
    print(f"{self.nome} fa: squawk squawk!")

  def nuota(self):
    print(f"{self.nome}, un pinguino della specie {self.specie}, sta nuotando agilmente nell'acqua.")
    
  def inserisci_db(self):
    tipo = "Pinguino"
    cursor.execute('''
      INSERT INTO animali (tipo, nome, eta, vario)
      VALUES (%s, %s, %s, %s)
    ''', (tipo, self.nome, self.eta, self.specie))
    myDb.commit()
    print(f"{self.nome} è stato inserito nel database come {tipo}.") 

#connesione db
myDb = db.db_connection('Animali')
cursor = myDb.cursor()

#test
simba = Leone("Simba", 5, branco=True)
simba.inserisci_db()
pingu = Pinguino("Pingu",5,"bianco")
pingu.inserisci_db()

#chiusura connesione db
cursor.close()
myDb.close()