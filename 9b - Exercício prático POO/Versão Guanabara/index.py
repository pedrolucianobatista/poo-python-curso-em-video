from Livro import Livro
from Pessoa import Pessoa

pessoas = []; 
pessoas = [Pessoa('Pedro', 22, 'M'), Pessoa('Maria', 25, 'F')]; 

livros = []; 
livros = [Livro('Aprendendo Java', 'José da Silva', 300, pessoas[0].getNome()), Livro('POO para iniciantes', 'Pedro Paulo', 500, pessoas[1].getNome()), Livro('Java Avançado', 'Maria Candido', 800, pessoas[0].getNome())]; 

livros[0].abrir(); 
livros[0].folhear(100); 
livros[0].avancarPag(); 

livros[0].detalhes(); 

livros[1].detalhes(); 