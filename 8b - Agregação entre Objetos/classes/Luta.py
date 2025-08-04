from random import choice

class Luta(): 
    def __init__(self):
    # Atributos
        self.desafiado = None; 
        self.desafiante = None; 
        self.rounds = 0; 
        self.aprovada = False; 
    # Métodos especiais 
    def getDesafiado(self): 
        return self.desafiado; 

    def setDesafiado(self, value): 
        self.desafiado = value; 
        return self.desafiado; 

    def getDesafiante(self): 
        return self.desafiante; 

    def setDesafiante(self, value): 
        self.desafiante = value; 
        return self.desafiante; 

    def getRounds(self): 
        return self.rounds; 

    def setRounds(self, value): 
        self.rounds = value; 
        return self.rounds; 

    def getAprovado(self): 
        return self.aprovada; 

    def setAprovado(self, value): 
        self.aprovada = value; 
        return self.aprovada; 
    # Métodos 
    def marcarLuta(self, l1, l2): 
        if (l1.getCategoria() == l2.getCategoria() and l1.getNome() != l2.getNome()): 
            self.aprovada = True; 
            self.desafiado = l1; 
            self.desafiante = l2; 
        else: 
            self.aprovada = False; 
            self.desafiado = None; 
            self.desafiante = None; 

    def lutar(self): 
        if (self.aprovada): 
            print('###  DESAFIADO  ###'); 
            self.desafiado.apresentar(); 
            print('###  DESAFIANTE  ###'); 
            self.desafiante.apresentar(); 

            aleatorio = choice([0, 1, 2]); 

            print('=' * 30);
            print('RESULTADO DA LUTA')
            if (aleatorio == 0): 
                print('Empatou!'); 
                self.desafiado.empatarLuta(); 
                self.desafiante.empatarLuta(); 
            elif (aleatorio == 1): 
                print(f'Vitória do {self.desafiado.getNome()}'); 
                self.desafiado.ganharLuta(); 
                self.desafiante.perderLuta(); 
            else: 
                print(f'Vitória do {self.desafiante.getNome()}'); 
                self.desafiante.ganharLuta(); 
                self.desafiante.perderLuta();  
            print('=' * 30);
        else: 
            print('A luta não pode acontecer!'); 
