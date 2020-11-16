n = int(input())
d = dict()

# i prend pour valeurs de 1 à n
for i in range(1, n + 1):
    # La valeur de d[i] est égale au carré de i
    d[i] = i ** 2

# On affiche le dictionnaire
print(d)
