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
              
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp

def arrondir_et_trier(liste):
    """
    Arrondit les nombres de la liste et retourne la liste triée dans l'ordre croissant.
    """
   
    n = 0

    
    for _ in liste:
        n += 1

   
    for i in range(n):
        
        liste[i] = int(liste[i] + 0.5)

    tri_a_bulles(liste)

    return liste
liste_nombre = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("Liste initiale :", liste_nombre)

resultat = arrondir_et_trier(liste_nombre)
print("Liste arrondie et triée :", resultat)
