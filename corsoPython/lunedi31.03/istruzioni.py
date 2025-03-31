#come istruzioni abbiamo il break che viene utilizzato per interrompere l'esecuzione di un ciclo in anticipo
# numeri = [1,2,3,4,5]

# for numero in numeri:
#   if numero == 3:
#     break
#   print(numero)
  
#continue viene utilizzato per saltare il resto del blocco di codice all interno di un ciclo e passare alla prossima iterazione
# numeri = [1,2,3,4,5]

# for numero in numeri:
#   if numero == 3:
#     continue
#   print(numero)
  
#pass viene utilizzato quando si desidera eseguire alcuna azione all interno di un ciclo
# for i in range(5):
#   if i == 3:
#     pass
#   print(i)

#riempie velocemente una lista
numeri = [*range(1,11)]
print(numeri)