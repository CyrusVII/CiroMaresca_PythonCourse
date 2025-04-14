import membroSquadre as ms
class Assistente(ms.MembroSquadre):
  def __init__(self, id, nome, eta, nome_squadra,specializzazione,anni_di_esperienza):
    super().__init__(id, nome, eta, nome_squadra)
    self.specializzazione = specializzazione
    self.anni_di_esperienza = anni_di_esperienza
    
  def percBonus(self):
    # Base: ogni anno dà 0.005 (0.5%), massimo 5%
      bonus = min(self.anni_di_esperienza * 0.005, 0.05)
      # Specializzazione extra
      if self.specializzazione.lower() == "analista di gioco":
          bonus += 0.01  # +1% se analista
      elif self.specializzazione.lower() == "fisioterapista":
          bonus += 0.005  # +0.5% se fisio
      return bonus