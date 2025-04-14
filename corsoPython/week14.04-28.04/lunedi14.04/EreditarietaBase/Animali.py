#classe base
class Animali:
  def __init__(self,nome):
    self.nome = nome
    
  def parla(self):
    print(f"{self.nome} fa suono generico")

#classe derivata eredita da animali
class Cane(Animali):
  def parla(self):
    print(f"{self.nome} abbaia")
    
animale_generico = Animali("AnimaleGenerico")
cane = Cane("Fido")

animale_generico.parla()
cane.parla()
    
