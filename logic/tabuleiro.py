import sys;
sys.path.append("..");

import random;
from logic.funcoesAuxiliares import *;
from global_data import *;

class tabuleiro:

    def __init__(self, 
                 tabuleiro : list = None, 
                 line0 = 0, 
                 column0 = 1):
        
        # Vou colocar uns valores fixos por enquanto, mas gera uns aleatórios depois
        if tabuleiro == None:
            self.body = [[1, 0, 2],
                        [5, 3, 7],
                        [4, 6, 8]];
            self.zero_line = 0;
            self.zero_column = 1;
        else:
            self.body = copy(tabuleiro);
            self.zero_column = column0;
            self.zero_line = line0;
    
    def show(self):
        for line in self.body:
            print(line);
    
    def show_all(self):
        self.show();
        print("Line0 = " + str(self.zero_line));
        print("Column0 = " + str(self.zero_column));
    
    def move(self, value):
        if value == "TOP":
            if self.can_move("TOP"):
                return self.move_top();
        if value == "LEFT":
            if self.can_move("LEFT"):
                return self.move_left();
        if value == "BOTTOM":
            if self.can_move("BOTTOM"):
                return self.move_bottom();
        if value == "RIGHT":
            if self.can_move("RIGHT"):
                return self.move_right();   

    def can_move(self, value):
        if value == "TOP":
            return self.zero_line != 0;
        if value == "LEFT":
            return self.zero_column != 0;
        if value == "BOTTOM":
            return self.zero_line != 2;
        if value == "RIGHT":
            return self.zero_column != 2;

    def move_top(self):
        value = self.body[self.zero_line - 1][self.zero_column];
        self.body[self.zero_line - 1][self.zero_column] = 0;
        self.body[self.zero_line][self.zero_column] = value;

        self.zero_line = self.zero_line - 1;
        self.zero_column = self.zero_column;

        return tabuleiro(self.body, self.zero_line, self.zero_column);

    def move_right(self):
        value = self.body[self.zero_line][self.zero_column + 1];
        self.body[self.zero_line][self.zero_column + 1] = 0;
        self.body[self.zero_line][self.zero_column] = value;

        self.zero_line = self.zero_line;
        self.zero_column = self.zero_column + 1;
        
        return tabuleiro(self.body, self.zero_line, self.zero_column);

    def move_bottom(self):
        value = self.body[self.zero_line + 1][self.zero_column];
        self.body[self.zero_line + 1][self.zero_column] = 0;
        self.body[self.zero_line][self.zero_column] = value;

        self.zero_line = self.zero_line + 1;
        self.zero_column = self.zero_column;
        
        return tabuleiro(self.body, self.zero_line, self.zero_column);
            
    def move_left(self):
        value = self.body[self.zero_line][self.zero_column - 1];
        self.body[self.zero_line][self.zero_column - 1] = 0;
        self.body[self.zero_line][self.zero_column] = value;

        self.zero_line = self.zero_line;
        self.zero_column = self.zero_column - 1;
        
        return tabuleiro(self.body, self.zero_line, self.zero_column);

    def see_move(self, value):
        if value == "TOP":
            if self.can_move("TOP"):
                return self.see_move_top();
        if value == "LEFT":
            if self.can_move("LEFT"):
                return self.see_move_left();
        if value == "BOTTOM":
            if self.can_move("BOTTOM"):
                return self.see_move_bottom();
        if value == "RIGHT":
            if self.can_move("RIGHT"):
                return self.see_move_right();    

    def see_move_top(self):
        new_matriz = copy(self.body);
        value = new_matriz[self.zero_line - 1][self.zero_column];
        new_matriz[self.zero_line - 1][self.zero_column] = 0;
        new_matriz[self.zero_line][self.zero_column] = value;

        return tabuleiro(new_matriz, self.zero_line - 1, self.zero_column);

    def see_move_right(self):
        new_matriz = copy(self.body);
        value = new_matriz[self.zero_line][self.zero_column + 1];
        new_matriz[self.zero_line][self.zero_column + 1] = 0;
        new_matriz[self.zero_line][self.zero_column] = value;

        return tabuleiro(new_matriz, self.zero_line, self.zero_column + 1);

    def see_move_bottom(self):
        new_matriz = copy(self.body);
        value = new_matriz[self.zero_line + 1][self.zero_column];
        new_matriz[self.zero_line + 1][self.zero_column] = 0;
        new_matriz[self.zero_line][self.zero_column] = value;

        return tabuleiro(new_matriz, self.zero_line + 1, self.zero_column);

    def see_move_left(self):
        new_matriz = copy(self.body);
        value = new_matriz[self.zero_line][self.zero_column - 1];
        new_matriz[self.zero_line][self.zero_column - 1] = 0;
        new_matriz[self.zero_line][self.zero_column] = value;

        return tabuleiro(new_matriz, self.zero_line, self.zero_column - 1);
   
    def scramble(self, steps):
        for i in range(0, steps):
            dice = random.randint(0,3);
            if dice == 0:
                self.move("TOP");
            elif dice == 1:
                self.move("RIGHT");
            elif dice == 2:
                self.move("BOTTOM");
            elif dice == 3:
                self.move("LEFT");

    def avaliate(self) -> int:
        p = 0;
        for i in range(0,3):
            for j in range(0,3):
                if self.body[i][j] == DEFAULT_GRID[i][j]:
                    p += 1;
        return p;
