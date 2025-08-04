class Visualizacao(): 
    def __init__(self, espectador='', filme=''):
        self.__espectador = espectador; 
        self.__filme = filme; 

        self.__espectador.viuMaisUm(); 
        self.__filme.setViews(self.__filme.getViews() + 1); 
        
    def getEspectador(self): 
        return self.__espectador; 

    def getFilme(self): 
        return self.__filme; 

    def setEspectador(self, value): 
        self.__espectador = value; 
        return self.__espectador; 

    def setFilme(self, value): 
        self.__filme = value;   
        return self.__filme; 

    def detalhes(self): 
        print(f'A pessoa {self.getEspectador()} está assistindo ao filme {self.getFilme()}'); 

    def avaliar(self, *args): 
        if (len(args) == 0): 
            self.__filme.setAvaliacao(5); 
        else: 
            valor = args[0]; 
            if (isinstance(valor, int)): 
                self.__filme.setAvaliacao(valor); 
            elif (isinstance(valor, float)): 
                porc = valor; 
                if porc <= 20: 
                    tot = 3; 
                elif porc <= 50: 
                    tot = 5; 
                elif porc <= 90: 
                    tot = 8; 
                else: 
                    tot = 10; 
                self.__filme.setAvaliacao(tot); 

# Usar o isinstance o args* e o vetor (eu acho)