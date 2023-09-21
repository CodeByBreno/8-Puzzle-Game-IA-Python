import sys;
sys.path.append("..");

from main import *;

head = Node();
arvore = ArvoreDeBusca(head);

solucao = arvore.busca_em_arvore();
i = 0;
print(solucao);
# for each in solucao:
#     i += 1;
#     print("---------------------PASSO " + str(i));
#     each.visualize();