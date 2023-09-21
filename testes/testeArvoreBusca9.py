import sys;
sys.path.append("..");

from tabuleiro import *;
from node import *;
from arvoreDeBusca import *;
tab = tabuleiro([[8,5,6],[2,3,0],[4,1,7]], 0, 1);
head = Node(tab);
head.visualize_simple();
arvore = ArvoreDeBusca(head);

solution = arvore.busca_em_largura(50);
print("SOLUÇÃO : ");
if type(solution) == str:
    print(solution);
else:
    for node in solution:
        node.visualize_simple();  