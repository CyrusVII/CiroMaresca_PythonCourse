class Libro:
  def __init__(self,titolo,autore,pagine):
      self.titolo = titolo
      self.autore = autore
      self.pagine = pagine
      
  def descrizione(self):
    return f"Il libro e {self.titolo} e stato scritto da {self.autore} a {self.pagine} pagine"
  

class Library:
    
    def __init__(self):
      self.all_book = []
    
    def crea_libro(self):
      while True:
        titolo = input('inserisci titolo: ')
        autore = input('inserisci autor: ')
        nPag = int(input('inserisci pagine: '))
        l = Libro(titolo,autore,nPag)
        self.aggiungi_libro(l)
        if input("Vuoi aggingere ancora un libro? (s/n) ---> ").lower().strip() == 'n':
            break
          
    def aggiungi_libro(self,l):
      self.all_book.append(l)
      
    def print_library(self):
      for i in self.all_book:
        print(i.descrizione())
      
l = Library()
l.crea_libro()
l.print_library()