from classes.Interface import Publicacao
from time import sleep

class Livro(Publicacao): 
    def __init__(self, titulo = '', autor = '', totPaginas = 0, pagAtual = 1, aberto = False):
        self.__titulo = titulo; 
        self.__autor = autor; 
        self.__totPaginas = totPaginas; 
        self.__pagAtual = pagAtual; 
        self.__aberto = aberto; 
        self.__leitor = None;

    def getTitulo(self): 
        return self.__titulo; 

    def setTitulo(self, value): 
        self.__titulo = value; 
        return self.__titulo; 

    def getAutor(self): 
        return self.__autor; 

    def setAutor(self, value): 
        self.__autor = value; 
        return self.__autor; 

    def getTotPaginas(self): 
        return self.__totPaginas; 

    def setTotPaginas(self, value): 
        self.__totPaginas = value; 
        return self.__totPaginas; 

    def getPagAtual(self): 
        return self.__pagAtual; 

    def setPagAtual(self, value): 
        self.__pagAtual = value; 
        return self.__pagAtual; 

    def getAberto(self): 
        return self.__aberto; 

    def setAberto(self, value): 
        self.__aberto = value; 
        return self.__aberto; 
    
    def detalhes(self, value): 
        self.__leitor = value.getNome(); 

        print('-' * 30);
        print(f'Título: {self.__titulo}'.center(30)); 
        print('-' * 30); 
        print(f'Autor: {self.__autor}'); 
        print(f'Total de páginas: {self.__totPaginas}'); 
        print(f'Página Atual: {self.__pagAtual}'); 
        print(f'Está aberto: {self.__aberto}'); 
        print(f'Leitor: {self.__leitor}'); 
        print('-' * 30); 
        
    def abrir(self): 
        if (not self.getAberto()):
            self.setAberto(True); 
        else: 
            print('Livro já se encontra aberto'); 

    def fechar(self): 
        if (self.getAberto()):
            self.setAberto(False); 
        else: 
            print('Livro já está fechado'); 

    def folhear(self): 
        if (self.getAberto()): 
            print('Folheando...');
            sleep(1);
            print(f'O livro possui {self.getTotPaginas()} páginas');
        else: 
            print('Não é possível folhear o livro com ele fechado'); 

    def avancarPag(self): 
        if (self.getAberto() and self.getPagAtual() < self.getTotPaginas()):
            self.setPagAtual(self.getPagAtual() + 1); 
        else: 
            print('Não foi possível avançar a página');

    def voltarPag(self): 
        if (self.getAberto() and self.getPagAtual() > 1):
            self.setPagAtual(self.getPagAtual() - 1); 
        else: 
            print('Não foi possível voltar a página'); 
