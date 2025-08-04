from Interface import AcoesVideo

class Video(AcoesVideo): 
    def __init__(self, titulo='', avaliacao=1, views=0, curtidas=0, reproduzindo=False):
        self.__titulo = titulo; 
        self.__avaliacao = avaliacao; 
        self.__views = views; 
        self.__curtidas = curtidas; 
        self.__reproduzindo = reproduzindo; 

    def getTitulo(self): 
        return self.__titulo; 

    def getAvaliacao(self): 
        return self.__avaliacao; 

    def getViews(self): 
        return self.__views; 

    def getCurtidas(self): 
        return self.__curtidas; 

    def getReproduzindo(self): 
        return self.__reproduzindo; 

    def setTitulo(self, value): 
        self.__titulo = value; 
        return self.__titulo; 

    def setAvaliacao(self, value): 
        self.__avaliacao = value; 
        return self.__avaliacao; 

    def setViews(self, value): 
        self.__views = value; 
        return self.__views; 

    def setCurtidas(self, value): 
        self.__curtidas = value; 
        return self.__curtidas; 

    def setReproduzindo(self, value): 
        self.__reproduzindo = value; 
        return self.__reproduzindo; 

    def play(self):
        if (self.getReproduzindo()): 
            print('Não foi possível dar play, pois o vídeo ja está sendo reproduzido'); 
        else: 
            self.setReproduzindo(True);
            print(f'Início da reprodução'); 

    def pause(self):
        if (not self.getReproduzindo()): 
            print('Não foi possível pausar, pois o vídeo já está pausado'); 
        else: 
            self.setReproduzindo(False);
            print('Vídeo pausado com sucesso'); 

    def like(self):
        self.setCurtidas(self.getCurtidas() + 1); 

    def detalhes(self): 
        print(f'Título: {self.getTitulo()}');
        print(f'Avaliação: {self.getAvaliacao()}'); 
        print(f'Views: {self.getViews()}'); 
        print(f'Curtidas: {self.getCurtidas()}'); 
        print(f'Reproduzindo: {self.getReproduzindo()}'); 
