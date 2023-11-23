def echanger_premiere_et_derniere(liste):
    """
    Échange les valeurs de la première et de la dernière case d'une liste non vide.
    """
    if len(liste) > 0:
        premiere_valeur = liste[0]
        derniere_valeur = liste[-1]

        liste[0] = derniere_valeur
        liste[-1] = premiere_valeur

ma_liste = [1, 2, 3, 4, 5]

print(ma_liste)


echanger_premiere_et_derniere(ma_liste)

print(ma_liste)
