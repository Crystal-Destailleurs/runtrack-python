def verifier_signe():
    # Demander à l'utilisateur de saisir un nombre
    nombre = float(input("Entrez un nombre : "))

    # Vérifier le signe du nombre
    if nombre > 0:
        print(f"{nombre} est positif")
    elif nombre < 0:
        print(f"{nombre} est négatif")
    else:
        print(f"{nombre} est nul")

# Appel de la fonction
verifier_signe()
