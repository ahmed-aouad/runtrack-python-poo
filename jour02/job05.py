class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50  


    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def est_en_marche(self):
        return self.__en_marche


    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_annee(self, annee):
        self.__annee = annee

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Méthode privée pour vérifier le niveau du réservoir
    def __verifier_plein(self):
        return self.__reservoir

    # Méthodes pour démarrer et arrêter la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:  # Vérification du niveau de carburant
            self.__en_marche = True
            print("Voiture démarée")
        else:
            print("Le niveau de carburant est insuffisant pour démarrer.")

    def arreter(self):
        self.__en_marche = False

#test
audi=Voiture("audi","r8","2018", 100)
audi.demarrer()
