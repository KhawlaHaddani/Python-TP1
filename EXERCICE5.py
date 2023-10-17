# Demande à l'utilisateur de saisir un nombre
nombre = int(input("Entrez un nombre : "))

# Vérifie si le nombre est pair
if nombre % 2 == 0:
    print("Ce nombre est pair")
elif nombre % 3 == 0:
    print("Ce nombre est impair, mais est multiple de 3")
else:
    print("Ce nombre n'est ni pair ni multiple de 3")
