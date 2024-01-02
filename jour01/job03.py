class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition de nombre1 et nombre2 est: {resultat}")

# Instanciation de la classe Operation
operation = Operation(12, 3)

# Appel de la méthode addition pour afficher le résultat
operation.addition()
