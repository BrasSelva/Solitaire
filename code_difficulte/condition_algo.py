import random

def creer_paquet(difficulte):
    if difficulte == "facile":
        return random.sample(range(1, 14), 4)
    elif difficulte == "intermediaire":
        return random.sample(range(1, 14), 6)
    elif difficulte == "difficile":
        return random.sample(range(1, 14), 8)
   

def jouer_solitaire(paquet):
    # Implementez ici la logique du jeu de solitaire en utilisant le paquet fourni.


if name == "main":
    difficulte = input("Choisissez la difficulté (facile, intermediaire, difficile) : ")
    paquet = creer_paquet(difficulte)
    jouer_solitaire(paquet)