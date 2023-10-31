def est_coup_valide(tas, position_source, position_cible):
    # Vérifie si un coup est valide
    if position_source < 0 or position_source >= len(tas) or position_cible < 0 or position_cible >= len(tas):
        return False

    carte_source = tas[position_source]
    carte_cible = tas[position_cible]

    # Vérifie si la carte source peut être déplacée vers la carte cible
    return carte_source['enseigne'] != carte_cible['enseigne'] and \
           valeurs.index(carte_source['valeur']) + 1 == valeurs.index(carte_cible['valeur'])

def resoudre_solitaire(tas):
    if len(tas) == 1:
        return [tas]

    solutions = []

    for i in range(len(tas)):
        for j in range(len(tas)):
            if i != j and est_coup_valide(tas, i, j):
                tas_temporaire = tas[:]
                carte_deplacee = tas_temporaire.pop(i)
                tas_temporaire.insert(j, carte_deplacee)
                sous_solutions = resoudre_solitaire(tas_temporaire)
                for solution in sous_solutions:
                    solutions.append([tas[i]] + solution)

    return solutions

# Utilisation de l'algorithme pour résoudre le solitaire
solution = resoudre_solitaire(tas_de_cartes)

# Affichage de la première solution trouvée
if solution:
    print("Solution trouvée:")
    print(solution[0])
else:
    print("Aucune solution trouvée.")
