def my_sort(liste):
    n = len(liste)  # Nombre d'éléments dans la liste
    coups = 0  # Initialiser le compteur de coups

    # Boucle extérieure pour passer à travers la liste
    for i in range(n):
        # Drapeau pour indiquer si des échanges ont été faits dans cette itération
        echanges_effectues = False

        # Boucle intérieure pour comparer et échanger les éléments adjacents
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                # Échanger les éléments
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echanges_effectues = True
                coups += 1

        # Si aucun échange n'a été effectué dans cette itération, la liste est triée
        if not echanges_effectues:
            break

    return liste, coups

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
liste_triee, nombre_coups = my_sort(ma_liste)

print("Liste triée :", liste_triee)
print("Nombre total de coups nécessaires :", nombre_coups)
