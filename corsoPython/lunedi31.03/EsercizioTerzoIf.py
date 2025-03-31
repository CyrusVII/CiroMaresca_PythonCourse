#Scrivi un programma che chiede all utente la sua eta.se l eta e inferiore a 18, il programma dovrebbe stampare "mi dispiace non uoi vedere questo film".
#Altrimenti stampa "puoi vedere questo file"

# age = int(input("Inserisci la tua eta: "))#prendo l eta
# print("mi dispiace non puoi vedere questo film" if age < 18 else "puoi vedere questo film") #if che stampa la condizione

#scrivi un programma che chiede all utente di inserire due numeri e un operazione da eseguire trra adizione sottrazione, moltiplicazione e divisione. il programma
#dovrebbe poi eseguire l operazione e stampare il risultato. tuttavia se l utente tenta di dividere per zero il programma dovrebbe stampare errore divisione per zero
#se l operazione scelta non e valida scrivere operazione non valida

#try catch gestione errori
try:
    # Richiesta dati dall'utente
    print("\n--- MENU ---")
    print("1. Addizione (+)")
    print("2. Sottrazione (-)")
    print("3. Divisione (/)")
    print("4. Moltiplicazione (*)")
    print("5. Esci")
    print("-------")
    
    scelta = input("Inserisci la scelta: ").strip()
    operazioni = {"1": "+", "2": "-", "3": "/", "4": "*"}#mappa operazioni
    op = operazioni.get(scelta)
    
    #if controllo scelta e operazione
    if scelta == "5":
        print("Uscita dal programma.")
    elif not op:
        print("Operazione non valida. Usa solo 1, 2, 3, 4 o 5.")
    else:
        n1 = int(input("Inserisci valore N1: "))
        n2 = int(input("Inserisci valore N2: "))
        print("-------")
        # Match per controllare la scelta dell'utente
        match op:
            case "+":
                print(f"Risultato addizione: {n1 + n2}")
            case "-":
                print(f"Risultato sottrazione: {n1 - n2}")
            case "/":
                if n2 == 0:
                    print("Errore: Impossibile dividere per 0")
                else:
                    print(f"Risultato divisione: {n1 / n2}")
            case "*":
                print(f"Risultato moltiplicazione: {n1 * n2}")
except ValueError:  # ValueError per catturare gli errori in input
    print("Errore: Inserisci solo numeri validi per N1 e N2!")