class produit:
    def __init__(self,nom, prixHT,TVA):
        self.nom=nom
        self.prixHT=prixHT
        self.TVA= TVA
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * (self.TVA / 100))
        return prixTTC
    def afficher(self):
        infos= f"nom : {self.nom} , prix TTC : {self.CalculerPrixTTC()}"
        return infos
    def ChangerNom(self,nom):
        self.nom = nom
    def ChangerPrixHT(self,prixHT):
        self.prixHT=prixHT
    
pantalon=produit("pantalon",110,20)
pantalon.ChangerPrixHT(110)
print(pantalon.afficher())
veste=produit("veste",210,20)
veste.ChangerNom("blouson")
print(veste.afficher())
chemise=produit("chemise",130,20)
print(chemise.afficher())