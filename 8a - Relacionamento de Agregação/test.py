class Endereço: 
    def __init__(self, rua, cidade, estado):
        self.rua = rua; 
        self.cidade = cidade; 
        self.estado = estado; 

    def mostrar_endereco(self): 
        return f'{self.rua}, {self.cidade} - {self.estado}'; 

class Pessoa: 
    def __init__(self, nome, idade, endereco):
        self.nome = nome; 
        self.idade = idade; 
        self.endereco = endereco; 

    def apresentar(self): 
        print(f'Nome: {self.nome}'); 
        print(f'Idade: {self.idade}'); 
        print(f'Endereço: {self.endereco.mostrar_endereco()}');

endereco1 = Endereço('Rua das Flores', 'Belo Horizonte', 'MG'); 

pessoa1 = Pessoa('Ana', 30, endereco1); 

pessoa1.apresentar(); 