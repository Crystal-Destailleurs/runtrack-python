# Variables représentant un produit
nom_produit = "Ordinateur portable"
prix_unitaire = 1000.0
quantite_en_stock = 50

# Afficher les informations du produit de manière formatée
print("Informations du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire : {prix_unitaire} euros")
print(f"Quantité en stock : {quantite_en_stock}")

# Demander la quantité à ajouter dans le stock
quantite_ajoutee = int(input("Entrez la quantité à ajouter dans le stock : "))
quantite_en_stock += quantite_ajoutee

# Demander la quantité à acheter
quantite_achetee = int(input("Entrez la quantité que vous souhaitez acheter : "))

# Mettre à jour le stock et calculer le coût total
cout_total = quantite_achetee * prix_unitaire
quantite_en_stock -= quantite_achetee

# Mettre à jour le prix unitaire avec une augmentation de 10%
prix_unitaire *= 1.1

# Afficher à nouveau toutes les informations sur le produit
print("\nInformations mises à jour du produit :")
print(f"Nom du produit : {nom_produit}")
print(f"Prix unitaire après augmentation de 10% : {prix_unitaire} euros")
print(f"Quantité en stock après ajout : {quantite_en_stock}")
print(f"Coût total de l'achat : {cout_total} euros")
