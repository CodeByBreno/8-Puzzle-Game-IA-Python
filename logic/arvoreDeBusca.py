from logic.tabuleiro import *;
from logic.node import *;

class ArvoreDeBusca():
    
    OBJETIVO = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]];
    border : list['Node'];

    def __init__(self, initial_state : Node):
        self.border = [];
        self.border.append(initial_state);
        self.initial_state = initial_state;

    def busca_em_profundidade(self, max_depth) -> list['Node'] | str:
        # Algoritmo do Slide
        while(True):
            if self.border == []:
                return "ERRO: Borda Vazia";
        
            no_escolhido = self.pop_choose_node();
        
            if self.teste_objetivo(no_escolhido):
                return no_escolhido.solution();
            
            if (no_escolhido.depth != max_depth):
                novos_nos = self.expand_node(no_escolhido);
                self.atualize_border(novos_nos, "DEPTH");  

    def busca_em_largura(self, max_depth) -> list['Node'] | str:
        # Algoritmo do Slide
        while(True):
            if self.border == []:
                return "ERRO: Borda Vazia";
        
            no_escolhido = self.pop_choose_node();
            if (no_escolhido.depth == max_depth):
                return "ERRO: Profundidade Máxima Atingida sem Solução";
        
            if self.teste_objetivo(no_escolhido):
                return no_escolhido.solution();
        
            novos_nos = self.expand_node(no_escolhido);
            self.atualize_border(novos_nos, "WIDTH");        

    def teste_objetivo(self, node : Node) -> bool:
        # Verifico se o conteúdo do nó é igual ao objetivo
        return node.table.body == self.OBJETIVO;
    
    def pop_choose_node(self) -> 'Node':
        # Retorno o primeiro elemento da borda
        return self.border.pop(0);
    
    def expand_node(self, node : Node) -> list['Node']:
        resultado = [];
        actions = node.possible_actions();

        for act in actions:
            no_filho = Node(state = act[0],
                            father = node,  
                            dir = act[1], 
                            depth = node.depth + 1);
            resultado.append(no_filho);
    
        return resultado;
        
    def atualize_border(self, node_list, type) -> None:
        if type == "DEPTH":
            self.border = node_list + self.border;
        if type == "WIDTH":
            self.border = self.border + node_list;

    def show_border(self):
        for node in self.border:
            node.visualize();

    def show_border_simple(self):
        for node in self.border:
            node.visualize_simple();
            print("Profundidade : " + str(node.depth));