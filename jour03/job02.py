class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert=False):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero}, Titulaire: {self.__prenom} {self.__nom}, Solde: {self.__solde}€, Découvert autorisé: {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print(f"Solde du compte: {self.__solde}€")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant pour ce retrait.")
        else:
            self.__solde -= montant
            print(f"Retrait de {montant}€ . Nouveau solde: {self.__solde}€")

    def agios(self):
        if self.__solde < 0:
            agios = -0.05 * self.__solde  
            self.__solde -= agios
            print(f"Agios de {agios}€ appliqués. Nouveau solde: {self.__solde}€")

    def virement(self, compte_dest, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant pour effectuer le virement.")
        else:
            self.__solde -= montant
            compte_dest.__solde += montant
            print(f"Virement de {montant}€ vers le compte {compte_dest.__numero} effectué. Nouveau solde: {self.__solde}€")


compte1 = CompteBancaire("19011979", "Robespierre", "Maximilien", 2000)
compte2 = CompteBancaire("20072022", "Bonaparte", "Napoleon", -100, decouvert=True)

compte1.afficher()
compte2.afficher()

compte1.versement(200)
compte1.retrait(500)
compte1.afficherSolde()

compte2.agios()
compte1.virement(compte2, 300)  

compte1.afficherSolde()
compte2.afficherSolde()

