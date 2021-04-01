
from Animal import Animal
from Oiseau import Oiseau
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    cygne= Oiseau (3,90,30)
    print(f"Le poids de l'oiseau est de : {cygne.poids} kg")
    print(f"La taille de l'oiseau est de : {cygne.taille} cm")
    #[Super fonction]
    print(f"La altitude_max  de l'oiseau est de : {cygne.altitude_max} m")
    cygne.se_deplacer()