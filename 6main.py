notes = [12, 8, 15, 18, 9, 14, 7, 16, 11, 13]
# 1. Trie les notes dans l'ordre croissant sans modifier la liste originale.
notes_triees = sorted(notes)
print("Notes triées :", notes_triees)
# 2. Affiche la médiane (valeur du milieu une fois triée).
n = len(notes_triees)
if n % 2 == 0:
    mediane = (notes_triees[n//2 - 1] + notes_triees[n//2]) / 2
else:
    mediane = notes_triees[n//2]
print(" Médiane :", mediane)
# 3. Sépare les notes en deux listes : admis (≥ 10) et recales (< 10).
admis = [note for note in notes if note >= 10]
recales = [note for note in notes if note < 10]
print("Admis :", admis) 
print("Recalés :", recales)
# 4. Affiche le taux de réussite en pourcentage.
taux_reussite = (len(admis) / len(notes)) * 100
print("Taux de réussite :", taux_reussite, "%") 



