x = int(input("Nombre de lignes: "))
y = int(input("Nombre de colonnes: "))

array = list()

# i prend pour valeurs de 0 à x
for i in range(x):
    # On rajoute une ligne
    array.append(list())

    # j prend pour valeurs de 0 à y
    for j in range(y):
        # Le j-ième élément de la ligne i prend pour valeur i * j
        array[i].append(i * j)

# On affiche le tableau
print(array)
