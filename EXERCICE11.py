poids = float(input("Donner le poids : "))
taille = float(input("Donner la taille : "))
if taille == 0:
    print("taille invalide.")
else:
    IMC = poids/(taille ** 2)

if IMC >= 40:
    print("obésité morbide ou massive")
elif (35 <= IMC < 40):
    print("obésité sévère")
elif (30 <= IMC < 35):
    print("obésité modérée")
elif (25 <= IMC < 30):
    print("Surpoids")
elif (18.8 < IMC < 25):
    print("corpulence normale")
elif (16.5 < IMC < 18.5):
    print("Maigreure")
else:
    print("Famine")




