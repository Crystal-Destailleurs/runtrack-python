def calcule():
    # Demander à l'utilisateur de saisir les valeurs
    num1 = float(input("Entrez le premier nombre : "))
    operator = input("Entrez l'opérateur (+, -, *, /, %) : ")
    num2 = float(input("Entrez le deuxième nombre : "))

    # Vérifier si l'opérateur est pris en charge
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Erreur : Division par zéro",
        '%': num1 % num2 if num2 != 0 else "Erreur : Division par zéro",
    }

    result = operations.get(operator, "Opérateur non pris en charge")
    print(f"Le résultat de {num1} {operator} {num2} est : {result}")

# Appel de la fonction
calcule()
