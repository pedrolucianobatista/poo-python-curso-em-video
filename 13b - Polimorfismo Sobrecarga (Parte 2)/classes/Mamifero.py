from classes.Animal import Animal 

class Mamifero(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros); 
        self._corPelo = corPelo; 

    def getCorPelo(self): 
        return self._corPelo; 

    def setCorPelo(self, value): 
        self._corPelo = value; 
        return self._corPelo; 

    def emitirSom(self):
        print('Som de mamífero'); 
