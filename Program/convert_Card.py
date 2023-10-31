class Carte:
    def init(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def str(self):
        return f"{self.valeur} de {self.couleur}"

def convertir_description_en_carte(description):
    mots = description.split()
    if len(mots) == 4 and mots[0] in ("As", "Roi", "Dame", "Valet", "10", "9", "8", "7", "6", "5", "4", "3", "2") and mots[1] == "de":
        return Carte(mots[0], mots[3])
    else:
        print(f"Description de carte invalide : {description}")
        return None

Exemple d'utilisation
description_carte_api = "As de cœur"
carte = convertir_description_en_carte(description_carte_api)

if carte:
    print(f"Carte convertie : {carte}")