from Pessoa import Pessoa; 

class Gafanhoto(Pessoa): 
    def __init__(self, nome='', idade=0, sexo='', experiencia=0, login='', totAssistido=0):
        super().__init__(nome, idade, sexo, experiencia); 
        self.__login = login; 
        self.__totAssistido = totAssistido; 

    def getLogin(self): 
        return self.__login; 

    def getTotAssistido(self): 
        return self.__totAssistido; 

    def setLogin(self, value): 
        self.__login = value; 
        return self.__login; 

    def setTotAssistido(self, value): 
        self.__totAssistido = value; 
        return self.__totAssistido; 

    def viuMaisUm(self): 
        self.setTotAssistido(self.getTotAssistido() + 1); 

    def detalhes(self):
        super().detalhes(); 
        print(f'Login: {self.getLogin()}'); 
        print(f'Total do vídeo que foi assistido: {self.getTotAssistido()}'); 
