from abc import ABC, abstractmethod 

class Animal(ABC): 
    @abstractmethod 
    def __init__(self, peso=0, idade=0, membros=0):
        super().__init__(); 
        self._peso = peso; 
        self._idade = idade; 
        self._membros = membros; 

    def getPeso(self): 
        return self._peso; 

    def getIdade(self): 
        return self._idade; 

    def getMembros(self): 
        return self._membros; 

    def setPeso(self, value): 
        self._peso = value; 
        return self._peso;

    def setIdade(self, value): 
        self._idade = value; 
        return self._idade; 

    def setMembros(self, value): 
        self._membros = value; 
        return self._membros; 

    def emitirSom(self): 
        print('Som de animal'); 
