from classes.Pessoa import Pessoa 

class Visitante(Pessoa): 
    def __init__(self, nome='', idade=0, sexo=''):
        super().__init__(nome, idade, sexo);