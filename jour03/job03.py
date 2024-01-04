class Tache:
    def __init__(self,titre,description):
        self.titre=titre  
        self.description=description
        self.statut="à faire"
    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.tache=[]
    def ajouterTache(self,LaTache):
        self.tache.append(LaTache)
        print(f"ajout réussit")
    def supprimerTache(self,LaTache):
        self.tache.remove(LaTache)
    def marquerCommeFinie(self,LaTache):
        LaTache.statut = "Terminé"
        print(f"{LaTache} terminé !")
    def afficherListe(self):
       print("Liste des taches :")
       for tache in self.tache:
            print(tache)
    def filterListe(self,statut):
        n=0
        print(f"les taches {statut} :")
        for task in self.tache:          
            if task.statut == statut:
                n+=1
                print(task)
        if n==0 :
            print("Aucune tache detectée.")

courir=Tache("courir","il faut courir")
travailler=Tache("travailler","il faut travailler")
dormir=Tache("dormir","il faut dormir")

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(courir)
liste_taches.ajouterTache(travailler)
liste_taches.ajouterTache(dormir)
liste_taches.afficherListe()

liste_taches.supprimerTache(travailler)
liste_taches.afficherListe()
liste_taches.marquerCommeFinie(courir)
liste_taches.afficherListe()
liste_taches.filterListe("à faire")




    
