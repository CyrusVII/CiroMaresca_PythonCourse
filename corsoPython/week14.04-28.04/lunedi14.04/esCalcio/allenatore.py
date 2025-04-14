import membroSquadre as ms

class Allenatore(ms.MembroSquadre):
  def __init__(self, id, nome, eta, nome_squadra,anni_di_esperienza):
    super().__init__(id, nome, eta, nome_squadra)
    self.anni_di_esperienza = anni_di_esperienza
    
  def percAnni(self):
    bonus = min((self.anni_di_esperienza // 2) * 0.015, 0.15)
    return bonus