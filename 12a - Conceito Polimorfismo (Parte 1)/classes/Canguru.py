from classes.Mamifero import Mamifero 

class Canguru(Mamifero): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo); 

    def locomover(self):
        print('Saltando'); 

    def usarBolsa(self): 
        print('Usando bolsa'); 
