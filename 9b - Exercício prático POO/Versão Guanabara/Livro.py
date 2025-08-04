from Interface import Publicacao

class Livro(Publicacao): 
    def __init__(self, titulo, autor, totPaginas, leitor, pagAtual = 0, aberto = 0):
        self.__titulo = titulo; 
        self.__autor = autor; 
        self.__totPaginas = totPaginas; 
        self.__pagAtual = pagAtual; 
        self.__aberto = aberto; 
        self.__leitor = leitor; 
    
    def detalhes(self): 
        print(f"""Livro: {self.getTitulo()}
Autor: {self.getAutor()}
Total de Páginas: {self.getTotPaginas()}
Página Atual: {self.getPagAtual()}
Leitor: {self.getLeitor()}""");

    def getTitulo(self): 
        return self.__titulo; 

    def getAutor(self): 
        return self.__autor; 

    def getTotPaginas(self): 
        return self.__totPaginas; 

    def getPagAtual(self): 
        return self.__pagAtual; 

    def getAberto(self): 
        return self.__aberto; 

    def getLeitor(self): 
        return self.__leitor; 

    def setTitulo(self, value): 
        self.__titulo = value; 
        return self.__titulo; 

    def setAutor(self, value): 
        self.__autor = value; 
        return self.__autor; 

    def setTotPaginas(self, value): 
        self.__totPaginas = value; 
        return self.__totPaginas; 

    def setPagAtual(self, value): 
        self.__pagAtual = value; 
        return self.__pagAtual; 

    def setAberto(self, value): 
        self.__aberto = value; 
        return self.__aberto; 

    def setLeitor(self, value): 
        self.__leitor = value; 
        return self.__leitor; 

    def abrir(self): 
        self.__aberto = True; 

    def fechar(self): 
        self.__aberto = False; 

    def folhear(self, p): 
        if (p > self.__totPaginas): 
            self.__pagAtual = 0; 
        else: 
            self.__pagAtual = p; 

    def avancarPag(self): 
        self.setPagAtual(self.__pagAtual + 1); 

    def voltarPag(self): 
        self.setPagAtual(self.__pagAtual - 1); 

# Consertar a interface do exercício anterior 