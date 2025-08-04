class Caneta: 
    def __init__(self, modelo = 'sem modelo', ponta = 0, cor = 'sem cor', tampada = True):
        self.modelo = modelo; 
        self._ponta = ponta; 
        self.cor = cor;
        self.tampada = tampada;
    
    def Caneta(self):   # Este é o método construtor 
        self.setModelo('Faber Castell'); 
        self.setCor('Preto'); 
        self.setPonta(0.7); 
        self.tampar();
        
    def status(self): 
        print('SOBRE A CANETA'); 
        print(f'Modelo: {self.modelo}'); 
        print(f'Ponta: {self._ponta}');
        print(f'Cor: {self.cor}');
        print(f'Tampada: {self.tampada}');

    def getModelo(self): 
        return self.modelo; 

    def setModelo(self, value): 
        self.modelo = value;

    def getPonta(self): 
        return self._ponta;

    def setPonta(self, value): 
        self._ponta = value; 
    
    def getCor(self): 
        return self.cor; 

    def setCor(self, value): 
        self.cor = value;

    def tampar(self): 
        if (not self.tampada): 
            print('TAMPADA');
            self.tampada = True; 
        else: 
            print('Não é possível tampa-la, pois ela já está tampada'); 

    def destampar(self): 
        if (not self.tampada): 
            print('ERRO! Já está destampada');
        else: 
            print('DESTAMPADA'); 
            self.tampada = False;

caneta1 = Caneta();

caneta1.Caneta();
caneta1.status();