def arrondir_notes(liste_notes):
    notes_arrondies = []
    for note in liste_notes:
        if note < 40:
            # Si la note est inférieure à 40, l'étudiant échoue, pas d'arrondi
            notes_arrondies.append(note)
        else:
            # Arrondir la note aux multiples de 5 si nécessaire
            multiple_de_5_sup = ((note // 5) + 1) * 5
            if multiple_de_5_sup - note < 3:
                notes_arrondies.append(multiple_de_5_sup)
            else:
                notes_arrondies.append(note)
    return notes_arrondies

# Exemple d'utilisation
liste_notes = [37, 54, 82, 65, 28, 43, 73, 91]
notes_arrondies = arrondir_notes(liste_notes)

print("Notes d'origine :", liste_notes)
print("Notes arrondies :", notes_arrondies)
