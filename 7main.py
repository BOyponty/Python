transactions = [500, -120, -45, 200, -300, 150, -80, 1000, -500, -95]
# 1. Calcule le solde final
solde_final = sum(transactions)
print("Solde final :", solde_final)
# 2. Affiche le total des crédits et le total des débits séparément.
total_credits = sum(t for t in transactions if t > 0)
total_debits = sum(t for t in transactions if t < 0)
print("le total des crédit sont :", total_credits)
print("le total des débits sont :", total_debits)
# 3. Affiche la transaction la plus importante (en valeur absolue).
transaction_importante = max(transactions, key=abs)
print("la transaction la plus importante est :", transaction_importante)
# 4. Affiche le nombre de transactions de chaque type (crédit / débit).
nombre_credits = sum(1 for t in transactions if t > 0)
nombre_debits = sum(1 for t in transactions if t < 0)
print("le nombre de crédits sont :", nombre_credits)
print("le nombre de débits sont :", nombre_debits)
# 5. Affiche "Compte positif ✅" ou "Compte négatif ❌" selon le solde.
if solde_final > 0:
    print("Compte positif ✅")              
else:   
     print("Compte négatif ❌")






7