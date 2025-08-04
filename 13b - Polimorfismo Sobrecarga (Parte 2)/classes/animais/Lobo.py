from classes.Mamifero import Mamifero 

class Lobo(Mamifero): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo); 

    def emitirSom(self):
        print('Auuuuuuuuuuu!'); 
