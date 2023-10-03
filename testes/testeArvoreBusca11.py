import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;

head = Node();
head.visualize();

arvore = ArvoreDeBusca(head);
novos_nos = arvore.expand_node(head);

for each in novos_nos:
    print("NOVO NO =====================");
    each.visualize_simple();

print("@@@@@@@@@ BORDA DA ÁRVORE: ");
arvore.show_border_simple();
arvore.pop_choose_node();
arvore.atualize_border(novos_nos, "PRIORITY");
print("@@@@@@@@@@@@@@@ BORDA DA ÁRVORE ATUALIZADA: ");
arvore.show_border_simple();