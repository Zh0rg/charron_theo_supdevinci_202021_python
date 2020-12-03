def binary_search(l, value):
    start = 0
    end = len(l) - 1
    index = -1

    while start <= end:
        middle = (end + start) // 2

        # Puisque la liste est triée, si l[middle] > valeur,
        # valeur se trouve entre debut et milieu
        if l[middle] > value:
            end = middle
        # Et vice-versa
        elif l[middle] < value:
            start = middle
        # Si l[middle] == valeur
        else:
            index = middle
            break

    return index

#Test
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elt = 6
print("L'élément {} est à l'indice {}.".format(elt, binary_search(array, elt)))
