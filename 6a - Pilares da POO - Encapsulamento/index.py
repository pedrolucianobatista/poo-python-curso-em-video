# Pesquisar sobre a questão da interface em python 

# interface Controlador
# Métodos Abstratos 
# publico abstrato Metodo ligar()
# publico abstrato Metodo desligar() 
# publico abstrato Metodo abrirMenu()
# publico abstrato Metodo fecharMenu()
# publico abstrato Metodo maisVolume()
# publico abstrato Metodo menosVolume()
# publico abstrato Metodo ligarMudo()
# publico abstrato Metodo desligarMudo()
# publico abstrato Metodo play()
# publico abstrato Metodo pause()
# FimInterface

from abc import ABC, abstractmethod; 

class interfaceControlador(ABC): 
    @abstractmethod
    def ligar(self): pass;

    @abstractmethod
    def desligar(self): pass; 

    @abstractmethod
    def abrirMenu(self): pass; 

    @abstractmethod 
    def fecharMenu(self): pass; 

    @abstractmethod 
    def maisVolume(self): pass; 

    @abstractmethod 
    def menosVolume(self): pass; 

    @abstractmethod 
    def ligarMudo(self): pass; 

    @abstractmethod 
    def desligarMudo(self): pass; 

    @abstractmethod 
    def play(self): pass; 

    @abstractmethod 
    def pause(self): pass; 

class ControleRemoto(interfaceControlador): 
    def __init__(self, volume = 50, ligado = False, tocando = False):
        self.volume = volume; 
        self.ligado = ligado; 
        self.tocando = tocando; 

    def getVolume(self): 
        return self.volume; 

    def getLigado(self): 
        return self.ligado; 

    def getTocando(self): 
        return self.tocando; 

    def setVolume(self, value): 
        self.volume = value; 

    def setLigado(self, value): 
        self.ligado = value; 

    def setTocando(self, value): 
        self.tocando = value; 

# Implementação dos métodos dessa classe 

    def ligar(self): 
        self.setLigado(True); 

    def desligar(self):
        self.setLigado(False); 

    # Mostrar especificações do controle
    def abrirMenu(self): 
        print(f'Volume: {self.getVolume() * '-'}');
        print(f'Ligado: {self.getLigado()}'); 
        print(f'Tocando: {self.getTocando()}'); 

    def fecharMenu(self):
        print('Fechando menu'); 
    # Aumentar apenas um tracinho no volume

    def maisVolume(self):
        if (self.getLigado()): 
            self.setVolume(self.getVolume() + 1); 

    def menosVolume(self):
        if (self.getLigado()): 
            self.setVolume(self.getVolume() - 1); 

    def ligarMudo(self):
        if (self.getLigado() and self.getVolume() > 0 ): 
            self.setVolume(0); 

    def desligarMudo(self):
        if (self.getLigado() and self.getVolume() == 0): 
            self.setVolume(50);

    def play(self):
        if (self.getLigado() and not self.getTocando()): 
            self.setTocando(True);

    def pause(self):
        if (self.getLigado() and self.getTocando()): 
            self.setTocando(False);