class Lutador(): 
    def __init__(self, nome = '', nacionalidade = '', idade = 0, altura = 0, peso = 0, vitoria = 0, derrotas = 0, empates = 0):
        self.__nome = nome; 
        self.__nacionalidade = nacionalidade; 
        self.__idade = idade; 
        self.__altura = altura; 
        self.__peso = peso; 
        self.__vitoria = vitoria; 
        self.__derrotas = derrotas; 
        self.__empates = empates; 

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

    def getVitoria(self): 
        return self.__vitoria; 

    def getDerrotas(self): 
        return self.__derrotas; 

    def getEmpates(self): 
        return self.__empates; 

    def getCategoria(self): 
        return self.setCategoria(self.__peso);

    def setNome(self, value): 
        self.__nome = value; 

    def setNacionalidade(self, value): 
        self.__nacionalidade = value; 

    def setIdade(self, value): 
        self.__idade = value; 

    def setAltura(self, value): 
        self.__altura = value; 

    def setPeso(self, value): 
        self.__peso = value; 
        self.setCategoria(self.__peso); 

    def setCategoria(self, value): 
        if (self.getPeso() < 52.2): 
            value = 'Inválido';
        elif (self.getPeso() < 56.7): 
            value = 'Mosca'; 
        elif (self.getPeso() <= 61.2): 
            value = 'Galo';
        elif (self.getPeso() <= 65.8): 
            value = 'Pena'; 
        elif (self.getPeso() <= 70.3): 
            value = 'Leve'; 
        elif (self.getPeso() <= 77.1): 
            value = 'Meio-Médio'; 
        elif (self.getPeso() <= 83.9): 
            value = 'Médio'; 
        elif (self.getPeso() <= 93):
            value = 'Meio-Pesado'; 
        elif (self.getPeso() <= 120.2): 
            value = 'Pesado';
        else: 
            value = 'Inválido'; 

        return value; 

    def setVitoria(self, value): 
        self.__vitoria = value; 

    def setDerrotas(self, value): 
        self.__derrotas = value; 

    def setEmpates(self, value): 
        self.__empates = value; 

    def apresentar(self): 
        print('-' * 35);
        print('Apresentação do lutador'.center(35)); 
        print('-' * 35);
        print(f'Nome: {self.getNome()}'); 
        print(f'Nacionalidade: {self.getNacionalidade()}'); 
        print(f'Idade: {self.getIdade()}'); 
        print(f'Altura: {self.getAltura()}'); 
        print(f'Peso: {self.getPeso()}Kg'); 
        print(f'Categoria: {self.setCategoria(self.getPeso())}'); 
        print(f'Vitória: {self.getVitoria()}'); 
        print(f'Derrotas: {self.getDerrotas()}'); 
        print(f'Empates: {self.getEmpates()}');

    def ganharLuta(self): 
        self.setVitoria(self.getVitoria() + 1); 
        print(f'O lutador {self.getNome()} venceu a luta'); 

    def perderLuta(self): 
        self.setDerrotas(self.getDerrotas() + 1); 
        print(f'O lutador {self.getNome()} perdeu a luta'); 

    def empatarLuta(self): 
        self.setEmpates(self.getEmpates() + 1); 
        print(f'O lutador {self.getNome()} empatou a luta'); 

    # Talvez seja um resumo das lutas do lutador em questão
    def status(self): 
        print(self.getNome()); 
        print(f'É um peso {self.getCategoria()}'); 
        print(f'{self.getVitoria()} vitórias'); 
        print(f'{self.getDerrotas()} derrotas');
        print(f'{self.getEmpates()} empates'); 

lutador = [Lutador('Pretty Boy', 'França', 31, 1.75, 68.9, 11, 2, 1), Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 14, 2, 3), Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 12, 2, 1), Lutador('Dead Code', 'Austrália', 28, 1.93, 81.6, 13, 0, 2)]; 

lutador[0].apresentar(); 
lutador[2].status(); 
lutador[3].getCategoria(); 
lutador[1].ganharLuta(); 
lutador[0].empatarLuta(); 