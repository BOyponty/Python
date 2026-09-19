from calculs import Calculs moyenne, mention, est_admis, meilleure_etudiant, taux_reussite
def afficher_resultats(etudiants):
    for etudiant in etudiants:
        notes = etudiants[etudiant]["notes"]
        filiere = etudiants[etudiant]["filière"]
        moyenne_etudiant = moyenne(notes)
        mention_etudiant = mention(moyenne_etudiant)
        admis = est_admis(moyenne_etudiant)

        print(f"Étudiant: {etudiant}")
        print(f"Filière: {filiere}")
        print(f"Notes: {notes}")
        print(f"Moyenne: {moyenne_etudiant:.2f}")
        print(f"Mention: {mention_etudiant}")
        print(f"Admis: {'Oui' if admis else 'Non'}")
        print("-" * 30)

    meilleur, meilleure_moyenne = meilleure_etudiant(etudiants)
    taux = taux_reussite(etudiants)

    print(f"Meilleur étudiant: {meilleur} avec une moyenne de {meilleure_moyenne:.2f}")
    print(f"Taux de réussite: {taux:.2f}%")i
     