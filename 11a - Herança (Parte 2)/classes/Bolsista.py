from classes.Aluno import Aluno 

class Bolsista(Aluno): 
    def __init__(self, nome='', idade=0, sexo='', matricula='', curso='', bolsa = 0):
        super().__init__(nome, idade, sexo, matricula, curso);
        self.__bolsa = bolsa; 

    def getBolsa(self): 
        return self.__bolsa; 

    def setBolsa(self, value): 
        self.__bolsa = value; 
        return self.__bolsa;

    def PagarMensalidade(self):
        super().PagarMensalidade(); 
        print('Pagamento da mensalidade realizado com sucesso'); 
        print('Observação: Bolsistas pagam apenas 50%'); 

    def RenovarBolsa(self): 
        self.setBolsa(self.getBolsa() + 1); 
        print('Bolsa renovada com sucesso'); 