# 3. La classe Libreria dovrebbe avere l'attributo:
# • catalogo (una lista che conterrà oggetti della classe Libro)
# 4. La classe Libreria dovrebbe avere i seguenti metodi:
# • aggiungi_libro(libro): che prende in input un oggetto della classe Libro e lo aggiunge al catalogo.
# • rimuovi_libro(isbn): che rimuove un libro dal catalogo in base al suo ISBN.
# • cerca_per_titolo(titolo): che restituisce una lista di libri che corrispondono al titolo dato.
# • mostra_catalogo(): che stampa una descrizione di tutti i libri presenti nel catalogo.
import book 

class Library:
  
  def __init__(self):
    self.all_books = {}  # Dizionario: isbn -> libro

  def isbn_controller(self, isbn):
    return isbn in self.all_books

  def create_book(self):
    while True:
      try:
        while True:
          isbn = int(input("Inserisci codice identificativo (ISBN): "))
          if not self.isbn_controller(isbn):
            break
          print("ISBN già presente, riprova.")
      except:
          print("Dato inserito non valido, riprova.")  # fine controllo isbn

      titolo = input('Inserisci titolo: ').lower().strip().capitalize()
      autore = input('Inserisci autore: ')

      try:
        while True:
          nPag = int(input('Inserisci numero di pagine: '))
          break
      except:
        print("Dato inserito non valido, riprova.")  # fine convalida pagine

      l = book.Book(titolo, autore, nPag, isbn)  # Passiamo anche l'isbn
      self.add_book(l, isbn)

      if input("Vuoi aggiungere ancora un libro? (s/n) ---> ").lower().strip() == 'n':
        break

  def add_book(self, l, isbn):
    self.all_books[isbn] = l

  def delete_book(self):
    try:
      isbn = int(input("Inserisci codice isbn per cancellare il libro : "))
      if self.isbn_controller(isbn):
        self.all_books.pop(isbn)
      else:
        print("Libro non trovato")
    except:
      print("input non valido")
  
  def serch_book(self):
    title = input("Inserisci titolo libro").lower().strip()
    print("--- Libri con questo titolo ---")
    for val in self.all_books.values():
      if title == val.titolo.lower():
        print(val.print_book())
        break
      

  def print_library(self):
    for isbn, libro in self.all_books.items():
      print(f"{libro.print_book()}")
