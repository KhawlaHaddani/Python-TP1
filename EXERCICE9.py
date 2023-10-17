total_facture = 0

for i in range(2):
    nom_article = input("Donnez le nom du " + str(i + 1) + "er article :")
    quantite_article = int(input("Donnez la quantité du " + str(i + 1) + "er article :"))
    prix_article = int(input("Donnez le prix unitaire du " + str(i + 1) + "er article :"))

    # Calcul du montant HT (montant de chaque article)
    montant_HT = prix_article * quantite_article

    # Affichage du prix total de l'article
    print("Totale pour l'article", nom_article, ":", montant_HT, "dh (ht)")

    total_facture += montant_HT

# Calcul du montant TTC (avec TVA)
montant_TTC = total_facture + total_facture * 0.20

# Affichage du prix total de la facture
print("Le total de votre facture est :", montant_TTC, "dh (TTC)")
