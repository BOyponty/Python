"""Premier programme formation python"""

nom = input("Quel est votre nom ?")
age = 0
while age == 0:
    age_str = input("Quel est votre age ?")

    try:
        age = int(age_str)
         
    except:
        print("ERREUR: Vous devez rentrer un nombre pour l'age")  
        print("fin de la boucle") 
else:
    print("Vous vous appelez " + nom + ", vous avez" + str(age) + " ans")
    print("L'an prochain vous aurez" + str(age+1) + " ans") 


"""boucle while : tant que """

"""n = 0
while n < 5:
          print("debut de la boucle") 

          print ("valeur de n : " + str(n))
          n = n + 1
          print("fin de la boucle")   """

"""mot_de_passe = "" 
while not mot_de_passe == "TOTO":
    mot_de_passe = input("Quel est le mot de passe ?") 

print("Mot de passe correct, vous avez accès au compte")"""
    