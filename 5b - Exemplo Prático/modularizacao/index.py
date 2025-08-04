class ContaBanco: 
    def __init__(self, numConta = 0000, tipo = '', dono = '', saldo = 0, status = False):
    # Atributos
        self.numConta = numConta; 
        self._tipo = tipo; 
        self.__dono = dono; 
        self.__saldo = saldo; 
        self.__status = status; 
    # Métodos Personalizados
    def abrirConta(self, t): 
        self.setTipo(t); 
        self.setStatus(True); 
        if (t == 'CC'): 
            self.setSaldo(50);
        elif (t == 'CP'): 
            self.setSaldo(150);
        print('Conta aberta com sucesso!');
    
    def fecharConta(self): 
        if (self.getSaldo() > 0): 
            print('Não posso fechar a conta, pois ela possui saldo');
        elif (self.getSaldo() < 0): 
            print('Não posso fechar a conta, pois ela possui débitos'); 
        else: 
            print('Conta fechada!');
            self.setStatus(False);
    
    # Verificar se há uma conta
    def depositarConta(self, value): 
        if (self.getStatus()): 
            self.setSaldo(self.getSaldo() + value); 
            print(f'Depósito realizado na conta de {self.getDono()}');
        else: 
            print('Impossível depositar em uma conta fechada!');

    # Verificar se há saldo suficiente
    def sacarConta(self, value): 
        if (self.getStatus()): 
            if (self.getSaldo() >= value): 
                self.setSaldo(self.getSaldo() - value); 
                print(f'Saque realizado na conta de {self.getDono()}');
            else: 
                print('Saldo insuficiente para saque'); 
        else: 
            print('Impossível sacar de uma conta fechada!');

    def pagarMensal(self): 
        v = 0; 
        if (self.getTipo() == 'CC'): 
            v = 12; 
        elif (self.getTipo() == 'CP'): 
            v = 20;
        if (self.getStatus()): 
            self.setSaldo(self.getSaldo() - v); 
            print(f'Mensalidade paga com sucesso por {self.getDono()}');
        else: 
            print('Impossível pagar uma conta fechada!'); 

    def setNumConta(self, value): 
        self.numConta = value;
    def getNumConta(self): 
        return self.numConta; 

    def setDono(self, value): 
        self.__dono = value;
    def getDono(self): 
        return self.__dono; 
    
    def setTipo(self, value):
        self._tipo = value;
    def getTipo(self):
        return self._tipo;

    def setStatus(self, value): 
        self.__status = value;
    def getStatus(self): 
        return self.__status;

    def setSaldo(self, value): 
        self.__saldo = value; 
    def getSaldo(self): 
        return self.__saldo;

    def allStatus(self): 
        print('-' * 30)
        print(f'Número Conta: {self.numConta}'); 
        print(f'Tipo Conta: {self._tipo}'); 
        print(f'Dono Conta: {self.__dono}');
        print(f'Saldo Conta: R${self.__saldo:.2f}'); 
        print(f'Status Conta: {self.__status}'); 
