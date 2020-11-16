# def permet de définir une fonction
def addstr(first, second):
    # Pour additioner et non concaténer, on dait convertir les chaînes qui contiennent des entiers en nombres
    result = int(first) + int(second)
    # print sert à afficher dans la console
    print(result)

# Exemple
print("'1' + '2' = ")
addstr("1", "2")
