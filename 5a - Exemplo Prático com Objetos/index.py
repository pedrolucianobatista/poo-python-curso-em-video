class ContaBancaria(): 
    def __init__(self, numConta = '', tipo = '', dono = '', saldo = 0, status = False):
        self.numConta = numConta; 
        self._tipo = tipo; 
        self.__dono = dono; 
        self.__saldo = saldo; 
        self.__status = status;

        if (self._tipo.strip().lower() == 'cc'): 
            self.__saldo += 50;
        elif (self._tipo.strip().lower() == 'cp'): 
            self.__saldo += 150; 
    
    def getNumConta(self): 
        print(f'Número Conta: {self.numConta}');

    def setNumConta(self, value): 
        self.numConta = value; 

    def getTipo(self): 
        print(f'Tipo Conta: {self._tipo}');

    def setTipo(self, value): 
        self._tipo = value; 
        if (self._tipo.strip().lower() == 'cc'): 
            self.__saldo += 50;
        elif (self._tipo.strip().lower() == 'cp'): 
            self.__saldo += 150;

    def getDono(self): 
        print(f'Dono Conta: {self.__dono}'); 
    
    def setDono(self, value): 
        self.__dono = value; 

    def getSaldo(self): 
        print(f'Saldo Conta: R${self.__saldo:.2f}');

    def setSaldo(self, value): 
        self.__saldo = value;

    def getStatus(self): 
        print(f'Conta Aberta? {self.__status}'); 
    
    def setStatus(self, value): 
        self.__status = value; 
    
    def abrirConta(self): 
        if (not self.__status): 
            self.__status = True; 
            print('Conta aberta com sucesso!'); 
        else: 
            print('Conta já foi aberta, não é possível abrir outra'); 

    def fecharConta(self):
        if (self.__status and self.__saldo == 0): 
            self.__status = False; 
            print('Conta fechada com sucesso'); 
        elif (not self.__status): 
            print('Você ainda não tem conta, diante disso não consigo fecha-la'); 
        else: 
            print('Você ainda possui dinheiro na conta, ou débitos e por isso não conseguimos fechar a conta')

    def depositar(self, value): 
        if (not self.__status): 
            print(f'Não é possível depositar R${value:.2f}, pois você não possui conta bancária');
        else: 
            self.__saldo += value;
            print(f'R${value:.2f} depositado com sucesso, agora o seu saldo é R${self.__saldo:.2f}');
    # Obs: Tentar colocar de erros para a passagem de parâmetros;

    def sacar(self, value): 
        if (not self.__status): 
            print(f'Não é possível sacar R${value:.2f}, pois você não possui conta bancária'); 
        else: 
            if (value > self.__saldo): 
                print(f'Valor do saque é maior do que você guardado R${self.__saldo:.2f}');
            else: 
                self.__saldo -= value; 
                print(f'R${value:.2f} sacado com sucesso, agora o seu saldo é R${self.__saldo:.2f}');

    def pagarMensal(self):             
        if (not self.haConta()):
            return;
        else: 
            if (self._tipo.strip().lower() == 'cc' and self.__saldo >= 12): 
                self.__saldo -= 12; 
                print('Pagamento mensal de R$12,00 realizado'); 
            elif (self._tipo.strip().lower() == 'cp' and self.__saldo >= 20): 
                self.__saldo -= 20; 
                print('Pagamento mensal de R$20,00 realizado'); 
            elif (self.__saldo < 12 or self.__saldo < 20): 
                print('Saldo insuficiente!')    # Ou tipo conta inexistente 
            else: 
                print('Tipo de conta inválido')

    def haConta(self): 
        if (not self.__status): 
            print('ERRO! Você não possui conta');
            return False; 
        return True;

    def statusAtributos(self): 
        print('-' * 30); 
        print('RESUMO CONTA BANCÁRIA'.center(30));
        print('-' * 30); 
        self.getDono();
        print(f'Número Conta: {self.numConta}'); 
        print(f'Tipo Conta: {self._tipo}'); 
        print(f'Saldo Conta: {self.__saldo}');
        print(f'Conta Aberta? {self.__status}'); 
        print('-' * 30); 

contaJubileu = ContaBancaria(); 
contaCreuza = ContaBancaria(); 

contaJubileu.pagarMensal();

contaJubileu.setStatus(True);
contaJubileu.setNumConta(1577);
contaJubileu.setTipo('cp');
contaJubileu.setDono('Jubileu'); 
contaJubileu.depositar(300);
contaJubileu.pagarMensal();
contaJubileu.statusAtributos();

contaCreuza.setStatus(True); 
contaCreuza.setNumConta(1466); 
contaCreuza.setTipo('cc'); 
contaCreuza.setDono('Creuza');
contaCreuza.depositar(500); 
contaCreuza.sacar(100); 
contaCreuza.pagarMensal();
contaCreuza.statusAtributos(); 