import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class JeuDeCartes:
    def __init__(self):
        couleurs = ["Coeurs", "Carreaux", "Piques", "Trèfles"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.cartes = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]

    def melanger(self):
        random.shuffle(self.cartes)

    def tirer_carte(self):
        if not self.cartes:
            return None
        return self.cartes.pop()

# Créer un jeu de cartes
jeu_de_cartes = JeuDeCartes()

# Mélanger le jeu de cartes
jeu_de_cartes.melanger()

# Tirer et afficher quelques cartes
for _ in range(5):
    carte = jeu_de_cartes.tirer_carte()
    if carte:
        print(carte)
    else:
        print("Le jeu de cartes est vide.")