from index import Lutador

lutadores = [
    Lutador('Pretty Boy', 'França', 31, 1.75, 68.9, 11, 2, 1), 
    Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 14, 2, 3), 
    Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 12, 2, 1), 
    Lutador('Dead Code', 'Austrália', 28, 1.93, 81.6, 13, 0, 2), 
    Lutador('UFOCobol', 'Brasil', 37, 1.7, 119.3, 5, 4, 3), 
    Lutador('Nerdaart', 'EUA', 30, 1.81, 105.7, 12, 2, 4)
    ]; 

lutadores[3].status(); 
lutadores[3].ganharLuta();
lutadores[3].status(); 