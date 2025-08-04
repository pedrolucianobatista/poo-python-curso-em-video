from random import choice

class Luta(): 
    def __init__(self):
        self.desafiado = None;
        self.desafiante = None; 
        self.rounds = 5; 
        self.aprovado = False;

    def marcarLuta(self, l1, l2): 
        self.aprovado = True;
        if (l1.getNome() != l2.getNome() and l1.getCategoria() == l2.getCategoria()):
            if (self.aprovado):
                print(f'Briga marcada entre {l1.getNome()} e {l2.getNome()}'); 
                self.aprovado = True;
                self.desafiado = l1; 
                self.desafiante = l2
        else: 
            print('Sem briga guys');

    def lutar(self): 
        if (self.aprovado): 
            resultado = choice([0, 1, 2]); 
            resultado = 2; 
            if (resultado == 0): 
                print(f'Lutador {self.desafiado.getNome()} ganhou a luta'); 
                self.desafiado.ganharLuta(); 
                self.desafiante.perderLuta(); 
            elif (resultado == 1): 
                print(f'Lutador {self.desafiante.getNome()} ganhou a luta');
                self.desafiante.ganharLuta(); 
                self.desafiado.perderLuta(); 
            else: 
                print('Luta empatou =('); 
                self.desafiado.empatarLuta(); 
                self.desafiante.empatarLuta(); 
        else: 
            print('Não foi possível a realização da luta');
