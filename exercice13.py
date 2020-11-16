# Pour l'aléatoire
import random

# On crée une liste de nombres pairs de 0 à 10 à partir d'un range
# grâce à la compréhension de liste
number = random.choice([i for i in range(11) if i%2 == 0])
# ou number = random.choice([i for i in range(0, 11, 2)])

# On affiche
print(number)
