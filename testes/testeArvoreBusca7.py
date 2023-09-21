import sys;
sys.path.append("..");

from main import *;
tab = tabuleiro([[3,1,2],[4,7,5],[6,0,8]], 2, 1);
head = Node(tab);
head.visualize_simple();
arvore = ArvoreDeBusca(head);

solution = arvore.busca_em_largura(10);
print("SOLUÇÃO : ");
if type(solution) == str:
    print(solution);
else:
    for node in solution:
        node.visualize_simple();