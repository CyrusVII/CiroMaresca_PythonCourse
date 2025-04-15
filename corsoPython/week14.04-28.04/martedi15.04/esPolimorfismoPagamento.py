# creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. 
# Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i 
# loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe
# base.
# 1. Classe Metodo Pagamento:
# Metodi:
# ■ effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare. 2. Classi Derivate:
# • CartaDiCredito:
# ■ Metodi come effettua_pagamento (importo) che simula un pagamento tramite carta di credito.
# • PayPal:
# Metodi come effettua_pagamento (importo) che simula un pagamento tramite PayPal. BonificoBancario:
# ■ Metodi come effettua_pagamento (importo) che simula un pagamento tramite bonifico bancario.
# 3. GestorePagamenti:
# • Una classe che usa un'istanza di Metodo Pagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.

# Classe base che definisce l'interfaccia comune per tutti i metodi di pagamento
class MetodoPagamento:
    def effettua_pagamento(self, importo):
        raise NotImplementedError("Questo metodo deve essere implementato dalla sottoclasse") #lancio un errore

# Sottoclasse: Carta di credito
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self, importo):
        commissione = importo * 0.05  
        print(f"Pagamento di {importo}€ + 5% di commissione ({commissione:.2f}€): Totale pagato {importo + commissione:.2f}€ con Carta di Credito.")

# Sottoclasse: PayPal
class PayPal(MetodoPagamento):
    def effettua_pagamento(self, importo):
        commissione = importo * 0.02  
        print(f"Pagamento di {importo}€ + 2% di commissione ({commissione:.2f}€): Totale pagato {importo + commissione:.2f}€ con PayPal.")

# Sottoclasse: Bonifico Bancario
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo):
        commissione = importo * 0.04  
        print(f"Pagamento di {importo}€ + 4% di commissione ({commissione:.2f}€): Totale pagato {importo + commissione:.2f}€ con Bonifico.")

# Classe che gestisce i pagamenti, non importa quale metodo specifico viene usato
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.metodo_pagamento = metodo_pagamento

    def paga(self, importo):
        self.metodo_pagamento.effettua_pagamento(importo)

#funzione main per avvio del programma
import random
def main():
    while True:
        try:
            ch = int(input('scegli metodo di pagamento \n 1) Carta (5%) \n 2) PayPal (2%) \n 3) Bonifico (4%) \n ---> '))
            obj = None
            match ch:
                case 1:
                    obj = CartaDiCredito()
                case 2:
                    obj = PayPal()
                case 3:
                    obj = BonificoBancario()
                case _:
                    print("Scelta non valida")
            if obj:
                gp = GestorePagamenti(obj)
                gp.paga(random.randint(100, 1000))
                break
        except:
            print("input non valido")

# Avvia il programma
if __name__ == "__main__":
    main()

