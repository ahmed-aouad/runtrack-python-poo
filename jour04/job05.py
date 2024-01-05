class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return 3.14159 * self.radius ** 2
    
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

rectangle = Rectangle(8, 5)
print("Aire du rectangle:", rectangle.aire())

cercle = Cercle(3)
print("Aire du cercle:", cercle.aire())