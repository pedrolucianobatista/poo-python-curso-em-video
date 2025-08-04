class Estante: 
    def __init__(self, cor, marca):
        self.cor = cor; 
        self.marca = marca; 
        # self.qtdPortas = qtdPortas; 
        # self.qtdGavetas = qtdGavetas; 

    def getCor(self): 
        return self.cor; 

    def getMarca(self): 
        return self.marca;
# Esses são os métodos getters na prática, basicamente são utilizados para as consultas em geral 
# Usar a questão da passagem de parâmetro para facilitar na alteração do atributo no caso do set

    def setCor(self, value): 
        self.cor = value;

    def setMarca(self, value): 
        self.marca = value;

# Métodos: Abrir/fechar porta; abrir/fechar gaveta; colocar/tirar objetos; 
# Usar a classe estante para utilizar na prática os getters e setters 

estante1 = Estante('Marrom', 'Enya'); 

estante1.setCor('Azul'); 
estante1.setMarca('Madeira'); 

print(f'Nova Cor:',estante1.getCor(),'\nNova Marca:',estante1.getMarca());