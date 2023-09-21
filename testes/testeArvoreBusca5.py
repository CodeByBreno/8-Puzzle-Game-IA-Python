import sys;
sys.path.append("..");

from main import *;

head = Node();
arvore = ArvoreDeBusca(head);

print("@@@@@@@@@ BORDA INICIAL DA ÁRVORE: ");
arvore.show_border_simple();
N = 100;

for i in range(0, N):
    no = arvore.pop_choose_node();
    novos_nos = arvore.expand_node(no);
    arvore.atualize_border(novos_nos, "DEPTH");

print("@@@@@@@@@@@@@@@@@@@@@ Borda após " + str(N) + " iterações")
arvore.show_border_simple();
tam_depth = len(arvore.border);


for i in range(0, N):
    no = arvore.pop_choose_node();
    novos_nos = arvore.expand_node(no);
    arvore.atualize_border(novos_nos, "WIDTH");

print("@@@@@@@@@@@@@@@@@@@@@ Borda após " + str(N) + " iterações")
arvore.show_border_simple();
tam_width = len(arvore.border);

print("TAMANHO DA BORDA (depth): " + str(tam_depth))
print("TAMANHO DA BORDA (width): " + str(tam_width))