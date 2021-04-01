from Animal import Animal
from Serpent import Serpent
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    anaconda= Serpent(3,4)
    print(f"Le poids de serpent anaconda est de : {anaconda.poids} kg")
    print(f"La taille de serpent anaconda est de : {anaconda.taille} cm")
    anaconda.se_deplacer()