# Crea una classe Prodotto e una classe Magazzino.
# Classe Prodotto:
# Attributi: nome, prezzo, quantità
# Classe Magazzino:
# Attributo: prodotti (lista di oggetti Prodotto)
# Metodi:
# aggiungi_prodotto(prodotto)
# valore_totale() → calcola il valore totale del magazzino (somma di prezzo × quantità)
# cerca_prodotto(nome) → ritorna il prodotto se esiste, altrimenti un messaggio di errore
# Obiettivo: esercitarsi con gestione di liste, ricerca, moltiplicazioni e strutture condizionali.

import time

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def print_data(self):
        return f"Name : {self.name} / Price : {self.price}$ / Quantity : {self.quantity}"


class Magazine:
    def __init__(self):
        self.product = {}

    # Check if a product exists by name
    def check_if_product_exist(self, name):
        for product in self.product.values():
            if product.name == name:
                return True
        return False

    # Method for creating and adding a product
    def create_product(self):
        print("--- Add new product to magazine ---")
        while True:
            try:
                name = input('Type product name ---> ').lower().strip().capitalize()

                # If product already exists, raise error
                if self.check_if_product_exist(name):
                    raise ValueError("Product already exists!")

                price = float(input("Type the price ---> "))
                quantity = int(input("Type available quantity ---> "))

                prod = Product(name, price, quantity)

                # Generate a new ID
                new_id = max(self.product.keys(), default=0) + 1

                self.product[new_id] = prod
                print("--- Product added ---")
                break
            except ValueError as e:
                print(f"Invalid data: {e}. Please try again.\n")

    # Print all products
    def print_all_product(self):
        print("--- All Products --- ")
        for key, val in self.product.items():
            print(f"ID : {key} / ", val.print_data())

    # Calculate the total value of the magazine
    def calcolate_magazine_value(self):
        total = 0
        for val in self.product.values():
            total += (val.price * val.quantity)
        return total

# ---------- MAIN ----------
def main():
    # Create 2 test products
    p1 = Product("Salt", 2.5, 10)
    p2 = Product("Bread", 3, 22)

    # Create the magazine
    magazine = Magazine()

    # Add test products to the magazine
    magazine.product[1] = p1
    magazine.product[2] = p2

    while True:
      
        time.sleep(2)
        # Display menu
        print("\n--- Menu --- \n 1. Show all products \n 2. Add new product \n 3. Check if a product exists \n 4. Calculate total value of magazine \n 0. Exit")
        try:
            ch = int(input(" Choose an option ---> "))
            match ch:
                case 1:
                    magazine.print_all_product()
                case 2:
                    magazine.create_product()
                case 3:
                    name = input("Enter product name to check ---> ").lower().strip().capitalize()
                    exists = magazine.check_if_product_exist(name)
                    print("Product exists!" if exists else "Product not found.")
                case 4:
                    value = magazine.calcolate_magazine_value()
                    print(f"Total value of products in magazine: {value}$")
                case 0:
                    print("Exiting program...")
                    break
                case _:
                    print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Run the program
#main()


