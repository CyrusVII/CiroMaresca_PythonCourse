import membroSquadre as ms
class Giocatore(ms.MembroSquadre):
  def __init__(self,id, nome, eta, nome_squadra,ruolo,numero_maglia):
    super().__init__(id,nome, eta, nome_squadra)
    self.ruolo = ruolo
    self.numero_maglia = numero_maglia
    
    
  
