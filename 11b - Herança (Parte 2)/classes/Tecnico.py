from classes.Pessoa import Pessoa 

class Tecnico(Pessoa): 
    def __init__(self, nome='', idade=0, sexo='', registroProfissional=0):
        super().__init__(nome, idade, sexo);
        self.__registroProfissional = registroProfissional; 

    def getRegistroProfissional(self): 
        return self.__registroProfissional; 
    
    def setRegistroProfissional(self, value): 
        self.__registroProfissional = value; 
        return self.__registroProfissional; 

    def praticar(self): 
        print(f'Técnico {self.getNome()} está praticando');

    def detalhes(self):
        super().detalhes(); 
        print(f'Registro Profissional: {self.getRegistroProfissional()}');
