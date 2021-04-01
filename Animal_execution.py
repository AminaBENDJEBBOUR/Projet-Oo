from Animal import Animal
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")

    #instanciez cet objet. Faites un print de ses attributs.
    chat = Animal(2, 40)
    print (chat)
    chat.se_deplacer() #Ajoutez une méthode se_deplacer( ) qui pour le moment ne fait rien. 
    

    chat = Animal(2, 40)
    chat.set_poids(-2)
 
    chat.se_deplacer() #Ajoutez une méthode se_deplacer( ) qui pour le moment ne fait rien. 