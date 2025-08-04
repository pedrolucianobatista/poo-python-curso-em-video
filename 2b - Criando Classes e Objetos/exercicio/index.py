# Utilização do exemplo da aula passada para verificar sobre a questão de métodos em uma classe abstrata 
# Classe para uma aula que se encadraria na questão abstrata 
# Definir métodos(funções) para essa classe abstrata 
# Iniciar aula, e finalizar utilizando duas chamadas

class Aula(): 
    def __init__(self, materia, tema, duracao, status):
        self.materia = materia; 
        self.tema = tema; 
        self.duracao = duracao; 
        self.status = status;

    def resume(self): 
        print(f'Matéria: {self.materia}\nTema: {self.tema}\nDuração: {self.duracao} minutos\nEstá sendo realizada? {self.status}');

    def finalizar(self): 
        if (self.status): 
            print('Estamos finalizando a aula guys'); 
        else: 
            print('Não é possível finalizar a aula, pois ela ainda não foi inicializada');

    def inicializar(self): 
        if (not self.status): 
            print('Estamos inicializando a aula guys');
        else: 
            print('Erro! A aula já foi iniciada');

aula1 = Aula('Matemática', 'Trigonométrica', 60, True); 

aula1.resume();
aula1.inicializar();