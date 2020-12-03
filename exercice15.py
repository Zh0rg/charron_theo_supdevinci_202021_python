# On saisie les deux chaînes
first = input("Première chaine: ")
second = input("Seconde chaine: ")

# On compare les longueurs et on affiche la plus longue si elle ne sont pas de même longueurs
if len(first) > len(second):
    print(first)
elif len(first) < len(second):
    print(second)
else:
    print(first)
    print(second)
