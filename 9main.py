annuaire = {
    "Alice":   "06 12 34 56 78",
    "Bob":     "07 98 76 54 32",
    "Charlie": "06 11 22 33 44",
}
# 1. Affiche le numéro de "Bob".
print("Numéro de Bob :", annuaire["Bob"])
# 2. Ajoute "Diana" avec le numéro `"07 55 44 33 22"`.
annuaire["Diana"] = "07 55 44 33 22"
# 3. Modifie le numéro de "Alice" en `"06 00 11 22 33"`.
annuaire["Alice"] = "06 00 11 22 33"
# 4. Supprime "Charlie" de l'annuaire.
del annuaire["Charlie"]
# 5. Vérifie si "Eve" est dans l'annuaire et affiche un message approprié.
if "Eve" in annuaire:
    print("Eve est dans l'annuaire.")
else:
    print("Eve n'est pas dans l'annuaire.")     
# 6. Affiche tous les contacts sous la forme : `"Alice → 06 12 34 56 78"`.
for nom, numero in annuaire.items():
    print(f"{nom} → {numero}")




