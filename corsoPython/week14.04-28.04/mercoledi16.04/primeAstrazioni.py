# Importiamo il modulo abc per poter creare classi astratte
from abc import ABC, abstractmethod

# Creiamo una classe astratta chiamata Animale
# Una classe astratta è una classe che non può essere istanziata direttamente,
# serve come base per altre classi
class Animale(ABC):
    
    # Definiamo un metodo astratto chiamato muovi
    # I metodi astratti sono metodi che devono essere implementati dalle classi figlie
    @abstractmethod
    def muovi(self):
        pass  # 'pass' significa che non facciamo nulla qui; la logica sarà definita nelle sottoclassi

# Creiamo una classe chiamata Cane che eredita da Animale
class Cane(Animale):
    
    # Implementiamo il metodo muovi specifico per il Cane
    def muovi(self):
        print("Corro")  # Quando il metodo viene chiamato, il cane "corre"

# Creiamo una classe chiamata Pesce che eredita da Animale
class Pesce(Animale):
    
    # Implementiamo il metodo muovi specifico per il Pesce
    def muovi(self):
        print("Nuoto")  # Quando il metodo viene chiamato, il pesce "nuota"
