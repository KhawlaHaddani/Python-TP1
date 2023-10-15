# Demande à l'utilisateur de saisir son âge et sa taille
age = input("Entrez votre âge : ")
taille = input("Entrez votre taille en mètres : ")

# convertir les entrée a des nombres
a = int(age)
t = float(taille)

# Affiche les informations dans un message
print("Vous avez " , a , "ans et vous mesurez " , t ,"m.")