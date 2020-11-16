rows = list()

while True:
    # Mets la saisie en majuscules
    row = input().upper()

    # Si la ligne est vide, on sort de la boucle
    if row == '':
        break

    rows.append(row)

# On affiche
print(*rows, sep='\n')
