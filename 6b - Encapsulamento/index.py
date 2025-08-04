from interface import controladorInterface

class ControleRemoto(controladorInterface): 
    def __init__(self, volume = 50, ligado = False, tocando = False):
        self.__volume = volume; 
        self.__ligado = ligado; 
        self.__tocando = tocando; 

    def __getVolume(self): 
        return self.__volume; 

    def __getLigado(self): 
        return self.__ligado; 

    def __getTocando(self): 
        return self.__tocando; 

    def __setVolume(self, value): 
        self.__volume = value; 

    def __setLigado(self, value): 
        self.__ligado = value;

    def __setTocando(self, value): 
        self.__tocando = value;   

    def ligar(self): 
        if (not self.__getLigado()): 
            self.__setLigado(True); 

    def desligar(self): 
        if (self.__getLigado()): 
            self.__setLigado(False); 

    def abrirMenu(self):
        print('-' * 30); 
        print('MENU'.center(30));
        print('-' * 30); 
        print(f'Volume: ({self.__getVolume()}) {(self.__getVolume() // 10) * '|'}'); 
        print(f'Está ligado? {self.__getLigado()}'); 
        print(f'Está tocando? {self.__getTocando()}');

    def fecharMenu(self):
        print('Fechando menu....'); 

    def maisVolume(self):
        if (self.__getLigado()): 
            self.__setVolume(self.__getVolume() + 5); 
        else: 
            print('Impossível aumentar volume');

    def menosVolume(self):
        if (self.__getLigado()): 
            self.__setVolume(self.__getVolume() - 5); 
        else: 
            print('Impossível diminuir volume'); 

    def ligarMudo(self):
        if (self.__getVolume() > 0 and self.__getLigado()): 
            self.__setVolume(0); 

    def desligarMudo(self):
        if (self.__getVolume() == 0 and self.__getLigado()): 
            self.__setVolume(50); 

    def play(self):
        if (self.__getLigado() and not self.__getTocando()): 
            self.__setTocando(True); 
        else: 
            print('Não consegui reproduzir');

    def pause(self): 
        if (self.__getLigado() and self.__getTocando()): 
            self.__setTocando(False);
        else: 
            print('Não consegui pausar'); 
