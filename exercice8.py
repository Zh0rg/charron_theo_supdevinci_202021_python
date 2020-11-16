# Pour pouvoir utiliser les expressions régulières
import re

tuples = list()

while True:
    ligne = input()

    # Si la ligne est vide, on sort de la boucle de saisie
    if ligne == '':
        break

    # On utlise l'association pour séparer les valeurs
    prenom, age, score = re.split(r'\s*,\s*', ligne)
    # On ajoute le tuple après avoir converti les valeurs
    tuples.append((prenom, age, score))

# On trie
tuples.sort()
# On affiche
print(tuples)
