from abc import ABC, abstractmethod

class Pessoa(ABC): 
    @abstractmethod
    def __init__(self, nome='', idade=0, sexo='', experiencia=0):
        self._nome = nome; 
        self._idade = idade; 
        self._sexo = sexo; 
        self._experiencia = experiencia; 

    def getNome(self): 
        return self._nome; 

    def getIdade(self): 
        return self._idade; 

    def getSexo(self): 
        return self._sexo; 

    def getExperiencia(self): 
        return self._experiencia; 

    def setNome(self, value): 
        self._nome = value; 
        return self._nome; 

    def setIdade(self, value): 
        self._idade = value; 
        return self._idade; 

    def setSexo(self, value): 
        self._sexo = value; 
        return self._sexo; 

    def setExperiencia(self, value): 
        self._experiencia = value ; 
        return self._experiencia; 

    def ganharExp(self, value): 
        self.setExperiencia(self.getExperiencia() + value); 

    def detalhes(self): 
        print(f'Nome: {self.getNome()}'); 
        print(f'Idade: {self.getIdade()} anos'); 
        print(f'Sexo: {self.getSexo()}'); 
        print(f'Experiência: {self.getExperiencia()}'); 
