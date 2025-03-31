#Scrivi un programma che chiede all utente la sua eta.se l eta e inferiore a 18, il programma dovrebbe stampare "mi dispiace non uoi vedere questo film".
#Altrimenti stampa "puoi vedere questo file"

age = int(input("Inserisci la tua eta"))#prendo l eta
print("mi dispiace non puoi vedere questo film" if age < 18 else "puoi vedere questo film") #if che stampa la condizione

#scrivi un programma che chiede all utente di inserire due numeri e un operazione da