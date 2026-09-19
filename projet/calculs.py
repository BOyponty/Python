def moyenne(notes):
    return sum(notes) / len(notes)

    def mention (moyenne):
        if moyenne >= 16:
            return "Très bien"
        elif moyenne >= 14:
            return "Bien"
        elif moyenne >= 12:
            return "Assez bien"
        elif moyenne >= 10:
            return "Passable"
        else:
            return "Insuffisant"

            def meilleure_etudiant (etudiants):
                meilleure_moyenne = 0
                meilleur_etudiant = ""

                for etudiant in etudiants:
                    notes = etudiants[etudiant]["notes"]
                    moyenne_etudiant = moyenne(notes)

                    if moyenne_etudiant > meilleure_moyenne:
                        meilleure_moyenne = moyenne_etudiant
                        meilleur_etudiant = etudiant

                return meilleur_etudiant, meilleure_moyenne

                def taux_reussite(etudiants):
                    total_etudiants = len(etudiants)
                    etudiants_reussis = 0

                    for etudiant in etudiants:
                        notes = etudiants[etudiant]["notes"]
                        if moyenne(notes) >= 10:
                            etudiants_reussis += 1

                    return (etudiants_reussis / total_etudiants) * 100