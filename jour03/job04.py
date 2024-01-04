class Joueur:
    def __init__(self,nom, numero, position,buts, passesdecisives,cartonsjaunes,cartonsrouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passesdecisives=passesdecisives
        self.cartonsjaunes=cartonsjaunes
        self.cartonsrouges=cartonsrouges

    def marquerUnBut(self):
        self.buts +=1
    def effectuerUnePasseDecisive(self):
        self.passesdecisives +=1
    def recevoirUnCartonJaune(self):
        self.cartonsjaunes +=1
    def recevoirUnCartonRouge(self):
        self.cartonsrouges +=1
    def afficherStatistiques(self):
        print(f"Satistiques {self.nom} \nnumero : {self.numero} \nposition: {self.position} \nbut:{ self.buts} \npassesdecisives :{ self.passesdecisives} \ncartonsjaunes: {self.cartonsjaunes}\ncartonsrouges : {self.cartonsrouges}")
        
class Equipe:
    def __init__(self,nom):
        self.nom = nom
        self.liste_joueurs=[]
    def ajouterJoueur(self,joueur):
         self.liste_joueurs.append(joueur)
    def AfficherStatistiquesJoueurs(self): 
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()       
    def mettreAJourStatistiquesJoueur(self,nom, numero, position,buts, passesdecisives,cartonsjaunes,cartonsrouges):
        self.nom=nom
        self.numero=numero
        self.position=position
        self.buts=buts
        self.passesdecisives=passesdecisives
        self.cartonsjaunes=cartonsjaunes
        self.cartonsrouges=cartonsrouges

Maradona=Joueur("Maradona",10,"buteur",0,0,1,0)
VanBasten=Joueur("VanBasten",9,"Ailier droit",0,0,0,0)
Cantona=Joueur("Cantona",11,"buteur",0,0,3,1)

Milan=Equipe("Milan")
Madrid=Equipe("Madrid")

Milan.ajouterJoueur(Maradona)
Milan.ajouterJoueur(VanBasten)
Madrid.ajouterJoueur(Cantona)

Milan.AfficherStatistiquesJoueurs()
Maradona.marquerUnBut()
VanBasten.effectuerUnePasseDecisive()
VanBasten.recevoirUnCartonRouge()
Maradona.recevoirUnCartonJaune()
Milan.AfficherStatistiquesJoueurs()
    





