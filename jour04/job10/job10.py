
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

valeurs_intervalle = [valeur for valeur in L if 25 <= valeur <= 90]

produit_valeurs_intervalle = 1
for valeur in valeurs_intervalle:
    produit_valeurs_intervalle *= valeur

print("Liste initiale :", L)
print("Liste des valeurs dans l'intervalle [25, 90] :", valeurs_intervalle)
print("Produit des valeurs dans l'intervalle [25, 90] :", produit_valeurs_intervalle)
