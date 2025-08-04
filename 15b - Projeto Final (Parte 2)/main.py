from Gafanhoto import Gafanhoto
from Video import Video 
from Visualizacao import Visualizacao 

videos = [Video('Aula 1 de POO'), Video('Aula 12 de PHP'), Video('Aula 10 de HTML5')]; 
gafanhoto = [Gafanhoto('Jubileu', 22, 'm', 0, 'juba'), Gafanhoto('Creuza', 12, 'f', 0, 'creuzita')]; 

vis = [Visualizacao(gafanhoto[0], videos[2]), Visualizacao(gafanhoto[0], videos[1])]; 

vis[0].avaliar(); 

videos[0].detalhes(); 

vis[0].avaliar(87.0); 

gafanhoto[0].detalhes(); 
