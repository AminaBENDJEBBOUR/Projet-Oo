from Animal import Animal
from Zoo import Zoo
from Oiseau import Oiseau
from Serpent import Serpent
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
    #[Association]
    
    cygne= Oiseau (3,90,30)
    anaconda= Serpent(3,4)
    zoo_1 =[cygne, anaconda]
    chat = Animal(2,40)
    zoo_1.append(chat)
    print (chat)
    print (zoo_1)
    
    #giraf=Animal(200,900)
    #lion=Animal(100,100)
    #zoo_1 =[giraf, lion]
    
    #elephant = Animal(200,900)
    #zoo_1.append(elephant)
    #print (zoo_1)


    canard = Animal(1,30)
    ours= Animal(300,250)
    singe=Animal(20,50)
    zoo_2=[canard, ours, singe]
    #print(zoo_1+zoo_2)
    
    zoo_3=zoo_1.__add__(zoo_2)
    print(zoo_3)
