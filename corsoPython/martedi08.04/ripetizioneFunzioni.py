# def funzione(*args):
#   print(type(args))#args trasforma il valore in una tupla in modo da poter passare alla funzione x variabili
#   print(args[0]+args[2])
#   for el in args:
#     print(el)
    
# funzione(10,11,12)

# def funzione(**args):#col doppio asterisco
#     print(args)#mi crea una mappa con i valori passati
    
# funzione(uno=10,due=11,tre=12)

# eta = 28
# def funzione():
#   global eta #cosi facendo posso prendere una variabile creata al di fuori della funzione
#   eta += 1
#print(eta)
  
  
# lista = [1, 2, 3, 4, 5]
# def funz(a):
#   return a * 2

# lista = [funz(i) for i in lista]
# print(lista)

# lista = [1, 2, 3, 4, 5]
# def funz(a):
#   return a * 2
# lista = list(map(funz,lista))
# print(lista)

# lista = [1, 2, 3, 4, 5]
# def pari(a):
#   return a%2==0
# for i in lista:
#   if not pari(i):
#     lista.pop(i)
# print(lista)

lista = [1, 2, 3, 4, 5]
def pari(a):
  return a%2==0
lista2 = list(filter(pari,lista))#filtra tramite la funzione
print(lista2)