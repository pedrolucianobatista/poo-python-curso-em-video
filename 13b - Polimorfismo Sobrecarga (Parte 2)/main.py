from classes.animais.Lobo import Lobo; 
from classes.animais.Cachorro import Cachorro; 
from classes.Mamifero import Mamifero

cachorro = Cachorro(); 
lobo = Lobo(); 
mamifero = Mamifero(); 

cachorro.reagir('Olá'); 
cachorro.reagir('Vai apanhar'); 
cachorro.reagir(11, 45); 
cachorro.reagir(21, 00); 
cachorro.reagir(True); 
cachorro.reagir(False); 
cachorro.reagir(2, 12.5); 
cachorro.reagir(17, 4.5); 
