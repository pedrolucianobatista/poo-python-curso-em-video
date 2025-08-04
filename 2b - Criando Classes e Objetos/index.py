class Caneta: 
    def __init__(self, modelo, cor, ponta, carga, tampada):
        self.modelo = modelo; 
        self.cor = cor; 
        self.ponta = ponta; 
        self.carga = carga; 
        self.tampada = tampada; 

    def rabiscar(self): 
        if (self.tampada): 
            print('ERRO! Caneta está tampada');
        else: 
            print('Rabiscando heheh');

    def tampar(self): 
        self.tampada = True;

    def destampar(self): 
        self.tampada = False;

    def status(self): 
        print(f'Modelo: {self.modelo}\nCor: {self.cor}\nPonta: {self.ponta}\nCarga: {self.carga}\nEstá tampada? {self.tampada}');

caneta1 = Caneta('Bic', 'Preta', 1.5, 100, False); 
caneta2 = Caneta('Faber Castell', 'Azul', 1.8, 90, True);

caneta1.tampar(); 
caneta1.rabiscar();
caneta1.status();

print();

caneta2.destampar(); 
caneta2.rabiscar(); 
caneta2.status();

# Fazer a primeira caneta dando erro, e a segunda rabiscando bonitinho