#python e un linguaggio di programmazione iterpretato,orientato agli ogetti, dinamico e ad alto livello. rilasciato nel 91.
#ideatore Guido Van Rossum

print("hello world") #classica stampa

#dichiarazione base var
name = "alice"
age = 25
#il print puo essere fatto inpiu modi con i + , o con l f
print(f"il mio nome e {name}, e ho {age} anni \n ------------")

#prendiamo invece l input dell utente
name1 = input("Insert name: ")
age1 = int(input("insert age: "))
print(f"il mio nome e {name1}, e ho {age1} anni")

#prendere singola lettera di un str
s = "prova mondo"
print(s[3]) #prende la terza lettera della stringa
print(len(s)) #per vedere la lunghezza di un str tipo length
print(s.upper()) #per fare tutto in maiuscolo
print(s.lower())#tutto minuscolo
print(s.split(" "))#crea un array in base allo split
print(s.replace('prova','camicia'))#cambia un dato presente con uno scelto da te