lignes = list()

while True:
    # Mets la saisie en majuscules
    ligne = input().upper()

    # Si la ligne est vide, on sort de la boucle
    if ligne == '':
        break

    lignes.append(ligne)

# On affiche
print(*lignes, sep='\n')
