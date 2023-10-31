
plateau = {
    'colonnes': [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]],
    'piles_finales': {'Coeurs': [], 'Carreaux': [], 'Piques': [], 'Trèfles': []}
}

def est_action_correcte(depart_colonne, arrivee_colonne):
    if (
        0 <= depart_colonne < len(plateau['colonnes']) and
        0 <= arrivee_colonne < len(plateau['colonnes'])
    ):
        colonne_depart = plateau['colonnes'][depart_colonne]
        colonne_arrivee = plateau['colonnes'][arrivee_colonne]
        
        if colonne_depart and colonne_arrivee:
            carte_depart = colonne_depart[-1]
            carte_arrivee = colonne_arrivee[-1]

            if carte_depart < carte_arrivee:
                return True

    return False

# Exemple d'utilisation
depart_colonne = 2
arrivee_colonne = 1

if est_action_correcte(depart_colonne, arrivee_colonne):
    print("Mouvement valide.")
else:
    print("Mouvement non valide.")
