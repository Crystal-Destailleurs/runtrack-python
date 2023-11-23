def tri_a_bulles(liste):
    """
    Tri à bulles de la liste.
    """
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échanger les valeurs
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp

def arrondir_et_trier(liste):
    """
    Arrondit les nombres de la liste et retourne la liste triée dans l'ordre croissant.
    """
    for i in range(len(liste)):
        # Convertir chaque nombre à son entier le plus proche
        liste[i] = int(liste[i] + 0.5)

    # Appeler la fonction de tri à bulles
    tri_a_bulles(liste)

    return liste

# Exemple d'utilisation
liste_nombre = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print ( liste_nombre)

# Appeler la fonction et afficher le résultat
resultat = arrondir_et_trier(liste_nombre)
print("Liste arrondie et triée :", resultat)
