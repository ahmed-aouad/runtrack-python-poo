class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def SePresenter(self):
        return self.nom + self.prenom

personne1=Personne("john", " Doe")
personne2=Personne("jean", " Dupond")

print("je suis", personne1.SePresenter())
print("je suis", personne2.SePresenter())

      