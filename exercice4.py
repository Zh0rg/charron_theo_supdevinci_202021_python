# On importe le module pour utiliser les expressions régulières
from re import split

x, y = [int(d) for d in split(r'\s*,\s*', input())]

array = list()

# i prend pour valeurs de 0 à x
for i in range(x):
    # On rajoute une ligne
    array.append(list())

    # j prend pour valeurs de 0 à y
    for j in range(y):
        # Le j-ième élément de la ligne i prend pour valeur i * j
        array[i].append(i * j)

array2 = [[i * j  for j in range(y)] for i in range(x)]

# On affiche le tableau
print(array)
print(array2)
