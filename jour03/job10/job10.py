def verifier_pair_impair():
    try:
  
        nombre = int(input("Entrez un nombre entier positif : "))


        if nombre >= 0:
            if nombre % 2 == 0:
                print(f"{nombre} est un nombre pair.")
            else:
                print(f"{nombre} est un nombre impair.")
        else:
            print("Veuillez entrer un nombre entier positif.")
    except ValueError:
        print("Veuillez entrer un nombre entier positif valide.")


verifier_pair_impair()
