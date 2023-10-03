import sys;
sys.path.append("..");

from main import *;
tab = tabuleiro([[1,0,2],[3,4,5],[6,7,8]], 0, 1);
head = Node(tab);
arvore = ArvoreDeBusca(head);
solution = arvore.buscar(10, "DEPTH");

print("SOLUÇÃO : ");
for node in solution:
    node.visualize_simple();