from classes import Pessoa

class Professor(Pessoa.Pessoa): 
    def __init__(self, nome = '', idade = 0, sexo = '', especialidade = '', salario = 0): 
        super().__init__(nome, idade, sexo); 
        self.__especialidade = especialidade; 
        self.__salario = salario; 

    def receberAumento(self, aum): 
        self.__salario += aum;

    def getEspecialidade(self): 
        return self.__especialidade; 

    def getSalario(self): 
        return self.__salario; 

    def setEspecialidade(self, value): 
        self.__especialidade = value; 
        return self.__especialidade; 

    def setSalario(self, value): 
        self.__salario = value; 
        return self.__salario; 

    def detalhes(self): 
        super().detalhes(); 
        print(f'Especialidade: {self.getEspecialidade()}'); 
        print(f'Salário: R${self.getSalario():.2f}');
