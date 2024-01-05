class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    
    def informationsVehicule(self):
        print(f"Marque = {self.marque}")
        print(f"Modèle = {self.modele}")
        print(f"Année = {self.annee}")
        print(f"Prix = {self.prix}")
    
    def demarrer(self):
        print("Attention, je roule!")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        Vehicule.__init__(self,marque, modele, annee, prix)
        self.roue = roue
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues = {self.roue}")


    
    def demarrer(self):
        print("Attention, la mob démarre!")



class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        Vehicule.__init__(self,marque, modele, annee, prix)
        self.portes = portes
    def demarrer(self):
        print("Attention, la titine démarre!")

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes = {self.portes}")

moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsVehicule()
moto.demarrer()
print()
voiture = Voiture("Mercedes", "Classe A", 2020, 18500)
voiture.informationsVehicule()
voiture.demarrer()

