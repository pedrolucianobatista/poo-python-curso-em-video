class Pessoa: 
    def __init__(self, nome, idade, sexo):  
        self.__nome = nome; 
        self.__idade = idade; 
        self.__sexo = sexo; 

    def fazerAniv(self): 
        self.__idade = self.__idade + 1; 

    def getNome(self): 
        return self.__nome; 

    def getIdade(self): 
        return self.__idade; 

    def getSexo(self): 
        return self.__sexo; 

    def setNome(self, value): 
        self.__nome = value; 
        return self.__nome; 

    def setIdade(self, value): 
        self.__idade = value; 
        return self.__idade; 

    def setSexo(self, value): 
        self.__sexo = value; 
        return self.__sexo; 

class Aluno(Pessoa): 
    def __init__(self, matr, curso):
        self.__matr = matr; 
        self.__curso = curso; 

    def canelarMatr(self): 
        self.__matr = False; 
        print('Matrículo cancelada com sucesso'); 

    def getMatr(self): 
        return self.__matr; 

    def getCurso(self): 
        return self.__curso; 

    def setMatr(self, value): 
        self.__matr = value; 
        return self.__matr; 

    def setCurso(self, value): 
        self.__curso = value; 
        return self.__curso; 

class Professor(Pessoa): 
    def __init__(self, especialidade, salario):
        self.__especialidade = especialidade; 
        self.__salario = salario; 

    def receberAum(self, value): 
        self.__salario += value; 

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

class Funcionario(Pessoa): 
    def __init__(self, setor, trabalhando):
        self.__setor = setor; 
        self.__trabalhando = trabalhando; 

    def mudarTrabalho(self): 
        self.__setor = 'Setor alterado'; 

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

p1 = Pessoa('Pedro', 21, 'm'); 
p2 = Aluno(1, 'ADS'); 
p3 = Professor('Matemática', 3500); 
p4 = Funcionario('Administrativo', True); 

p1.setNome('Pedro'); 
p2.setNome('Maria'); 
p3.setNome('Cláudio'); 
p4.setNome('Fabiana'); 

p2.setCurso('Informática'); 
p3.setSalario(2500.75); 
p4.setSetor('Estoque'); 
