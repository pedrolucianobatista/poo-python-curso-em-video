from animais.Animal import Animal

class Peixe(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corEscama=''):
        super().__init__(peso, idade, membros);
        self.__corEscama = corEscama; 

    def getCorEscama(self): 
        return self.__corEscama; 

    def setCorEscama(self, value): 
        self.__corEscama = value; 
        return self.__corEscama; 

    def locomover(self):
        print('Nadando'); 

    def alimentar(self):
        print('Comendo substãncias'); 

    def emitirSom(self):
        print('Peixe não faz som'); 

    def soltarBolha(self): 
        print('Soltou uma bolha'); 

    def detalhes(self):
        super().detalhes(); 
        print(f'Cor da Escama: {self.getCorEscama()}'); 
