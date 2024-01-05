class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
         print(f"L'age de la perssone est : {self.age} ans")  

    def bonjour(self):
        print("Hello") 

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age    


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans.")

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print(f"Le cours de {self.__matiereEnseignee} va commencer")  


personne = Personne()
personne.afficherAge() 
personne.bonjour()      
personne.modifierAge(18)
personne.afficherAge() 
print()
eleve = Eleve(18)
eleve.bonjour() 
eleve.allerEnCours() 
eleve.afficherAge() 
print() 
professeur = Professeur("Cybersécurité")
professeur.enseigner()  

    


