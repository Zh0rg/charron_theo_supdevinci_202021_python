# Pour pouvoir utiliser les expressions régulières
import re

tuples = list()

while True:
    row = input()

    # Si la ligne est vide, on sort de la boucle de saisie
    if row == '':
        break

    # On utlise l'association pour séparer les valeurs
    name, age, score = re.split(r'\s*,\s*', row)
    # On ajoute le tuple après avoir converti les valeurs
    tuples.append((name, age, score))

# On trie
tuples.sort()
# On affiche
print(tuples)
