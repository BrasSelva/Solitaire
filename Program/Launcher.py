import random

# Définir les valeurs et les enseignes des cartes
valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
enseignes = ['Cœur', 'Carreau', 'Trèfle', 'Pique']

# Créer un jeu de cartes
jeu_de_cartes = [{'valeur': valeur, 'enseigne': enseigne} for valeur in valeurs for enseigne in enseignes]

# Mélanger le jeu de cartes
random.shuffle(jeu_de_cartes)

# Distribuer les cartes pour la partie de solitaire
tas_de_cartes = jeu_de_cartes[:28]  # Les 28 premières cartes forment le tas initial
reserve = jeu_de_cartes[28:]  # Les cartes restantes forment la réserve

# Afficher le tas de cartes et la réserve
print("Tas de cartes initial:")
print(tas_de_cartes)
print("\nRéserve:")
print(reserve)
