def time_to_text():
    try:
        minutes = int(input("Entrez le nombre de minutes : "))

        if minutes >= 0:
            heures = minutes // 60
            minutes_restantes = minutes % 60

            if heures == 0 and minutes_restantes == 0:
                print("0 heures et 0 minutes")
            elif heures == 0:
                print(f"{minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
            elif minutes_restantes == 0:
                print(f"{heures} heure{'s' if heures > 1 else ''}")
            else:
                print(f"{heures} heure{'s' if heures > 1 else ''} et {minutes_restantes} minute{'s' if minutes_restantes > 1 else ''}")
        else:
            print("Veuillez entrer un nombre entier de minutes positif.")
    except ValueError:

        print("Veuillez entrer un nombre entier de minutes valide.")

time_to_text()