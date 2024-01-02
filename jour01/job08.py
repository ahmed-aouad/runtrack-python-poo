# Définition de la classe Cercle
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def circonference(self):
        return 2 * 3.1416 * self.rayon

    def aire(self):
        return 3.1416 * self.rayon ** 2

    def diametre(self):
        return 2 * self.rayon
    
    def afficherInfos(self):
        print(f"Cercle - Rayon: {self.rayon}, Diamètre: {self.diametre()}, Circonférence: {self.circonference()}, Aire: {self.aire()}")



    # Création de deux cercles avec des rayons de 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

    # Affichage des informations pour chaque cercle
print("Informations du Cercle 1:")
cercle1.afficherInfos()
print()
print("Informations du Cercle 2:")
cercle2.afficherInfos()
