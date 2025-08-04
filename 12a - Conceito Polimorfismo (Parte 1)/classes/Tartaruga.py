from classes.Reptil import Reptil 

class Tartaruga(Reptil): 
    def __init__(self, peso=0, idade=0, membros=0, corEscama=''):
        super().__init__(peso, idade, membros, corEscama); 

    def locomover(self):
        print('Andando beeeem devagar'); 
 