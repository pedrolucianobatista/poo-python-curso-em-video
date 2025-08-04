from classes import Pessoa; 

class Funcionario(Pessoa.Pessoa): 
    def __init__(self, nome = '', idade = 0, sexo = '', setor = '', trabalhando = False): 
        super().__init__(nome, idade, sexo);
        self.__setor = setor; 
        self.__trabalhando = trabalhando; 

    def mudaTrabalho(self): 
        self.__trabalhando = not self.__trabalhando; 

    def getSetor(self): 
        return self.__setor; 

    def getTrabalhando(self): 
        return self.__trabalhando; 

    def setSetor(self, value): 
        self.__setor = value; 
        return self.__setor; 

    def setTrabalhando(self, value): 
        self.__trabalhando = value; 
        return self.__trabalhando; 

    def detalhes(self):
        super().detalhes(); 
        print(f'Setor: {self.getSetor()}'); 
        print(f'Está trabalhando: {self.getTrabalhando()}'); 
