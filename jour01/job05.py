class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("les coordonnées sont" , self.x , self.y)   

    def afficherX(self):
        print("La coordonnée X est: ", self.x)

    def afficherY(self):
        
        print("la coordonnée Y est: ", self.y)  

    def changerX(self, x):
        self.x = x
        print("la nouvelle coordonnée Y est: ", self.x)  

    def changerY(self, y):
        self.y = y
        print("la nouvelle coordonnée Y est: ", self.y)  

point = Point(10, 5) 

point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(25)
point.changerY(12)
        

