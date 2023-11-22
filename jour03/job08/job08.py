def afficher_produits():

    type = input("Entrez le type (fruit/légume) : ").lower()
    saison = input("Entrez la saison (hiver/été) : ").lower()


    if type == "fruit" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruit" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "légume" and saison == "été":
        print("Artichaut, aubergine, navet")
    else:
        print("Combinaison type et saison non prise en charge")


afficher_produits()
