import random

nombre_secret = random.randint(1, 50)
tentatives_max = 5
tentatives_faites = 0
trouve = False

print(f"Jeu du Nombre Mystère (Maximum {tentatives_max} essais)")

while tentatives_faites < tentatives_max and not trouve:
    essai = int(input(f"\nEssai {tentatives_faites + 1}/{tentatives_max} - Entre un nombre : "))
    tentatives_faites += 1 

    if essai > nombre_secret:
        print("🔼 Trop grand")
    elif essai < nombre_secret:
        print("🔽 Trop petit")
    else:
        print("✅ Bravo, tu as trouvé !")
        trouve = True

if not trouve:
    print(f"\n❌ Dommage ! Tu as épuisé tes {tentatives_max} tentatives.")
    print(f"Le nombre secret était : {nombre_secret}")