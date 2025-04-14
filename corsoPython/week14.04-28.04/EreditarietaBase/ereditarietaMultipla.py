class Veicolo:
  def __init__(self, marca, modello):
    self.marca = marca
    self.modello = modello

  def mostra_informazioni(self):
    print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
  def __init__(self, dotazioni):
    self.dotazioni = dotazioni

  def mostra_dotazioni(self):
    print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

class AutomobiliSportiva(Veicolo, DotazioniSpeciali):
  def __init__(self, marca, modello, dotazioni, cavalli):
    #alternativa aa super per ereditarieta multipla
    Veicolo.__init__(self, marca, modello)
    DotazioniSpeciali.__init__(self, dotazioni)
    self.cavalli = cavalli

  def mostra_informazioni(self):
    super().mostra_informazioni()  # Chiama Veicolo.mostra_informazioni()
    print(f"Potenza: {self.cavalli} CV")
    self.mostra_dotazioni()

# Fuori dalle classi!
auto_sportiva = AutomobiliSportiva("Ferrari", "F8", ["ABS", "Controller"], 110)
auto_sportiva.mostra_informazioni()
