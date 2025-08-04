class Lutador(): 
    # Atributos 
    def __init__(self, nome, nacionalidade, idade, altura, peso, vitorias = 0, derrotas = 0, empates = 0, categoria = ''):
        self.__nome = nome;
        self.__nacionalidade = nacionalidade; 
        self.__idade = idade; 
        self.__altura = altura;
        self.__peso = peso; 
        self.__categoria = categoria; 
        self.__vitorias = vitorias; 
        self.__derrotas = derrotas; 
        self.__empates = empates; 
    # Métodos Públicos 
    def ganharLuta(self): 
        self.setVitorias(self.getVitorias() + 1); 
    
    def perderLuta(self): 
        self.setDerrotas(self.getDerrotas() + 1); 
    
    def empatarLuta(self):
        self.setEmpates(self.getEmpates() + 1); 
    
    def apresentar(self): 
        print('-' * 35);
        print('APRESENTAÇÃO'.center(35));
        print('-' * 35);
        print(f'Lutador: {self.getNome()}'); 
        print(f'Origem: {self.getNacionalidade()}'); 
        print(f'{self.getIdade()} anos'); 
        print(f'{self.getAltura()}m de altura'); 
        print(f'Pesando: {self.getPeso()}Kg'); 
        print(f'Categoria: {self.getCategoria()}'); 
        print(f'Ganhou: {self.getVitorias()}'); 
        print(f'Perdeu: {self.getDerrotas()}'); 
        print(f'Empatou: {self.getEmpates()}'); 
    
    def status(self): 
        print(self.getNome()); 
        print(f'é um peso {self.getCategoria()}'); 
        print(f'{self.getVitorias()} vitórias'); 
        print(f'{self.getDerrotas()} derrotas'); 
        print(f'{self.getEmpates()} empates'); 

    # Métodos Especiais 
    def getNome(self): 
        return self.__nome; 

    def getNacionalidade(self): 
        return self.__nacionalidade; 

    def getIdade(self): 
        return self.__idade; 

    def getAltura(self): 
        return self.__altura; 

    def getPeso(self): 
        return self.__peso; 

    def getCategoria(self): 
        return self.__setCategoria(self.__peso); 

    def getVitorias(self): 
        return self.__vitorias; 

    def getDerrotas(self): 
        return self.__derrotas; 

    def getEmpates(self): 
        return self.__empates; 

    def setNome(self, value): 
        self.__nome = value; 
        return self.__nome; 

    def setNacionalidade(self, value): 
        self.__nacionalidade = value; 
        return self.__nome; 

    def setIdade(self, value): 
        self.__idade = value; 
        return self.__idade; 

    def setAltura(self, value): 
        self.__altura = value; 
        return self.__altura; 

    def setPeso(self, value): 
        self.__peso = value; 
        return self.__peso; 

    def __setCategoria(self, value): 
        if (self.getPeso() < 52.2): 
            value = 'Inválido'; 
        elif (self.getPeso() <= 70.3): 
            value = 'Leve'; 
        elif (self.getPeso() <= 83.9): 
            value = 'Médio'; 
        elif (self.getPeso() <= 120.2): 
            value = 'Pesado'; 
        else: 
            value = 'Inválido'; 
        return value; 

    def setVitorias(self, value): 
        self.__vitorias = value; 
        return self.__vitorias; 

    def setDerrotas(self, value): 
        self.__derrotas = value; 
        return self.__derrotas; 

    def setEmpates(self, value): 
        self.__empates = value; 
        return self.__empates; 

# Tirar o atributo referente a categoria