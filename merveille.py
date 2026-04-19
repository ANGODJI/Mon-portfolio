import random

jour=["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
jour_secret=random.choice (jour)
tentatives_max=2
tentatives_faites=0
trouve=False

print(f"jeux du jour mystère (Maximum {tentatives_max}essai)")

while tentatives_faites < tentatives_max and not trouve:
    essai=input (f"\n essaie {tentatives_faites+1}/{tentatives_max} - entre un jour: ")
    tentatives_faites+=1

    pos_essai = jour.index(essai)
    pos_secret = jour.index(jour_secret)

    if pos_essai == pos_secret:
        print("✅ Bravo, tu as trouvé !")
        trouve = True
    elif pos_essai > pos_secret:
        print("C'est plus tôt dans la semaine (avant)")
    else:
        print("C'est plus tard dans la semaine (après)")
if not trouve:
    print(f"\n❌ Dommage ! Tu as épuisé tes {tentatives_max} tentatives.")
    print(f"Le jour secret était : {jour_secret}")   
        
