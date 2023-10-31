def retourner_premiere_carte(pile):
    if len(pile) > 0:
        carte_retournee = pile.pop(0)  # Retire la première carte de la pile
        carte_retournee['retournee'] = True  # Marque la carte comme retournée
        return carte_retournee
    else:
        print("La pile est vide.")
        return None

# Exemple d'utilisation
tas_de_cartes = [{'valeur': '2', 'enseigne': 'Cœur'},
                 {'valeur': '5', 'enseigne': 'Pique'},
                 {'valeur': 'K', 'enseigne': 'Carreau'}]

# Retourner la première carte de la pile
carte_retournee = retourner_premiere_carte(tas_de_cartes)

# Afficher la carte retournée
if carte_retournee:
    print("Carte retournée:", carte_retournee)
else:
    print("Aucune carte retournée.")
