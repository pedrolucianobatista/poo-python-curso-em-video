from classes.animais.Lobo import Lobo 

class Cachorro(Lobo): 
    def __init__(self, peso=0, idade=0, membros=0, corPelo=''):
        super().__init__(peso, idade, membros, corPelo); 

    def emitirSom(self):
        print('Au! Au! Au!'); 

    def reagir(self, *args): 
        if (isinstance(args[0], str)): 
            frase = args[0]; 
            if (frase == 'toma comida' or frase == 'Olá'): 
                print('Abanar e latir'); 
            else: 
                print('Rosnar'); 
        elif (isinstance(args[0], bool)): 
            dono = args[0]; 
            if (dono == True): 
                print('Abanar'); 
            else: 
                print('Rosnar e latir'); 
        elif (isinstance(args[0], int)):
            hora = args[0]; 
            if (hora < 12): 
                print('Abanar'); 
            elif (hora >= 18): 
                print('Ignorar'); 
            else: 
                print('Abanar e Latir'); 
        else: 
            idade = args[0], peso = args[1]; 
            if (idade < 5): 
                if (peso < 10): 
                    print('Abanar'); 
                else: 
                    print('Latir'); 
            else: 
                if (peso < 10): 
                    print('Rosnar'); 
                else: 
                    print('Ignorar'); 


# Verificar o tipo de argumento
# Fazer a primeira verificação com o primeiro parâmetro e verificar o tipo de instanciação algo assim 
# Realizar a sobrecarga no método envolvendo as especificações do python 