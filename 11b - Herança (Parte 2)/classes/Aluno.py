from classes.Pessoa import Pessoa

class Aluno(Pessoa): 
    def __init__(self, nome='', idade=0, sexo='', matricula='', curso='',):
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

    def pagarMensalidade(self): 
        print(f'Pagando mensalidade do aluno {self.getNome()}'); 

    def detalhes(self):
        super().detalhes();
        print(f'Matrícula: {self.getMatricula()}'); 
        print(f'Curso: {self.getCurso()}'); 
