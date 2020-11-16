result = str()

# i prend les valeurs de 2000 à 3200
for i in range(2000, 3201):
    # Si i est multiple de 7 mais pas de 5
    if i % 7 == 0 and i % 5 != 0:
        # Si ce n'est pas le premier nombre, on ajoute une virgule
        if result != "":
            result += ", "

        resultat += str(i)

# On affiche
print(result)
