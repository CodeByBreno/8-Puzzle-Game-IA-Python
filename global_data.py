#não use para atribuições, evite problemas com ponteiros
from tkinter import *;

DEFAULT_GRID = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]; 

buttons_grid = [0,0,0,0,0,0,0,0,0];
grid_jogo = [[0, 1, 2],[3, 4, 5],[6, 7, 8]];
texto_resposta = '';

# Maior profundidade que pode ser alcançada pelo algoritmo
# Para as buscas cegas, use valores por volta de 10, senão vai demorar demais
MAX_LEVELS = 100;

# Modifique o tipo de busca realizada no programa com a constante abaixo
# Opções: DEPTH, WIDTH, PRIORITY, PRIORITY_IGNORE_ZERO
# As duas primeiras são buscas cegas por profundidade e por largura, resp.
# A terceira é uma busca que usa como heurística a quantidade de blocos em posição correta
SEARCH_TYPE = "PRIORITY_IGNORE_ZERO";