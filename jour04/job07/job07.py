def compter_multiples_de_trois(liste):
    """
    Compte le nombre de multiples de 3 dans une liste.
    """
    count = 0
    for nombre in liste:
        if nombre % 3 == 0:
            count += 1
    return count


L = [8, 24, 48, 2, 16]
print (L)


nombre_de_multiples_de_trois = compter_multiples_de_trois(L)

print("Le nombre de multiples de 3 :", nombre_de_multiples_de_trois)
