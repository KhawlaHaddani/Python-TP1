# Demande à l'utilisateur de saisir deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Vérifie si le produit est négatif ou positif
if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
    print("Le produit de ces deux nombres est positif.")
else:
    print("Le produit de ces deux nombres est négatif.")
