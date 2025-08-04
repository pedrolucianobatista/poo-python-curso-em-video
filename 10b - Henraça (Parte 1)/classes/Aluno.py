from classes import Pessoa

class Aluno(Pessoa.Pessoa): 
    def __init__(self, nome = '', idade = 0, sexo = '', mat = '', curso = ''): 
        super().__init__(nome, idade, sexo);
        self.__mat = mat; 
        self.__curso = curso; 

    def cancelarMatr(self): 
        print('Matrícula será cancelada'); 

    def getMat(self): 
        return self.__mat; 

    def getCurso(self): 
        return self.__curso; 

    def setMat(self, value): 
        self.__mat = value; 
        return self.__mat; 

    def setCurso(self, value): 
        self.__curso = value; 
        return self.__curso; 

    def detalhes(self): 
        super().detalhes(); 
        print(f'Matéria: {self.getMat()}'); 
        print(f'Curso: {self.getCurso()}'); 
