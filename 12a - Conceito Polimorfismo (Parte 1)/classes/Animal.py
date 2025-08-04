from abc import ABC, abstractmethod

class Animal(ABC): 
    @abstractmethod
    def __init__(self, peso=0, idade=0, membros=0):
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

    def locomover(self): 
        print('Estou me locomovendo'); 

    def alimentar(self): 
        print('Estou comendo'); 

    def emitirSom(self): 
        print('Estou emitindo som'); 

    def detalhes(self): 
        print(f'Peso: {self.getPeso()}Kg'); 
        print(f'Idade: {self.getIdade()} anos'); 
        print(f'Membros: {self.getMembros()}'); 
