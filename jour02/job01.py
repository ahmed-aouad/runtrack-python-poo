
class rectangle:
    def __init__(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def mutateur(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def afficher(self):
        print(f" La longueur est : {self.__longueur} , La largeur est : {self.__largeur}")

rect=rectangle(10,5)
rect.afficher()

rect.mutateur(25,15)
rect.afficher() 