temperature =[22,18,25,30,17,28,21]
print("latempérature la plus haute est :", max(temperature),"°C")

print("la température la plus basse est :", min(temperature),"°C")

moyenne = sum(temperature) / len(temperature)

print("la moyenne des températures est :", moyenne,"°C")

jours_chauds = [temp for temp in temperature if temp > 20]
print("les jours où la température a dépassé 20°C sont :", jours_chauds)

print("le nombre de jours où la température a dépassé 20°C est :", len(jours_chauds))
 














