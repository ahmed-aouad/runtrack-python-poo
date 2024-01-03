class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = ""

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Le montant des crédits est négatif")

    def __studentEval(self):
        if self.__credits >= 90:
            self.__level = "Excellent"
        elif self.__credits >= 80:
            self.__level = "Très bien"
        elif self.__credits >= 70:
            self.__level = "Bien"
        elif self.__credits >= 60:
            self.__level = "Passable"
        else:
            self.__level = "Insuffisant"

    def studentInfo(self):
        self.__studentEval()  # Update the level based on the current credits
        print(f"Nom = {self.__nom}")
        print(f"Prénom = {self.__prenom}")
        print(f"id = {self.__numero_etudiant}")
        print(f"Niveau = {self.__level}")

# Instanciation de l'objet représentant John Doe
john_doe = Student("Doe", "John", 145)

# Simulation de l'ajout de crédits et affichage des informations
john_doe.add_credits(10)
john_doe.add_credits(10)
john_doe.add_credits(10)  # Total de 30 crédits ajoutés
john_doe.studentInfo()  # Affichage des informations


    



