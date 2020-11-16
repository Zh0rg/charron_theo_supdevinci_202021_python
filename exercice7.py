# Pour pouvoir utiliser les expressions régulières
import re

# Les différents patterns et erreurs associées
patterns = [
    ".*[a-z].*",
    ".*[AZ].*",
    ".*[0-9].*",
    ".*[@$#].*"
]
mots_de_passe = re.split(r'\s*,\s*', input("Entrez une liste de mots de passe: "))

for mot_de_passe in mots_de_passe:
    valide = True

    if not (len(mot_de_passe) >= 6 and len(mot_de_passe) <= 12):
        valide = False

    # On vérifie si chaque pattern est trouvé dans mot_de_passe
    # Si il est manquant, valide passe à False
    for pattern in patterns:
        if re.fullmatch(pattern, mot_de_passe) is None:
            valide = False

    if valide:
        print(mot_de_passe)
