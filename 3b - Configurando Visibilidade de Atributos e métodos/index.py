class Caneta():
    def __init__(self, modelo, cor, ponta, carga, tampada):
        self.modelo = modelo; 
        self.cor = cor; 
        # self._ponta = ponta;  Privado 
        # self._carga = carga;  Privado
        # self._tampada = tampada;  Protegido
        # Aparentemente o atributo protegido é possível realizar alterações pontuais 
        self.ponta = ponta; 
        self.carga = carga; 
        self.tampada = tampada;

    def status(self): 
        print(f'Modelo: {self.modelo}'); 
        print(f'Uma caneta: {self.cor}'); 
        print(f'Ponta: {self.ponta}'); 
        print(f'Carga: {self.carga}'); 
        print(f'Está tampada? {self.tampada}'); 

    def rabiscar(self): 
        if (self.tampada == True): 
            print('ERRO: Não posso rabiscar'); 
        else: 
            print('Estou Rabiscando'); 

    def _tampar(self): 
        self.tampada = True;

    def _destampar(self): 
        self.tampada = False;

caneta1 = Caneta('Bic cristal', '', 0, 0, '');

caneta1.status();