class Pessoa(): 
    def __init__(self, nome = '', idade = 0, sexo = ''):  
        self.__nome = nome; 
        self.__idade = idade; 
        self.__sexo = sexo; 

    def getNome(self): 
        return self.__nome; 

    def setNome(self, value): 
        self.__nome = value; 
        return self.__nome; 

    def getIdade(self): 
        return self.__idade; 

    def setIdade(self, value): 
        self.__idade = value; 
        return self.__idade; 

    def getSexo(self): 
        return self.__sexo; 

    def setSexo(self, value): 
        self.__sexo = value; 
        return self.__sexo; 

    def fazerAniver(self): 
        return self.setIdade(self.getIdade() + 1); 
