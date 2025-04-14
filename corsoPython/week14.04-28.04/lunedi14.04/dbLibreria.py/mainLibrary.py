
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
