class Personnage:
    def __init__(self, nom, vie=100):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        ennemi.vie -= 10
        print(f"{self.nom} attaque {ennemi.nom} et lui inflige 10 points de dégâts!")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancerJeu(self):
        joueur = Personnage("Joueur")
        ennemi = Personnage("Ennemi", 100 + 50 * self.niveau)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                break

            ennemi.attaquer(joueur)

        self.afficherResultat(joueur, ennemi)

    def afficherResultat(self, joueur, ennemi):
        if joueur.vie > 0:
            gagnant, perdant = joueur, ennemi
        else:
            gagnant, perdant = ennemi, joueur

        print(f"{perdant.nom} a été vaincu! {gagnant.nom} remporte la victoire!")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()

