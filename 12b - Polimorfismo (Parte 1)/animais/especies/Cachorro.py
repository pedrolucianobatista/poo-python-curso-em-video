from animais.Mamifero import Mamifero 

class Cachorro(Mamifero): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo); 

    def emitirSom(self):
        print('Au! Au! Au!'); 
