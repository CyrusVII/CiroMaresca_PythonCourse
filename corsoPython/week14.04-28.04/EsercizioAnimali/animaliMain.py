# Esercizio Ereditarietà
# Creare una classe base Animale e diverse classi derivate che rappresentano diversi tipi di animali in uno zoo.
# Ogni classe derivata avrà attributi e metodi specifici che riflettono le caratteristiche e comportamenti unici degli animali che rappresentano.
# • Classe Animale:
# • Attributi:
# ■ nome (stringa che descrive il nome dell'animale)
# ■ eta (intero che rappresenta l'età dell'animale)
# 。 Metodi:
# ■ fai_suono(): un metodo che stampa un suono generico dell'animale.
# • Classi Figlie:
# • Creare almeno tre classi Figlie di Animale ES: Leone, Giraffa, e Pinguino. Ogni classe avrà attributi e metodi specifici:
# ■ Per esempio, la classe Leone potrebbe avere un metodo caccia() che stampa un messaggio su come il leone sta cacciando.

# Classe base
class Animale:
    def __init__(self, nome, eta):
      self.nome = nome
      self.eta = eta

    def fai_suono(self):
      print(f"{self.nome} emette un suono generico.")


# Classe figlia: Leone
class Leone(Animale):
    def __init__(self, nome, eta, branco):
      super().__init__(nome, eta)
      self.branco = branco  

    def fai_suono(self):
      print(f"{self.nome} ruggisce: ROAR!")

    def caccia(self):
      print(f"{self.nome} sta cacciando con il branco." if self.branco else f"{self.nome} caccia da solo.")


# Classe figlia: Giraffa
class Giraffa(Animale):
    def __init__(self, nome, eta, altezza):
      super().__init__(nome, eta)
      self.altezza = altezza 

    def fai_suono(self):
      print(f"{self.nome} emette un lieve muggito.")

    def mangia_foglie(self):
        print(f"{self.nome} mangia foglie dagli alberi alti grazie alla sua altezza di {self.altezza} metri.")


# Classe figlia: Pinguino
class Pinguino(Animale):
    def __init__(self, nome, eta, specie):
      super().__init__(nome, eta)
      self.specie = specie

    def fai_suono(self):
      print(f"{self.nome} fa: squawk squawk!")

    def nuota(self):
      print(f"{self.nome}, un pinguino della specie {self.specie}, sta nuotando agilmente nell'acqua.")

