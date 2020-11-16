# On importe le module pour utiliser les expressions régulières
from re import split

# On transforme la chaîne en liste
words = split(r'\s*,\s*', input())
# On trie la liste
words.sort()
# On transforme la liste en chaîne
# dans laquelle les mots sont séparés par des virgules
result = ", ".join(words)
# On affiche
print(result)
