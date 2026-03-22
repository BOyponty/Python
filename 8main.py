etudiants = {
    "Alice":   [14, 16, 18, 12],
    "Bob":     [8,  10, 9,  11],
    "Charlie": [15, 17, 14, 19],
    "Diana":   [6,  8,  7,  9],
}
# 1. Calcule et affiche la moyenne de chaque étudiant.
moyennes = {nom: sum(notes) / len(notes) for nom, notes in etudiants.items()}
for nom, moyenne in moyennes.items():
    print(f"Moyenne de {nom} : {moyenne:.2f}")
# 2. Affiche le nom de l'étudiant avec la meilleure moyenne.    
meilleure_etudiant = max(moyennes, key=moyennes.get)
print(f"Étudiant avec la meilleure moyenne : {meilleure_etudiant} ({moyennes[meilleure_etudiant]:.2f})")
# 3. Affiche la liste des étudiants admis (moyenne ≥ 10).
etudiants_admis = [nom for nom, moyenne in moyennes.items() if moyenne >= 10]
print("Étudiants admis (moyenne ≥ 10) :", etudiants_admis)  

 
 
 