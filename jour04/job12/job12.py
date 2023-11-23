def tri_croissant(liste):
    """
    Trie la liste passée en paramètre dans l'ordre croissant (tri par sélection).
    """
    n = 0
    for _ in liste:
        n += 1

    for i in range(n - 1):
        index_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[index_min]:
                index_min = j

        temp = liste[i]
        liste[i] = liste[index_min]
        liste[index_min] = temp


ma_liste = [7, 11, 42, 39, 2]

print("Liste initiale :", ma_liste)

tri_croissant(ma_liste)


print("Liste triée :", ma_liste)
