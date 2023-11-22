def Add():
    # Demander à l'utilisateur de saisir deux nombres entiers
    a = int(input("Entrez le premier nombre entier : "))
    b = int(input("Entrez le deuxième nombre entier : "))
    
    # Calculer la somme et l'afficher
    result = a + b
    print(f"La somme de  {a} et {b} est: {result}")

# Appels de la fonction
Add()
