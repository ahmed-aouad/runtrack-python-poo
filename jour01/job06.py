class Animal:

    def __init__(self, age):
        self.age = age 

    def vieillir(self):
        self.age += 1

    def nommer(self, prenom):   
        self.prenom = prenom
        print("L'animal se nomme ", self.prenom ) 


animal = Animal(0) 
print("l'age de l'animal", animal.age, "age")

animal.vieillir()
print("l'age de l'animal", animal.age, "age")

animal.nommer("Luna")



