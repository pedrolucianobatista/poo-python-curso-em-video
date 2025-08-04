from animais.Animal import Animal; 
from animais.Mamifero import Mamifero; 
from animais.Reptil import Reptil; 
from animais.Ave import Ave; 
from animais.Peixe import Peixe; 

from animais.especies.Cachorro import Cachorro; 
from animais.especies.Canguru import Canguru; 
from animais.especies.Cobra import Cobra;  
from animais.especies.Tartaruga import Tartaruga; 
from animais.especies.Goldfish import Goldfish; 
from animais.especies.Arara import Arara; 

m = Mamifero(); 
r = Reptil(); 
p = Peixe(); 
a = Ave(); 

canguru = Canguru();
cachorro = Cachorro(); 
cobra = Cobra();
tartaruga = Tartaruga(); 
goldfish = Goldfish(); 
arara = Arara(); 

canguru.locomover(); 
cachorro.locomover();

canguru.emitirSom(); 
cachorro.emitirSom(); 
