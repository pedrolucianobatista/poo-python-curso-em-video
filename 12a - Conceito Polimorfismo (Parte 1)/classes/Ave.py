from classes.Animal import Animal 

class Ave(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corPena=''):
        super().__init__(peso, idade, membros); 
        self.__corPena = corPena; 

    def getCorPena(self): 
        return self.__corPena; 

    def setCorPena(self, value): 
        self.__corPena = value; 
        return self.__corPena; 

    def locomover(self):
        print('Voando'); 

    def alimentar(self):
        print('Comendo frutas'); 

    def emitirSom(self):
        print('Som de ave'); 

    def fazerNinho(self): 
        print('Construiu um ninho'); 

    def detalhes(self):
        super().detalhes(); 
        print(f'Cor da pena: {self.getCorPena()}'); 
