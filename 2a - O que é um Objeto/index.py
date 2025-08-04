# Criar uma classe para a criação de um objeto caneta 

# Atributos, métodos e estado 
# Fazer uma verificação para ver se a caneta está destampada ou não 

class Caneta(): 
    def __init__(self, cor, marca, ponta, tampada):
        self.cor = cor; 
        self.marca = marca; 
        self.ponta = ponta; 
        self.tampada = tampada  # usa o valor recebido 

    def rabiscar(self): 
        if self.tampada: 
            print('Não pode rabiscar, está tampada'); 
        else: 
            print('Pode rabiscar, está destampada'); 

    def destampar(self): 
        self.tampada = False; 

    def tampar(self): 
        self.tampada = True;

c1 = Caneta("azul", "Bic", 0.5, True); 

c1.destampar();
