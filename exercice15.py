# On saisie les deux chaînes
chaine1 = input("Première chaine: ")
chaine2 = input("Seconde chaine: ")

# On compare les longueurs et on affiche la plus longue si elle existe
if len(chaine1) > len(chaine2):
    print(chaine1)
elif len(chaine1) < len(chaine2):
    print(chaine2)
else:
    print(chaine1)
    print(chaine2)
