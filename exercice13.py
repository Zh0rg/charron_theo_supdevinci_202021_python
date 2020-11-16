# Pour l'aléatoire
import random

# On crée une liste de nombres pairs de 0 à 10 à partir d'un range
# grâce à la compréhension de liste
nombre = random.choice([i for i in range(11) if i%2 == 0])
# ou nombre = random.choice([i for i in range(0, 11, 2)])

# On affiche
print(nombre)
