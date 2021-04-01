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
    
    

   
    #[Association]
    
    canard = Animal(1,30)
    chat = Animal(2,40)
    
    animaux = Zoo([chat, canard])
    
    singe = Animal (2,8)
    animaux.add_animal(singe)
    #print(' '.join([str(i) for i in animaux]))
    #print(animaux)


    lyon = Animal(90,80)
    tigre= Animal(70,70)
    renard=Animal(20,20)
    animaux_sauvage=Zoo([lyon, tigre, renard])
    zoo=animaux+animaux_sauvage
    #print(zoo)
    #print(' '.join([str(i) for i in zoo])) 

    #cygne= Oiseau (3,90,30)
    #anaconda= Serpent(3,4)
    #zoo_1 =[cygne, anaconda]
    #chat = Animal(2,40)
    #zoo_1.append(chat)

    #print (zoo_1)
    #print(' '.join([str(i) for i in zoo_1]))


    #canard = Animal(1,30)
    #ours= Animal(300,250)
    #singe=Animal(20,50)
    #zoo_2=[canard, ours, singe]
    #zoo_3=zoo_1+zoo_2
    #print(zoo_1+zoo_2)
    
    #zoo_3=zoo_1.__add__(zoo_2)
    #print(zoo_3)
    #print(' '.join([str(i) for i in zoo_3]))      
