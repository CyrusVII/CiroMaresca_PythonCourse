# Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari tipi di prodotti. 
# Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti. 
# Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
# 1. Classe Prodotto:
# • Attributi:
# ■ nome (stringa che descrive il nome del prodotto)
# costo_produzione (costo per produrre il prodotto)
# • prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
# • Metodi:
# calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione. 2. Classi parallele:
# • Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
# Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
# 3. Classe Fabbrica:
# • Attributi:
# ■ inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino. 。 Metodi:
# aggiungi prodotto: aggiunge prodotti all'inventario.
# ■ vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
# ■resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.

#import
import time

#classe prodotti
class Product:
  
  def __init__(self, name, pQuantity, pCost, pSell):
    self.name = name
    self.pQuantity = pQuantity
    self.pCost = pCost
    self.pSell = pSell
    
  # Metodo per calcolare il profitto di un oggetto
  def calcolate_profict(self):
      return self.pSell - self.pCost

#classe che estende prodotto elettronica
class Elettronica(Product):
  
  def __init__(self, name, pQuantity, pCost, pSell, garanzia):
    # Chiamata al costruttore della classe base (Product)
    super().__init__(name, pQuantity, pCost, pSell)
    self.garanzia = garanzia  # Attributo specifico per Elettronica
  
  # Metodo per visualizzare le informazioni sul prodotto elettronico
  def print_info(self):
    print(f" Garanzia: {self.garanzia} anni")

#classe che estende prodotto abbigliamento
class Abbigliamento(Product):
  
  def __init__(self, name, pQuantity, pCost, pSell, materiale):
    # Chiamata al costruttore della classe base (Product)
    super().__init__(name, pQuantity, pCost, pSell)
    self.materiale = materiale  # Attributo specifico per Abbigliamento
  
  # Metodo per visualizzare le informazioni sul prodotto di abbigliamento
  def print_info(self):
    print(f" Materiale: {self.materiale}")

#classe factory per gestire i prodotti
class Factory:
  
  def __init__(self):
    self.all_product = {}
    
  # Metodo di stampa dei prodotti
  def print_all_product(self):
    print('--- Lista Prodotti ---')
    for key, val in self.all_product.items():
      product = val['product']  # recuperiamo l'oggetto Product
      # Stampa dei dettagli del prodotto
      print(f"-----\n Id: {key} \n Name: {product.name} \n Quantita: {product.pQuantity} "
            f"\n Costo Produzione: {product.pCost} $ \n Prezzo di vendita: {product.pSell} $ \n Il margine di guadagno: {product.calcolate_profict()} $")
      
      # Stampa le informazioni specifiche per ogni tipo di prodotto
      if isinstance(product, Elettronica):
        product.print_info()  # Stampa garanzia
      elif isinstance(product, Abbigliamento):
        product.print_info()  # Stampa materiale
    print('-----')  # print decorativo
  
  # Metodo per aggiungere prodotti al dizionario
  def add_product(self):
    while True:
      try:
        # Chiedi all'utente di scegliere il tipo di prodotto
        category = input('Inserisci la categoria del prodotto (Elettronica/Abbigliamento) ---> ').lower()
        
        # Chiedi all'utente di inserire i dettagli del prodotto
        name = input('Inserisci il nome del prodotto ---> ')
        pQ = int(input('Inserisci la quantità del prodotto ---> '))
        prodPrice = float(input('Inserisci il costo di produzione ---> '))
        sellPrice = float(input('Inserisci il prezzo di vendita ---> '))
        
        # Seleziona l'ID per il prodotto
        idKey = max(self.all_product.keys()) + 1 if self.all_product else 1
        
      except ValueError:
        print("Per favore, inserisci un numero valido!")
        continue
        
      # Aggiungi il prodotto basato sulla categoria selezionata
      if category == "elettronica":
        garanzia = int(input('Inserisci la durata della garanzia in anni ---> '))
        product = Elettronica(name, pQ, prodPrice, sellPrice, garanzia)
      elif category == "abbigliamento":
        materiale = input('Inserisci il materiale dell\'abbigliamento ---> ')
        product = Abbigliamento(name, pQ, prodPrice, sellPrice, materiale)
      else:
        print("Categoria non valida. Puoi scegliere tra 'Elettronica' o 'Abbigliamento'.")
        continue
      
      # Aggiungi il prodotto nel dizionario
      self.all_product[idKey] = {'product': product}

      print('Prodotto aggiunto alla lista...')
      
      # Chiedi se l'utente vuole aggiungere altri prodotti
      if input("Vuoi aggiungere altri prodotti (s/n) ---> ").lower().strip() != 's':
        break
    
    # Stampa la lista aggiornata dei prodotti
    self.print_all_product()

  # Metodo per togliere un prodotto
  def delete_product(self):
    while True:
      try:
        idKey = int(input("Inserisci la chiave del prodotto da togliere ---> "))
        if idKey in self.all_product:
          del self.all_product[idKey]
          print('Prodotto rimosso')
        else:
          print('Chiave prodotto inesistente')
      except ValueError:
        print("Per favore, inserisci un numero valido!")
        continue
      
      if input("Vuoi togliere un altro prodotto (s/n) ---> ").lower().strip() != 's':
        break
    
    self.print_all_product()
  
  # Def per prendere id prodotto dall'utente
  def take_product_id(self): 
    try: 
        return int(input("Id del prodotto da acquistare ---> "))
    except ValueError:
      print("Per favore, inserisci un numero valido!")
      
  # Def per vendere e restituire prodotti
  def sell_back_product(self):
    self.print_all_product()
    id = self.take_product_id()
    if id in self.all_product:
      ch = int(input("Premi - 1) Comprare - 2) Restituire ---> "))
      quan = int(input("Inserisci la quantità ---> "))
      product = self.all_product[id]['product']
      match ch:
        case 1:
          if product.pQuantity >= quan:
            product.pQuantity -= quan
            print(f"Venduti {quan} pezzi di {product.name}.")
          else:
            print(f"Mi dispiace, ma questo prodotto ha solo {product.pQuantity} pezzi disponibili.")
        case 2:
          product.pQuantity += quan
          print(f"Restituiti {quan} pezzi di {product.name}.")
        case _:
          print("Scelta non valida...")
    else:
      print("Id non valido")

#classe main per la gestione del programma
class Main:
  def __init__(self):
    pass
  
  def menu(self):
    factory = Factory()
    while True:
      time.sleep(2)
      try:
        ch = int(input("--- Menu --- \n 1) Stampa lista prodotti \n 2) Aggiungi Prodotto \n 3) Compra prodotto o Restituisci prodotto \n 4) Cancella prodotto \n ---> "))
        match ch:
          case 1:
            factory.print_all_product()
          case 2:
            factory.add_product()
          case 3:
            factory.sell_back_product()
          case 4:
            factory.delete_product()
      except ValueError:
        print("Per favore, inserisci un numero valido!")
        continue

#avvio programma
main = Main()
main.menu()

