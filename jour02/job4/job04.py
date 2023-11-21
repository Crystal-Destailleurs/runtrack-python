def saisir_entier_superieur_zero(message):
    while True:
        try:
            valeur = int(input(message))
            if valeur > 0:
                return valeur
            else:
                print("Veuillez entrer un entier supérieur à zéro.")
        except ValueError:
            print("Veuillez entrer un entier valide.")

def afficher_tables_multiplication(n):
    for i in range(1, n + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

N = saisir_entier_superieur_zero("Entrez un entier supérieur à zéro (N) : ")

afficher_tables_multiplication(N)
