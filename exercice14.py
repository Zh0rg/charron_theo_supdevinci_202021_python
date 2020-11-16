tetes = int(input("Nombre de tetes: "))
pattes = int(input("Nombre de pattes: "))

# Il y a au moins tetes * 2 pattes
if pattes < tetes * 2:
    print("Casse-tete impossible à résoudre")

# Il y a au moins 'tetes' paires de pattes,
# les paires de pattes restantes appartiennent aux lapins.
# (pattes - tetes * 2) * 2 est le nombre de pattes appartenant aux lapins
# le reste appartient aux poulets
# On divise par 4 le nombre de pattes de lapins pour obtenir le nombre de lapins
# (pattes - tetes * 2) * 2 / 4 = (pattes - tetes * 2) / 2
# On soustrait le nombre de lapin au nombre de tetes pour obtenir le nombre de poulets
lapins = (pattes - tetes * 2)  / 2
poulets = tetes - lapins

# On affiche le résultat
print("Il y a {} lapins et {} poulets dans la ferme.".format(int(lapins), int(poulets)))
