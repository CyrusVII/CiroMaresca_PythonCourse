import numpy as np

class Matrici:
    def __init__(self):
      self.matrice_1 = []
      self.matrice_2 = []
      self.somma = []
      self.sommaSpeciale = 0
    
    def crea_linspace(self):
      self.matrice_1 = np.linspace(0, 10, 50)
    
    def crea_random(self):
      self.matrice_2 = np.random.rand(50)
    
    def somma_elementi(self):
      if len(self.matrice_1) == 50 and len(self.matrice_2) == 50:
        self.somma = self.matrice_1 + self.matrice_2
      else:
        print("Devi prima creare entrambi gli array.")
    
    def somma_speciale(self):
      if self.somma.size > 0:
        self.sommaSpeciale = sum(x for x in self.somma if x > 5)
      else:
        print("Devi prima calcolare la somma dei due array.")
    
    def stampa(self):
      print("Matrice 1:", self.matrice_1)
      print("-----")
      print("Matrice 2:", self.matrice_2)
      print("-----")
      print("Somma:", self.somma)
      print("-----")
      print("Somma Speciale (elementi > 5):", self.sommaSpeciale)


def menu():
  print("\n-----\nSeleziona un'opzione:")
  print("1. Creiamo un array di 50 numeri equidistanti tra 0 e 10.")
  print("2. Array di 50 numeri casuali compresi tra 0 e 1.")
  print("3. Somma elemento per elemento dei due array.")
  print("4. Calcolo somma degli elementi del nuovo array maggiori di 5")
  print("5. Stampa tutto.")
  print("6. Esci.")
  
  scelta = int(input("---> "))
  print("-----\n")
  return scelta


def main():
  matrici = Matrici()
  
  while True:
    ch = menu()
    match ch:
      case 1:
        matrici.crea_linspace()
        print(matrici.matrice_1)
      case 2:
        matrici.crea_random()
        print(matrici.matrice_2)
      case 3:
        matrici.somma_elementi()
        print(matrici.somma)
      case 4:
        matrici.somma_speciale()
        print(matrici.sommaSpeciale)
      case 5:
        matrici.stampa()
      case 6:
        print("Abbandono programma....")
        break
      case _:
        print("Opzione non valida, riprova.")
        

if __name__ == "__main__":
    main()
