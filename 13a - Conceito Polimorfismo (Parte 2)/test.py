from abc import ABC, abstractmethod; 

class Animal(ABC): 
    @abstractmethod
    def __init__(self, peso=0, idade=0, membros=0):
        self._peso = peso; 
        self._idade = idade; 
        self._membros = membros; 

    def getPeso(self): 
        return self._peso; 
    
    def getIdade(self): 
        return self._idade; 

    def getMembros(self): 
        return self._membros; 

    def setPeso(self, value): 
        self._peso = value; 
        return self._peso; 

    def setIdade(self, value):  
        self._idade = value; 
        return self._idade; 

    def setMembros(self, value): 
        self._membros = value; 
        return self._membros; 

    def emitirSom(self): 
        print('Som de Mamífero'); 

class Mamifero(Animal): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros); 
        self._corPelo = corPelo; 

    def getCorPelo(self): 
        return self._corPelo; 

    def setCorPelo(self, value): 
        self._corPelo = value; 
        return self._corPelo; 

    def emitirSom(self):
        return super().emitirSom(); 

class Lobo(Mamifero): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo);

    def emitirSom(self):
        print('Auuuuuuuuuuuu'); 

class Cachorro(Lobo): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo); 

    def reagir(self, *args): 
        if len(args) == 1: 
            if isinstance(args[0], str): 
                frase = args[0]; 
                if frase in ['toma comida', 'olá']: 
                    print('Abanar e latir'); 
                else: 
                    print('Rosnar'); 
            elif isinstance(args[0], int): 
                hora = args[0]; 
                if hora < 12: 
                    print('Abanar'); 
                elif hora >= 18: 
                    print('Ignorar'); 
                else: 
                    print('Abanar e latir'); 
            elif isinstance(args[0], bool): 
                dono = args[0]; 
                if dono: 
                    print('Abanar'); 
                else: 
                    print('Rosnar e latir'); 
        elif len(args) == 2: 
            idade, peso = args 
            if idade < 5: 
                if peso < 10: 
                    print('Abanar'); 
                else: 
                    print('Latir'); 
            else: 
                if peso < 10: 
                    print('Rosnar');
                else: 
                    print('Ignorar'); 

    def emitirSom(self):
        print('Au! Au! Au!'); 

c1 = Cachorro(); 

c1.reagir('olá'); 
c1.reagir('Vai apanhar'); 
c1.reagir(11, 45); 
c1.reagir(21, 00); 
c1.reagir(True); 
c1.reagir(False); 
c1.reagir(2, 12.5); 
c1.reagir(17, 4.5); 

# Polimorfismo por sobrecarga