def supprimer_doublons(liste):
    """
    Supprime les doublons de la liste passée en paramètre.
    """
    liste_sans_doublons = []

    for element in liste:
        # Vérifier si l'élément est déjà dans la liste sans doublons
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Afficher la liste initiale
print("Liste initiale :", ma_liste)

# Appeler la fonction pour supprimer les doublons
liste_sans_doublons = supprimer_doublons(ma_liste)

# Afficher la liste sans doublons
print("Liste sans doublons :", liste_sans_doublons)
    