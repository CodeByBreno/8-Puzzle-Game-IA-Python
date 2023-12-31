import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from global_data import *;

class Node:
    def __init__(self, 
                 state : tabuleiro = None, 
                 father : 'Node' = None,
                 dir : str = None, 
                 depth : int = 0,
                 priority: int = 0):
        
        if state != None:
            self.table = tabuleiro(state.body, state.zero_line, state.zero_column);
        else:
            self.table = tabuleiro();
        
        self.father = father;
        self.dir = dir;
        self.custo = 1;
        self.depth = depth;
        self.priority = self.avaliate();
    
    def visualize(self):
        self.table.show_all();

        print("---Nó pai: ");
        if self.father != None: 
            self.father.table.show_all(); 
        else: print("Sem pai"); 
        print("Movimento feito: " + str(self.dir));
        print("Profundidade do Nó: " + str(self.depth));  
        print("Nota do Nó: " + str(self.priority));
    
    def visualize_simple(self):
        self.table.show();
        print("Movimento = " + str(self.dir) + " | Nota = " + str(self.priority));

    def possible_actions(self) -> list[('tabuleiro', str)]:
        possible_actions = [];
        directions = ("TOP", "RIGHT", "BOTTOM", "LEFT");

        for dir in directions:
            if self.table.can_move(dir):
                estado = self.table.see_move(dir);
                possible_actions.append((estado, dir));

        return possible_actions;

    def solution(self) -> list['Node']:
        solucao = [];
        no = self;
        while (no != None):
            solucao = [no] + solucao;
            no = no.father;

        return solucao;

    def avaliate(self) -> int:
        p = self.table.avaliate();
        return p;
