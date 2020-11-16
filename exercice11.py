def recherche_binaire(liste, valeur):
    longueur = len(liste)
    debut = 0
    fin = longueur - 1
    indice = -1

    while debut <= fin:
        milieu = (fin - debut) // 2

        # Puisque la liste est triée, si liste[milieu] > valeur,
        # valeur se trouve entre debut et milieu
        if liste[milieu] > valeur:
            fin = milieu
        # Et vice-versa
        elif liste[milieu] > valeur:
            debut = milieu
        # Si liste[milieu] == valeur
        else:
            indice = milieu
            break

    return indice

#Test
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("L'élément 3 est à l'indice {}.".format(recherche_binaire(liste, 3)))
