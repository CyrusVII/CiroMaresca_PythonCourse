# Esercizio 2 (Facile):
# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

class Libro:
  def __init__(self,titolo,autore,pagine):
      self.titolo = titolo
      self.autore = autore
      self.pagine = pagine
      
  def descrizione(self):
    return f"Il libro e {self.titolo} e stato scritto da {self.autore} a {self.pagine} pagine"
    
#inizializzo e provo
libro = Libro('La programmazione di Mirko','Mirko',22)
print(libro.descrizione())