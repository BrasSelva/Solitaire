import tkinter as tk
import random

def initialiser_plateau():
    # Créez un plateau avec des paires de cartes.
    cartes = ["As", "Roi", "Dame", "Valet", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    plateau = cartes * 2
    random.shuffle(plateau)
    return plateau

def retourner_carte(carte_index):
    # Retourne une carte lorsque l'utilisateur clique dessus.
    if not cartes_retournees[carte_index]:
        cartes_retournees[carte_index] = True
        labels_cartes[carte_index].config(text=plateau[carte_index])

def rafraichir_plateau():
    # Rafraîchit le plateau en masquant les cartes retournées.
    for i in range(len(plateau)):
        if not cartes_retournees[i]:
            labels_cartes[i].config(text="")

fenetre = tk.Tk()
fenetre.title("Jeu de Cartes")

plateau = initialiser_plateau()
cartes_retournees = [False] * len(plateau)
labels_cartes = []

for i in range(len(plateau)):
    label_carte = tk.Label(fenetre, text="", font=("Arial", 24), width=5, height=2)
    label_carte.grid(row=i // 4, column=i % 4)
    label_carte.bind("<Button-1>", lambda event, i=i: retourner_carte(i))
    labels_cartes.append(label_carte)

bouton_rafraichir = tk.Button(fenetre, text="Rafraîchir le plateau", command=rafraichir_plateau)
bouton_rafraichir.grid(row=len(plateau) // 4 + 1, columnspan=4)

fenetre.mainloop()