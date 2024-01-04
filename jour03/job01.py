class Ville:
    def __init__(self, nom, nombrehabitant):
        self.__nom = nom        
        self.__nombrehabitant = nombrehabitant

    def get_Habitant(self):
        return self.__nombrehabitant
    
    def get_Ville(self):
        return self.__nom
    
    def set_Habitant(self, nombrehabitant):
        self.__nombrehabitant = nombrehabitant  

    def afficher(self):
        print(f"La population de la ville de {self.__nom} est de: {self.__nombrehabitant} habitants")

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom        
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self, nouvelle_population):
        nouvelle_population += self.__ville.get_Habitant()
        self.__ville.set_Habitant(nouvelle_population)
        print(f"Mise à jour de la populationde de la ville de {self.__ville.get_Ville()} {nouvelle_population} habitants")

Paris = Ville("Paris", 1000000)  
Paris.afficher()  

Marseille = Ville("Marseille", 861635)
Marseille.afficher()

john = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Marseille)
Chloe = Personne("Chloe", 18, Paris)

john and Chloe.ajouterPopulation(2)
Myrtille.ajouterPopulation(1)

