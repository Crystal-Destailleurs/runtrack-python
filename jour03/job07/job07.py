def determiner_domaine():
    
    langage = input("Entrez le langage : ")

    if langage.lower() == "javascript" or langage.lower() == "js":
        print("Tu es un développeur web")
    elif langage.lower() == "python":
        print("Tu es un développeur IA")
    elif langage.lower() == "java":
        print("Tu es un développeur logiciel")
    elif langage.lower() == "reactjs" or langage.lower() == "rjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")


determiner_domaine()

