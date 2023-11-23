def remplacer_element_par_somme(voisins, liste):
    """
    Remplace l'élément à l'index 3 de la liste par la somme des voisins.
    """
    if len(liste) >= 5:
        liste[3] = liste[voisins[0]] + liste[voisins[1]]

def main():

    L = [1, 2, 3, 4, 5]
 
    print(L)

    print(L[1])

    remplacer_element_par_somme([2, 4], L)

    print( L)

    print(L[-1])

main()
