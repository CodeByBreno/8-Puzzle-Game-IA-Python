import sys;
sys.path.append("..");

from main import *;

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
arvore.atualize_border(novos_nos, "WIDTH");
print("@@@@@@@@@@@@@@@ BORDA DA ÁRVORE ATUALIZADA: ");
arvore.show_border_simple();

no = arvore.pop_choose_node();
novos_nos = arvore.expand_node(no);
arvore.atualize_border(novos_nos, "WIDTH");

print("@@@@@@@@@@@@@@@@@@@ BORDA NA BUSCA DE NIVEL 2: ");
arvore.show_border_simple();

no = arvore.pop_choose_node();
novos_nos = arvore.expand_node(no);
arvore.atualize_border(novos_nos, "WIDTH");

print("@@@@@@@@@@@@@@@@@@@ BORDA NA BUSCA DE NIVEL 3: ");
arvore.show_border_simple();
