# On importe le module pour utiliser les expressions régulières
from re import split

# On transforme la chaîne en liste
mots = split(r'\s*,\s*', input())
# On trie la liste
mots.sort()
# On transforme la liste en chaîne
# dans laquelle les mots sont séparés par des virgules
resultat = ", ".join(mots)
# On affiche
print(resultat)
