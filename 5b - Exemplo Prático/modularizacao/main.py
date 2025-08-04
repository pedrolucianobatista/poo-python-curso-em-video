# Método para sacar os dinheiros. Obs: Somente utilização com os getters e setters
# Não acessar diretamente os atributos 
# 12:23

# cc = 50   cp = 150

# Método para pagar a mensalidade 

from index import ContaBanco;

p1 = ContaBanco(); 
p2 = ContaBanco();

p1.setNumConta(1111); 
p1.setDono('Jubileu'); 
p1.abrirConta('CC');

p2.setNumConta(2222); 
p2.setDono('Creuza');
p2.abrirConta('CP');

p1.depositarConta(100); 
p2.depositarConta(500);
p2.sacarConta(100);

p1.sacarConta(150);
p1.fecharConta();

p1.allStatus();
p2.allStatus();