def afficher_alphabet_a_lenvers():
    print(' '.join(chr(lettre) for lettre in range(ord('Z'), ord('A')-1, -1)))

afficher_alphabet_a_lenvers()
