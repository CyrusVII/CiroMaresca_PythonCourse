import tkinter as tk
import random
import time
import pandas as pd

# --- CONFIG ---
GRID_SIZE = 2  # 2x2 = 4 carte
CARDS = ['🐶', '🐱'] * 2  # 2 coppie

# --- VARIABILI GLOBALI ---
first_card = None
matches_found = 0
start_time = 0
mistakes = 0
player_data = []

# --- LOGICA GIOCO ---
def shuffle_cards():
    random.shuffle(CARDS)
    return CARDS

def card_click(i, buttons, symbols):
    global first_card, matches_found, mistakes

    buttons[i].config(text=symbols[i], state="disabled")

    if first_card is None:
        first_card = i
    else:
        if symbols[i] == symbols[first_card]:
            matches_found += 1
            first_card = None
            if matches_found == GRID_SIZE:
                end_game()
        else:
            mistakes += 1
            root.after(1000, reset_cards, i, first_card, buttons)
            first_card = None

def reset_cards(i1, i2, buttons):
    buttons[i1].config(text="?", state="normal")
    buttons[i2].config(text="?", state="normal")

def end_game():
    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    # Salva dati
    player_data.append({
        'avg_time_per_card': total_time / (GRID_SIZE * 2),
        'mistakes': mistakes,
        'level': GRID_SIZE * 2,
        'success': 1  # completato con successo
    })
    pd.DataFrame(player_data).to_csv("player_data.csv", index=False)

    result_label.config(text=f"Fatto! Tempo: {total_time}s | Errori: {mistakes}")

# --- INTERFACCIA TKINTER ---
def start_game():
    global start_time, matches_found, mistakes, first_card
    first_card = None
    matches_found = 0
    mistakes = 0
    result_label.config(text="")

    symbols = shuffle_cards()
    for i in range(GRID_SIZE * 2):
        buttons[i].config(text="?", state="normal", command=lambda i=i: card_click(i, buttons, symbols))

    start_time = time.time()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🧠 Memory Game Adattivo")

buttons = []
for i in range(GRID_SIZE * 2):
    btn = tk.Button(root, text="?", width=10, height=5)
    btn.grid(row=i // GRID_SIZE, column=i % GRID_SIZE, padx=10, pady=10)
    buttons.append(btn)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=2, column=0, columnspan=GRID_SIZE)

start_button = tk.Button(root, text="Inizia", command=start_game)
start_button.grid(row=3, column=0, columnspan=GRID_SIZE, pady=10)

root.mainloop()
