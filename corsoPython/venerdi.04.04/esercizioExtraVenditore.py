#implementare classe venditore che richieda x prodotti alla fabbrica la fabbrica puoi produre 10 prodotti al giorno
#import
import time

#classe prodotti
class Product:
  
  def __init__(self, name, pCost, pSell):
    self.name = name
    self.pCost = pCost
    self.pSell = pSell
    
  # Metodo per calcolare il profitto di un oggetto
  def calcolate_profict(self):
      return self.pSell - self.pCost
    
  #metodo per calcolare i giorni di produzione
  def day_production(self,day):
    return day // 10

#classe factory per gestire i prodotti
class Factory:
  
  def __init__(self):
    self.all_product = {
    1: Product("T-shirt", 5.00, 15.00),
    2: Product("Jeans", 12.00, 40.00),
    3: Product("Sneakers", 25.00, 70.00),
    4: Product("Jacket", 30.00, 100.00),
    5: Product("Cap", 3.00, 12.00),
    6: Product("Sunglasses", 7.00, 25.00),
    7: Product("Backpack", 10.00, 35.00),
    8: Product("Watch", 20.00, 60.00),
    9: Product("Scarf", 4.00, 18.00),
    10: Product("Gloves", 6.00, 20.00)
    }   
    
  # Metodo di stampa dei prodotti
  def print_all_product(self):
    print('--- Lista Prodotti ---')
    for key, val in self.all_product.items():
      product = val  # recuperiamo l'oggetto Product
      # Stampa dei dettagli del prodotto
      print(f"-----\n Id: {key} \n Name: {product.name}"
            f"\n Costo Produzione: {product.pCost} $ \n Prezzo di vendita: {product.pSell} $ \n Il margine di guadagno: {product.calcolate_profict()} $")

  # Def per vendere e restituire prodotti
  def sell_product(self):
    self.print_all_product()
    idProdOrder = int(input("Inserisi id del prodotto che vuoi ordinare ---> "))
    if idProdOrder in self.all_product:
      product = self.all_product[idProdOrder]
      quant = int(input("Inserisci quantita che vui ordinare ---> "))
      print(f"Per produrre {quant} pezzi di {product.name} ci sono voluti {product.day_production(quant)} giorni")
    else:
      print("Id non valido")

#classe main per la gestione del programma
class Venditore:
  def __init__(self):
    pass
  
  def menu(self):
    factory = Factory()
    print('Benvenuto venditore')
    while True:
      time.sleep(2)
      try:
        ch = int(input("--- Menu --- \n 1) Stampa lista prodotti \n 2) Compra prodotto \n---> "))
        match ch:
          case 1:
            factory.print_all_product()
          case 2:
            factory.sell_product()
      except ValueError:
        print("Per favore, inserisci un numero valido!")
        continue

#avvio programma
ven = Venditore()
ven.menu()
