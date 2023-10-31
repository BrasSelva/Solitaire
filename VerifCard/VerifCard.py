regles = {
    "action1": ["condition1", "condition2"],
    "action2": ["condition3"],
    "action3": ["condition1", "condition4"],
    # Ajoutez d'autres règles selon vos besoins
}

# Fonction pour vérifier la validité d'une action
def est_action_correcte(action, conditions):
    if action in regles:
        regle = regles[action]
        return all(cond in conditions for cond in regle)
    else:
        return False

# Exemple d'utilisation
action = "action1"
conditions = ["condition1", "condition2"]

if est_action_correcte(action, conditions):
    print(f"L'action '{action}' est correcte.")
else:
    print(f"L'action '{action}' est incorrecte.")
