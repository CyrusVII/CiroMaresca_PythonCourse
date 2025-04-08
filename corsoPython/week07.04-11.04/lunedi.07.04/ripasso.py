cliente1 = {"nome":"tommaso"}
print(cliente1.get("via","dato non presente"))#per cercare una chiave e da un risultato
print(cliente1.get("nome","dato non presente"))#per cercare una chiave 
print(cliente1)
print(cliente1.setdefault("via","via pippo"))#setdefault se non trova il valore lo setta nel dizionario
print(cliente1)
print(cliente1.setdefault("via","via pippo"))#se c'e la chiava la restituisce
print(cliente1)

#list compretion
cliente1M = {k+"M":v+"M" for k,v in cliente1.items()}
print(cliente1M)

#comandi
print(f"Il max {max(cliente1)}")#prende l ultima chiava del dizionario

lista = ['zero','uno','due']
for i,val in enumerate(lista):
  print(f"Indice : {i}, valore:{val}")