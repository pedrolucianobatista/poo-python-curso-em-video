# Importar de uma forma melhor 
# from classes import Pessoa.Pessoa (se der)

from classes import Aluno;
from classes import Funcionario;
from classes import Pessoa;
from classes import Professor; 


p1 = Pessoa.Pessoa(); 
p2 = Aluno.Aluno();  
p3 = Professor.Professor(); 
p4 = Funcionario.Funcionario(); 

p1.setNome('Pedro'); 
p2.setNome('Maria'); 
p3.setNome('Cláudio'); 
p4.setNome('Fabiana'); 

p2.setCurso('Informática'); 
p3.setSalario(2500.75); 
p4.setSetor('Estoque'); 

p1.setSexo('M'); 
p4.setSexo('F'); 
p2.setIdade(18); 

p2.setCurso('Informática'); 
p3.setSalario(2500.75); 
p4.setSetor('Estoque'); 

p1.detalhes(); 
p2.detalhes(); 
p3.detalhes(); 
p4.detalhes(); 
 