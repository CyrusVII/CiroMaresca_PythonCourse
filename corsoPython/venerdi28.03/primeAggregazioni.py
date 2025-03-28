#list
#x = ["x","y","z"]
# x.append(6)#per inserire un elemento nella lista
# x.insert(0, 0)#per inserire un elemento in una posizione specifica prima posizione poi elemento
# x.remove(3)#per rimuvere un elemnto che e presente nella lista
# x.sort serve per riordinare la lista dal piu piccolo al piu grande o alfabetico
# x.extend viene usata per aggiungere gli elementi di un altra lista all interno di questa
# x.pop() rimuovo l ultimo elemento della lista o l indice specificato x.pop(1)
# x.clear()#per pulire la lista da tutti glie elementi
# x.revers riordina la lista al contrario
# print(1 in x)#un espressione boolean per controllare se un valore e nella lista
# len(x)#per sapoere quanti elementi abbiamo nella lista
numbers = [1,2,3,4,5]
name = ["Bob","Alice","Charlie"]
misto = [1,"due",True,4.5]

#accedo a un elemento della lista tramite indice
print(f"{numbers[0]} print numero nella lista numbers")
print(f"{len(name)} size lista name")
numbers[2] = 10 #modifica del valore alla posizione x con nuovo valore
print(f"{numbers} lista numbers aggiornata")
print(f"3 c'e in numbers? {3 in numbers}")#controlliamo se il valore e presente nella lista restituisce boolean
print(f"lista nomi non ordinata \n {name} \n ordinata: \n {sorted(name)}")
misto.remove("due")
print(misto)

