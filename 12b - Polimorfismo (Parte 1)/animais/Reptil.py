from animais.Animal import Animal 

class Reptil(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corEscama=''):
        super().__init__(peso, idade, membros);
        self.__corEscama = corEscama; 

    def getCorEscama(self): 
        return self.__corEscama; 

    def setCorEscama(self, value): 
        self.__corEscama = value; 
        return self.__corEscama; 

    def locomover(self):
        print('Rastejando'); 

    def alimentar(self):
        print('Comendo Vegetais'); 

    def emitirSom(self):
        print('Som de Réptil'); 

    def detalhes(self):
        super().detalhes(); 
        print(f'Cor Escama: {self.getCorEscama()}'); 
