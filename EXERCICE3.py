# Demande à l'utilisateur de saisir la distance en kilomètres
distance_km = float(input("Entrez la distance en kilomètres : "))

# Demande à l'utilisateur de saisir le temps en minutes
temps_minute = float(input("Entrez le temps en minutes : "))

# Convertit la distance en mètres (1 kilomètre = 1000 mètres)
distance_metres = distance_km * 1000

# Convertit le temps en secondes (1 minute = 60 secondes)
temps_secondes = temps_minute * 60

# Calcule la vitesse en mètres par seconde
vitesse = distance_metres / temps_secondes

# Affiche la vitesse
print("La vitesse en mètre par seconde est " ,vitesse, "m/s.")
