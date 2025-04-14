#Classe MembroSquadra:
# Attributi: nome (stringa)
# età (intero)
# Metodi:
# descrivi() (stampa una descrizione generale del membro della squadra)

class MembroSquadre():
  def __init__(self,id,nome,eta,nome_squadra):
    self.id = id
    self.nome = nome
    self.eta = eta
    self.nome_squadra = nome_squadra
    self.nomeDb = "calcio"
    
  def print_data(self):
    return f"{self.nome}\n{self.eta}\n{self.nome_squadra}"