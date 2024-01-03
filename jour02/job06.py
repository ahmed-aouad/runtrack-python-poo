class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix):
        if self.__statut_commande == "en cours":
            self.__plats_commandes[nom_plat] = prix
        else:
            print("Impossible d'ajouter un plat, la commande n'est pas en cours.")

    def annuler_commande(self):
        self.__statut_commande = "annulée"

    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande N°{self.__numero_commande}")
        for plat, prix in self.__plats_commandes.items():
            print(f"- {plat}: {prix}€ HT")
        print(f"Total: {total}€ (TVA incluse)")

    
    def __calculer_total(self):
        total = sum(self.__plats_commandes.values())
        return total + self.__calculer_tva(total)

    def __calculer_tva(self, total):
        tva = total * 0.2  #TVA est de 20%
        return tva

commande1 = Commande(1)
commande1.ajouter_plat("couscous", 15)
commande1.afficher_commande()
