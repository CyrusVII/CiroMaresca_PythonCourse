# Esercizio 1 (Facile):
# Crea una classe chiamata Punto. Questa classe dovrebbe avere:
# Due attributi: x e y, per rappresentare le coordinate del punto nel piano. Un metodo muovi che prenda in input un valore per dx e un valore per dy e 
# modifichi le coordinate del punto di questi valori.
# Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
# piano.



import math  # Importiamo la libreria per usare sqrt()

class Punto:
    def __init__(self, x, y):
        #Inizializza un punto con coordinate (x, y).
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        #Sposta il punto di dx e dy lungo gli assi x e y.
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):
        #Restituisce la distanza del punto dall'origine (0,0).
        return math.sqrt(self.x ** 2 + self.y ** 2) #math.sqrt() per calcolare la radice quadrata.

# Test della classe
# p = Punto(3, 4)
# print(f"Coordinate iniziali: ({p.x}, {p.y})")

# p.muovi(1, -2)
# print(f"Dopo lo spostamento: ({p.x}, {p.y})")

# distanza = p.distanza_da_origine()
# print(f"Distanza dall'origine: {distanza}")

# Esercizio 2 (Facile):
# Crea una classe chiamata Libro. Questa classe dovrebbe avere:
# Tre attributi: titolo, autore e pagine.
# Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".

class Libro:
  def __init__(self,titolo,autore,pagine):
      self.titolo = titolo
      self.autore = autore
      self.pagine = pagine
      
  def descrizione(self):
    return f"Il libro e {self.titolo} e stato scritto da {self.autore} a {self.pagine} pagine"
    
#inizializzo e provo
libro = Libro('La programmazione di Mirko','Mirko',22)
print(libro.descrizione())
