heads = int(input("Nombre de tetes: "))
legs = int(input("Nombre de pattes: "))

# Il y a au moins tetes * 2 pattes, le nombre de pattes est impair ou il n'y a pas assez de têtes
if legs < heads * 2 or legs % 2 != 0 or legs > heads * 4:
    exit("Casse-tete impossible à résoudre")

# Il y a au moins 'tetes' paires de pattes,
# les paires de pattes restantes appartiennent aux lapins.
# (legs - heads * 2) * 2 est le nombre de pattes appartenant aux lapins
# le reste appartient aux poulets
# On divise par 4 le nombre de pattes de lapins pour obtenir le nombre de lapins
# (legs - heads * 2) * 2 / 4 = (legs - heads * 2) / 2
# On soustrait le nombre de lapins au nombre de tetes pour obtenir le nombre de poulets
rabbits = (legs - heads * 2)  / 2
# ou  rabbits = legs % heads / 2
chickens = heads - rabbits

# On affiche le résultat
print("Il y a {} lapins et {} poulets dans la ferme.".format(int(rabbits), int(chickens)))
