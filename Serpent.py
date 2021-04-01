
from Animal import Animal

class Serpent(Animal): #[Héritage] Crée
    is_serpent= True
    def se_deplacer(self):#[Polymorphisme]
        print ("je rampe")

    def __str__(self):
       
        return f"Le poids de l'animalserpent est de : {self.get_poids()} kg. La taille de serpent est de : {self.get_taille()} cm"
