import Book as b
import DbConnetion as dc

class Library:
  def __init__(self):
    self.dbName = "library"
    self.create_table()

  def create_table(self):
      myDb = dc.db_connection(self.dbName)
      cursor = myDb.cursor()
      query = '''
      CREATE TABLE IF NOT EXISTS books (
          isbn INTEGER PRIMARY KEY,
          titolo TEXT NOT NULL,
          autore TEXT NOT NULL,
          pagine INTEGER NOT NULL
      );
      '''
      cursor.execute(query)
      myDb.commit()
      cursor.close()
      myDb.close()
      print("db creato")

  def isbn_controller(self, isbn):
    print(f"Controllo ISBN: {isbn}")
    myDb = dc.db_connection(self.dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT 1 FROM books WHERE isbn = %s", (isbn,))
    result = cursor.fetchone()
    cursor.close()
    myDb.close()
    return result is not None

  def create_book(self):
    while True:
      while True:
        try:
          isbn = int(input("Inserisci codice identificativo (ISBN): "))
          if not self.isbn_controller(isbn):
            break
          print("ISBN già presente, riprova.")
        except:
          print("Dato inserito non valido, riprova.")

      titolo = input('Inserisci titolo: ').lower().strip().capitalize()
      autore = input('Inserisci autore: ')

      while True:
        try:
          nPag = int(input('Inserisci numero di pagine: '))
          break
        except:
            print("Dato inserito non valido, riprova.")

      myDb = dc.db_connection(self.dbName)
      cursor = myDb.cursor()
      cursor.execute(
        "INSERT INTO books (isbn, titolo, autore, pagine) VALUES (%s, %s, %s, %s)",
        (isbn, titolo, autore, nPag)
      )
      myDb.commit()
      cursor.close()
      myDb.close()

      print("Libro aggiunto con successo.")

      if input("Vuoi aggiungere ancora un libro? (s/n) ---> ").lower().strip() == 'n':
        break

  def delete_book(self):
    try:
      isbn = int(input("Inserisci codice ISBN per cancellare il libro: "))
      if self.isbn_controller(isbn):
        myDb = dc.db_connection(self.dbName)
        cursor = myDb.cursor()
        cursor.execute("DELETE FROM books WHERE isbn = %s", (isbn,))
        myDb.commit()
        cursor.close()
        myDb.close()
        print("Libro cancellato.")
      else:
        print("Libro non trovato.")
    except ValueError:
      print("Input non valido.")

  def serch_book(self):
    title = input("Inserisci titolo libro ---> ").lower().strip()
    myDb = dc.db_connection(self.dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT * FROM books WHERE LOWER(titolo) = %s", (title,))
    results = cursor.fetchall()
    cursor.close()
    myDb.close()

    if results:
      print("--- Libri con questo titolo ---")
      for row in results:
        libro = b.Book(*row)
        print(libro.print_book())
    else:
      print("Nessun libro trovato con questo titolo.")

  def print_library(self):
    myDb = dc.db_connection(self.dbName)
    cursor = myDb.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    myDb.close()

    print("--- La libreria ---")
    for book in books:
      libro = b.Book(*book)
      print(libro.print_book())
