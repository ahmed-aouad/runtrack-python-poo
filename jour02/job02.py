class Livre:
    def __init__(self,titre, auteur, nombresdepages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombresdepages = nombresdepages

    def  changer_titre(self, titre):
        self.__titre = titre

    def changer_auteur(self, auteur):
        self.__auteur = auteur  
    
    def changer_nombresdepages(self, nombresdepages):

        if nombresdepages > 1:
            self.__nombresdepages = nombresdepages 

        else:
            print("erreur de pages")
            

    def afficher(self):
        print(f"Le livre est {self.__titre} , l'auteur est {self.__auteur}  , le nombre de page {self.__nombresdepages}")        

livre = Livre("Le rouge et le noir", "Stendhal", 350)
livre.afficher()
livre.changer_nombresdepages(400)
livre.afficher()
livre.changer_nombresdepages(0)
livre.changer_auteur("Henri Beyle")
livre.afficher()




