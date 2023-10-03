import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;
tab = tabuleiro([[8,5,6],[2,3,0],[4,1,7]], 0, 1);
head = Node(tab);
head.visualize_simple();
arvore = ArvoreDeBusca(head);

solution = arvore.buscar(50, "DEPTH");
print("SOLUÇÃO : ");
if type(solution) == str:
    print(solution);
else:
    for node in solution:
        node.visualize_simple();  