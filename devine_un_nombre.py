from random import randint

nombre_a_deviner = randint(1, 100)

print("Devinez le nombre")

while True:
    premier_essai = int(input('Quel est le nombre? '))

    if premier_essai < nombre_a_deviner:
        print("C'est plus")
    elif premier_essai > nombre_a_deviner:
        print("C'est moins")
    else:
        print("Vous avez gagné")
        break

print("Fin du jeu")
