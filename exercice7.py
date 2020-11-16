# Pour pouvoir utiliser les expressions régulières
import re

# Les différents patterns et erreurs associées
patterns = [
    ".*[a-z].*",
    ".*[AZ].*",
    ".*[0-9].*",
    ".*[@$#].*"
]
passwords = re.split(r'\s*,\s*', input("Entrez une liste de mots de passe: "))

for password in passwords:
    valid = True

    if not (len(password) >= 6 and len(password) <= 12):
        valid = False

    # On vérifie si chaque pattern est trouvé dans password
    # Si il est manquant, valid passe à False
    for pattern in patterns:
        if re.fullmatch(pattern, password) is None:
            valid = False

    if valide:
        print(password)
