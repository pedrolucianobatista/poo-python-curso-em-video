# Realizar os testes da aula com base nos tipos de consultas 

class Caneta(): 
    def __init__(self, cor, marca, carga, tampada):
        # Deixar a carga com o aspecto protegido para verificar as diferenças 

        self.cor = cor; 
        self.marca = marca; 
        self._carga = carga;
        self.__tampada = tampada;

    def status(self): 
        print(f'Cor: {self.cor}'); 
        print(f'Marca: {self.marca}'); 
        print(f'Carga: {self._carga}'); 
        print(f'Tampada: {self.__tampada}'); 

    def _rabiscar(self): 
        if (self.__tampada): 
            print('Não é possível rabiscar, pois a caneta está tampada'); 
        else: 
            print('Estou rabiscando heheh'); 

    def tampar(self): 
        if (self.__tampada): 
            print('A caneta já está tampada'); 
        else: 
            print('Acabei de tampar'); 
            self.__tampada = True;

    def destampar(self): 
        if (not self.__tampada): 
            print('Ela já está destampada'); 
        else: 
            print('Acabei de destampar'); 
            self.__tampada = False;

 
caneta1 = Caneta('Azul', 'Bic', 90, True); 

caneta1.status();
caneta1._rabiscar();

# Realizar a função para a verificação da possibilidade de rabiscar com a caneta em si 