#1. La classe Libro dovrebbe avere gli attributi:
# 。 titolo
# 。 autore
# 。 isbn (numero identificativo unico per ogni libro)
# 2. Inoltre, dovrebbe avere un metodo descrizione() che restituisce una stringa che descrive il libro usando tutti e tre gli attributi.

class Book:
  def __init__(self,isbn,titolo,autore,pagine):
      self.isbn = isbn
      self.titolo = titolo
      self.autore = autore
      self.pagine = pagine
      
  def print_book(self):
    return f"----- \n isbn : {self.isbn} \n Titolo : {self.titolo} \n Autore : {self.autore} \n pagine : {self.pagine}"