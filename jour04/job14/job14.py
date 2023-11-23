def est_separateur(c):
    """
    Vérifie si le caractère c est un séparateur (espace, virgule, point, etc.).
    """
    return c in (' ', ',', '.', ';', ':', '!', '?')

def my_long_word(longueur_min, phrase):
    """
    Retourne les mots de la phrase ayant une longueur supérieure à longueur_min.
    """
    mots = []
    mot_actuel = ""

    for caractere in phrase:
        if not est_separateur(caractere):
            mot_actuel += caractere
        else:
            if mot_actuel:
       
                longueur_mot = 0
                for _ in mot_actuel:
                    longueur_mot += 1

                if longueur_mot > longueur_min:
                    mots.append(mot_actuel)
                mot_actuel = ""

    if mot_actuel:
  
        longueur_mot = 0
        for _ in mot_actuel:
            longueur_mot += 1

        if longueur_mot > longueur_min:
            mots.append(mot_actuel)

    return " ".join(mots)

longueur_minimale = 3
phrase = "La pain c'est bien car le pain c'est la vie, c'est comme l'eau, c'est bien et c'est la vie aussi"

resultat = my_long_word(longueur_minimale, phrase)
print("Output :", resultat)
