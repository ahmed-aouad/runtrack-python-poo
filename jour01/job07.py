class personnage:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def haut(self):
        self.y-=1
    def bas(self):
        self.y+=1
    def gauche(self):
        self.x-=1
    def droit(self):
        self.x+=1
    def position(self):
        print(f"({self.x} {self.y})")

#exemple de postion
perso = personnage(20, 5) 
perso.position()
perso.droit()
perso.bas()
perso.position()
