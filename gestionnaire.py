matieres = ["Communication digitale", "Anglais", "Ecosysteme digital", "Web analyst", "MERISE", "Analyse de données"]
liste_etudiants = []

print("=== GESTIONNAIRE D'ÉTUDIANTS (Moyenne, Statut & rang) ===")
while True:
    nom = input("\nEntrez le nom de l'étudiant (ou 'quitter' pour finir) : ")
    if nom.lower() == 'quitter':
        break

    age = input(f"Entrez l'âge de {nom} : ")
    spécialité = input(f"Entrez la spécialité de {nom} : ")

    somme_notes = 0

    print(f"Saisie des notes pour {nom} :")
    for matiere in matieres:
        note = float(input(f"  Note en {matiere} : "))
        somme_notes += note

    moyenne = somme_notes / len(matieres)

    if moyenne >= 10:
        statut = "ADMIS"
    else:
        statut = "AJOURNÉ"

    etudiant = {
        "Nom": nom,
        "Age": age,
        "Spécialité": spécialité,
        "Moyenne": round(moyenne, 2),
        "Statut": statut
    }

    liste_etudiants.append(etudiant)
    print("Ajout réussi :", etudiant)

liste_etudiants.sort(key=lambda x: x["Moyenne"], reverse=True)

for i, etudiant in enumerate(liste_etudiants):
    etudiant["Rang"] = i + 1

print("\n" + "=" * 95)
print(f"{'NOM':<15} | {'ÂGE':<5} | {'SPECIALITE':<15} | {'MOYENNE':<10} | {'RANG':<5} | {'STATUT'}")
print("-" * 95)

for e in liste_etudiants:
    print(f"{e['Nom']:<15} | {e['Age']:<5} | {e['Spécialité']:<15} | {e['Moyenne']:<10} | {e['Rang']:<5} | {e['Statut']}")

print("=" * 95)