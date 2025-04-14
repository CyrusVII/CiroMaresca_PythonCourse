class Book:
    def __init__(self, isbn, titolo, autore, pagine):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def print_book(self):
        return f"---\n isbn : {self.isbn} \n Titolo : {self.titolo} \n Autore : {self.autore} \n Pagine : {self.pagine}"