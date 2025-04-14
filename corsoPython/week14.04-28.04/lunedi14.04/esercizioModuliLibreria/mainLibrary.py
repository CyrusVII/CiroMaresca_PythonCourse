# Esercizio: Immagina di gestire una libreria. Crea due classi: Libro e Libreria.
# 1. La classe Libro dovrebbe avere gli attributi:
# 。 titolo
# 。 autore
# 。 isbn (numero identificativo unico per ogni libro)
# 2. Inoltre, dovrebbe avere un metodo descrizione() che restituisce una stringa che descrive il libro usando tutti e tre gli attributi.
# 3. La classe Libreria dovrebbe avere l'attributo:
# • catalogo (una lista che conterrà oggetti della classe Libro)
# 4. La classe Libreria dovrebbe avere i seguenti metodi:
# • aggiungi_libro(libro): che prende in input un oggetto della classe Libro e lo aggiunge al catalogo.
# • rimuovi_libro(isbn): che rimuove un libro dal catalogo in base al suo ISBN.
# • cerca_per_titolo(titolo): che restituisce una lista di libri che corrispondono al titolo dato.
# • mostra_catalogo(): che stampa una descrizione di tutti i libri presenti nel catalogo.

from library import Library 

def main():
    lib = Library()

    while True:
        print("\n----- MENU BIBLIOTECA -----")
        print("1. Aggiungi un libro")
        print("2. Cancella un libro")
        print("3. Cerca un libro per titolo")
        print("4. Mostra tutti i libri")
        print("5. Esci")

        try:
            scelta = int(input("Scegli un'opzione (1-5): "))
        except:
            print("Input non valido. Inserisci un numero tra 1 e 5.")
            continue

        match scelta:
            case 1:
                lib.create_book()
            case 2:
                lib.delete_book()
            case 3:
                lib.serch_book()
            case 4:
                lib.print_library()
            case 5:
                print("Uscita dal programma...")
                break
            case _:
                print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
