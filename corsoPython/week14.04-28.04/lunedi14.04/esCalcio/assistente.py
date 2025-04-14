import membroSquadre as ms
class Assistente(ms.MembroSquadre):
  def __init__(self, id, nome, eta, nome_squadra,specializzazione,anni_di_esperienza):
    super().__init__(id, nome, eta, nome_squadra)
    self.specializzazione = specializzazione
    self.anni_di_esperienza = anni_di_esperienza