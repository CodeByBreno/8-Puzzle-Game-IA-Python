import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;

tab = tabuleiro([[3, 1, 5],[2, 4, 0],[6,7,8]], 1, 2);
head = Node(tab);
#head.visualize();

arvore = ArvoreDeBusca(head);
novos_nos = arvore.expand_node(head);
print("teste");

for each in novos_nos:
    print("NOVO NO =====================");
    each.visualize_simple();
