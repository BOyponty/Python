votes = ["Alice", "Bob", "Alice", "Charlie", "Bob",
         "Alice", "Charlie", "Bob", "Alice", "Charlie"]
# 1. Compte le nombre de votes pour chaque candidat (sans utiliser `Counter`).
vote_counts = {}
for vote in votes:
    if vote in vote_counts:
        vote_counts[vote] += 1
    else:
        vote_counts[vote] = 1           
# 2. Affiche les résultats triés du plus voté au moins voté.
sorted_votes = sorted(vote_counts.items(), key=lambda x: x[1], reverse=True)
print("Résultats triés du plus voté au moins voté :")
for candidat, count in sorted_votes:
    print(f"{candidat} : {count} votes")
# 3. Affiche le pourcentage de votes pour chaque candidat.
total_votes = len(votes)    
print("Pourcentage de votes pour chaque candidat :")
for candidat, count in vote_counts.items():
    pourcentage = (count / total_votes) * 100
    print(f"{candidat} : {pourcentage:.2f}%")
# 4. Déclare le vainqueur.
vainqueur = sorted_votes[0][0]          
print(f"Le vainqueur est : {vainqueur}")
# 5. Vérifie s'il y a égalité entre les deux premiers.
if len(sorted_votes) > 1 and sorted_votes[0][1] == sorted_votes
[1][1]:
    print("Il y a une égalité entre les deux premiers candidats.")      
else:    print("Il n'y a pas d'égalité entre les deux premiers candidats.")












Exercice 10 — 🔴 Difficile
Tu gères un système de votes pour une élection :
```python
votes = ["Alice", "Bob", "Alice", "Charlie", "Bob",
         "Alice", "Charlie", "Bob", "Alice", "Charlie"]
```
1. Compte le nombre de votes pour chaque candidat (sans utiliser `Counter`).
2. Affiche les résultats triés du plus voté au moins voté.
3. Affiche le pourcentage de votes pour chaque candidat.
4. Déclare le vainqueur.
5. Vérifie s'il y a égalité entre les deux premiers.