def draw_carpet_with_diagonal(n):
    for i in range(n+1):
        for j in range(n+1):
            
            if i == 0 and j == 0:
                # Coin supérieur gauche
                print('+', end='')
            elif i == 0 and j == n:
                # Coin supérieur droit
                print('+', end='')
            elif i == n and j == 0:
                # Coin inférieur gauche
                print('+', end='')
            elif i == n and j == n:
                # Coin inférieur droit
                print('+', end='')
            elif i == 0 or i == n:
                # Afficher les bords supérieur et inférieur avec '-'
                print('-', end='')
            elif j == 0 or j == n:
                # Afficher les bords latéraux avec '|'
                print('|', end='')

            elif i + j == n:
                # Afficher la diagonale inversée avec des espaces sur un fond de '#'
                print(' ', end='')
            else:
                # Afficher le reste du tapis avec '.'
                print('#', end='')
        print()  # Passer à la ligne suivante après chaque ligne

# Exemple d'utilisation avec n=9
taille = int(input("Entrez la taille du tapis : "))
draw_carpet_with_diagonal(taille)
