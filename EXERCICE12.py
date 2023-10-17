# Fonction pour calculer le salaire en fonction du grade et du nombre d'heures travaillées
def calculer_salaire(grade, heures_travaillees):
    tarif_horaire = 0
    prime = 0
    
    if grade == "A":
        tarif_horaire = 200
        prime = (heures_travaillees // 20) * 1000
    elif grade == "B":
        tarif_horaire = 150
        prime = (heures_travaillees // 20) * 800
    elif grade == "C":
        tarif_horaire = 120
        prime = (heures_travaillees // 15) * 500
    elif grade == "D":
        tarif_horaire = 100
        prime = (heures_travaillees // 15) * 350
    elif grade == "E":
        tarif_horaire = 80
        prime = (heures_travaillees // 10) * 100
    else:
        return "Grade invalide"

    salaire = (tarif_horaire * heures_travaillees) + prime
    return salaire

# Demande à l'utilisateur de saisir le grade de l'employé
grade = input("Entrez le grade de l'employé (A, B, C, D ou E) : ")

# Demande à l'utilisateur de saisir le nombre d'heures travaillées
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))

# Calcule le salaire en fonction du grade et du nombre d'heures travaillées
salaire = calculer_salaire(grade, heures_travaillees)

# Affiche le résultat
# if isinstance(salaire, int):
print(f"Le salaire de l'employé est : {salaire} DH.")
#else:
    #print(salaire)
