from abc import ABC, abstractmethod

# Classe astratta Forma: definisce un'interfaccia per forme geometriche
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

# Classe concreta Rettangolo che eredita da Forma
class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza

    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)

# f = Forma()  # Errore: non si può istanziare una classe astratta
r = Rettangolo(5, 10)
print(r.area())       # Output: 50
print(r.perimetro())  # Output: 30

