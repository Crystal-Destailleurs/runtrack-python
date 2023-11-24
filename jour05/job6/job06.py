def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_par_semaine = 7
    nombre_allers_retours_par_jour = 2
    hauteur_totale_par_jour = nombre_allers_retours_par_jour * hauteur_marche
    distance_totale_par_semaine = nombre_jours_par_semaine * hauteur_totale_par_jour * nombre_marches / 100

    return distance_totale_par_semaine

# Exemple d'utilisation
nombre_marches = int(input("Entrez le nombre de marches du phare : "))
hauteur_marche = float(input("Entrez la hauteur de chaque marche en cm : "))

distance_totale = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)

print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
