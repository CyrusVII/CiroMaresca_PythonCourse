#Scrivi un programma che chiede all utente la sua eta.se l eta e inferiore a 18, il programma dovrebbe stampare "mi dispiace non uoi vedere questo film".
#Altrimenti stampa "puoi vedere questo file"

# age = int(input("Inserisci la tua eta: "))#prendo l eta
# print("mi dispiace non puoi vedere questo film" if age < 18 else "puoi vedere questo film") #if che stampa la condizione

#scrivi un programma che chiede all utente di inserire due numeri e un operazione da eseguire trra adizione sottrazione, moltiplicazione e divisione. il programma
#dovrebbe poi eseguire l operazione e stampare il risultato. tuttavia se l utente tenta di dividere per zero il programma dovrebbe stampare errore divisione per zero
#se l operazione scelta non e valida scrivere operazione non valida

op = input("inserisci l operazione (+ - / *): ").lower().strip()
n1 = int(input("Inserisci valore N1: "))
n2 = int(input("Inserisci valore N2: "))
match op:
  case "+":
    print(f"Risultato addizione: {n1+n2}")
  case "-":
    print(f"Risultato sottrazione: {n1+n2}")
  case "/":
    if(n2 == 0):
      print("Impossibile dividere per 0")
    else:
      print(f"Risultato divisione: {n1/n2}")
  case "*":
      print(f"Risultato moltiplicazione: {n1*n2}")