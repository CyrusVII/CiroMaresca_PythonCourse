def esempio_basilare():
    """
    Legge due numeri da input e ne stampa la somma.
    Se si verifica *qualsiasi* errore (input non numerico, EOF, ecc.), 
    stampa un messaggio generico.
    """
    try:
        a = int(input("Inserisci il primo numero: "))
        b = int(input("Inserisci il secondo numero: "))
        print(f"La somma è: {a + b}")
    except Exception as e:
        # Cattura tutte le eccezioni ereditate da Exception
        print(f"Errore generico: {e}")
    else:
        print("Vado solo se non ci sono errori")
    finally:
        print("Vado sempre")

if __name__ == "__main__":
    esempio_basilare()
