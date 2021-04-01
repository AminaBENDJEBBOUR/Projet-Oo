from Animal import Animal 
class Zoo:
    def __init__(self,zoo_1):#[Association] 
        #Cette classe possède un attribut qui est une liste d’objets de type Animal.
        #Vous passerez la liste d’animaux comme paramètres lors de l’instanciation de l’objet.
        self.zoo_1=[]
        for animal in zoo_1:
            if not isinstance(animal, Animal):
                raise TypeError
            else:
                self.zoo_1.append(animal)
    
    def add_animal(self,animal):#Vous définirez une méthode permettant d’ajouter un objet de type Animal à une instance de Zoo.
        self.zoo_1.append(animal)
          
          
    #def __str__(self):
        #return f'({self.zoo_1})'

    def __add__(self, other):        
        if isinstance(other, Zoo):            
            return Zoo(self.liste_animal+other.liste_animal)       
        else:           
            return None

#def add_zoo(self,zoo_2) :
        
        #if isinstance(zoo_2,Zoo) :
            #self.zoo_1 += zoo_2.zoo_1
            # print(" Le zoo contient maintenant", len(self.zoo_1)) 
        #else :
            #raise ValueError(str(zoo_2))     

#def __add__(self,other) :
        
    #if isinstance(other,Zoo) :
        #print(" Le nouveau zoo contient", len(self.zoo_1 + other.zoo_1)) 
        #return self.zoo_1 + other.zoo_1
    #else :
        #raise ValueError(str(zoo_2)+' is not of class Zoo. Replace it.')
    
    #def __add__(self, other):
        #return self.zoo + other.zoo
