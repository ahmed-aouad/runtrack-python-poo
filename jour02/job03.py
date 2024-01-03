class Livre:
    def __init__(self, titre, auteur, nombresdepages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombresdepages = nombresdepages
        self.__disponible = True

    def changer_titre(self, titre):
        self.__titre = titre

    def changer_auteur(self, auteur):
        self.__auteur = auteur

    def changer_nombresdepages(self, nombresdepages):
        if nombresdepages > 1:
            self.__nombresdepages = nombresdepages
        else:
            print("Erreur de pages")

    def afficher(self):
        disponibilite = "disponible" if self.__disponible else "indisponible"
        print(f"Le livre {self.__titre}, écrit par {self.__auteur}, a {self.__nombresdepages} pages et est {disponibilite}.")

    def vérification(self):
        return self.__disponible

    def emprunter(self):
        if self.vérification():
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.vérification():
            self.__disponible = True
        else:
            print("Le livre n'a pas été emprunté.")

# Utilisation de la classe Livre
livre = Livre("Le rouge et le noir", "Stendhal", 350)
livre.afficher()
livre.emprunter()
livre.afficher()
livre.rendre()
livre.afficher()
