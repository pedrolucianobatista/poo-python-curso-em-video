# Identifique dois objetos físicos do seu ambiente e classifique-os. 
# Identifique dois objetos conceituais do seu dia-a-dia e classique-os. 

# Definir atributos, métodos e estado 

# Classe Concreta

class Celular(): 
    def __init__(self, marca, height, width, ligado):
        self.marca = marca; 
        self.height = height; 
        self.width = width; 
        self.ligado = ligado; 

    def ligar(self):
        self.ligado = True;

    def desligar(self):
        self.ligado = False;

    def isOn(self):
        if (not self.ligado): 
            print('O celular está desligado'); 
        else: 
            print('O celular está ligado');

celular1 = Celular('Samsung', 280, 600, False);

# Classe Abstrata

class Estudar(): 
    def __init__(self, materia, tema, duracao, ocupado):
        self.materia = materia; 
        self.tema = tema; 
        self.duracao = duracao; 
        self.ocupado = ocupado;

    def isStudying(self): 
        if (not self.ocupado): 
            print('O caba está estudando haha'); 
        else: 
            print('O caba não está estudando haha');

estudo1 = Estudar('Banco de dados', 'Sintaxe de Sql', 45, False);

estudo1.isStudying();