import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;

head = Node();
arvore = ArvoreDeBusca(head);

solucao = arvore.busca_por_prioridade(500);
i = 0;
print(solucao);