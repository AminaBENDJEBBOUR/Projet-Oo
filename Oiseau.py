
from Animal import Animal
class  Oiseau(Animal): #[Héritage] Crée
    is_oiseau= True
    def se_deplacer(self):#[Polymorphisme]
        print ("je vole")

   #[Mot clé “super”] 
    def __init__(self, poids, taille,altitude_max ):
        super().__init__(poids,taille)
        self.altitude_max= altitude_max
        #print(self.poids,self.taille,self.altitude_max)

    def __str__(self):
       
        return f"Le poids de l'oiseau est de : {self.get_poids()} kg. La taille de l'animaloiseau est de : {self.get_taille()} cm"
               

