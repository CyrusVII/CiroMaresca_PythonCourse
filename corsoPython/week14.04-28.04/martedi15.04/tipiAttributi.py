#attributo privato __attrributo
#attribupo protetto e giusto una convenzione per definire un dato che puo essere usato nella classe e nelle sue sotto classi _attrtributo
class Computer:
    def __init__(self):
        self.__processore = "Intel i5" #attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self,processore):
        self.__processore = processore
        
pc = Computer()
print(pc.get_processore())
#accede all attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5")
#modifica l attributo privato tramite il setter
print(pc.get_processore())

#variabile globale
numero = 10

def funzione_esterna():
    #variabile locale nella funzione esterna
    numero = 5
    print("numero dento funzione_esterna ",numero)
    
    def funzione_interna():
        #metodo nonlocale per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print(f"Numero dentro funzione_nterna (nonlocal): {numero}")
    funzione_interna()
print(f"numero nel main (global): {numero}")
funzione_esterna()
print(f"numero nel main dopo chiamata (global non cambiato): {numero}")