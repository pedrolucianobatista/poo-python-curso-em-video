from classes.Pessoa import Pessoa; 

class Bolsista(Pessoa): 
    def __init__(self, nome='', idade=0, sexo='', bolsa=''):
        super().__init__(nome, idade, sexo)
        self.__bolsa = bolsa; 

    def getBolsa(self): 
        return self.__bolsa; 

    def setBolsa(self, value): 
        self.__bolsa = value; 
        return self.__bolsa; 

    def renovarBolsa(self): 
        print(f'Renovando bolsa de {self.getNome()}'); 

    def pagarMensalidade(self): 
        print(f'{self.getNome()} é bolsista! Pagamento facilitado!');

    def detalhes(self):
        super().detalhes(); 
        print(f'Bolsa: {self.getBolsa()}'); 
