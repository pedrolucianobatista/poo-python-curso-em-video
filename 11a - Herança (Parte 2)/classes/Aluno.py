from classes.Pessoa import Pessoa

class Aluno(Pessoa): 
    def __init__(self, nome = '', idade = 0, sexo = '', matricula = '', curso = ''):
        super().__init__(nome, idade, sexo); 
        self.__matricula = matricula; 
        self.__curso = curso; 

    def getMatricula(self): 
        return self.__matricula; 

    def getCurso(self): 
        return self.__curso; 

    def setMatricula(self, value): 
        self.__matricula = value; 
        return self.__matricula; 

    def setCurso(self, value): 
        self.__curso = value; 
        return self.__curso; 

    def PagarMensalidade(self): 
        print('Pagamento da mensalidade realizado com sucesso'); 
