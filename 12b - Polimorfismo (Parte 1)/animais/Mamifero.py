from animais.Animal import Animal

class Mamifero(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros); 
        self.__corPelo = corPelo; 

    def getCorPelo(self): 
        return self.__corPelo; 

    def setCorPelo(self, value): 
        self.__corPelo = value; 
        return self.__corPelo; 

    def locomover(self):
        print('Correndo'); 

    def alimentar(self):
        print('Mamando'); 

    def emitirSom(self):
        print('Som de mamífero'); 

    def detalhes(self):
        super().detalhes();
        print(f'Cor do Pelo: {self.getCorPelo()}'); 
