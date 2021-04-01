class Animal:
    
    poids=0
    taille=0

    def __init__(self,poids, taille):
        self.__poids=poids
        self.__taille=taille
            
    def se_deplacer(self):
        pass
   
    def get_poids(self): #[Encapsulation] 
        return self.__poids


    def set_poids(self, poids):#[Encapsulation] 
        if poids<0:
            raise ValueError  
             
        self.__poids = poids

     
    def __str__(self):
         
        return f"Le poids de l'animal est de : {self.__poids} kg. La taille de l'animal est de : {self.__taille} cm"
 


     