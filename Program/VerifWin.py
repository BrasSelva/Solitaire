jeu_de_solitaire = {
    'colonnes': {
        'colonne1': [4, 3, 2, 1],
        'colonne2': [],
        # ... Ajoutez d'autres colonnes
    },
    'piles_finales': {
        'Coeurs': [],
        'Carreaux': [],
        'Piques': [],
        'Trèfles': [],
    }
}

# Fonction pour vérifier la victoire
def est_victoire(jeu):
    for pile in jeu['piles_finales'].values():
        if len(pile) != 13:
            return False
    return True

# Fonction pour vérifier la défaite (exemple simplifié)
def est_defaite(jeu):
    for colonne in jeu['colonnes'].values():
        if colonne:
            return False
    return True

# Exemple d'utilisation
if est_victoire(jeu_de_solitaire):
    print("Félicitations, vous avez gagné le jeu de solitaire !")
elif est_defaite(jeu_de_solitaire):
    print("Désolé, vous avez perdu. Toutes les colonnes sont vides.")
else:
    print("Le jeu continue...")

# Modifiez le jeu_de_solitaire en fonction de l'état réel de votre jeu.
