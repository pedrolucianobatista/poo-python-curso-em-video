from animais.Peixe import Peixe 

class Goldfish(Peixe): 
    def __init__(self, peso=0, idade=0, membros=0, corEscama=''):
        super().__init__(peso, idade, membros, corEscama); 

