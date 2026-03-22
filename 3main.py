produits = {
    "pommes":  {"prix": 1.50, "quantite": 100},
    "bananes": {"prix": 0.75, "quantite": 150},
    "lait":    {"prix": 2.30, "quantite":  50},
}
produits["pain"]= {"prix": 2.00, "quantite": 40}
produits["pommes"]["prix"] -= 10

print("Prix des lait:", produits["lait"]["prix"], "€")

print("Quantité de bananes:",produits["bananes"]["quantite"], "unités")

total = 0

for produit in produits:
    prix = produits[produit]["prix"]
    quantite = produits[produit]["quantite"]
    total += prix * quantite

print("Valeur totale du stock :", total)