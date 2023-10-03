from interface.estilos import *;
from logic.funcoesAuxiliares import *;
from global_data import *;
from tkinter import *;
from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;
from interface.answer_widget import *;

def get_position(i):
    global grid_jogo;

    for line in range(0,3):
        for column in range(0,3):
            if grid_jogo[line][column] == i:
                return (line, column);

def check_surrounding(line, column):
    global grid_jogo;

    #TOP
    if (line != 0):
        if (grid_jogo[line-1][column] == 0):
            return (line-1, column);
    #RIGHT
    if (column != 2):
        if (grid_jogo[line][column+1] == 0):
            return (line, column+1);
    #BOTTOM
    if (line != 2):
        if (grid_jogo[line+1][column] == 0):
            return (line+1, column);
    #LEFT
    if (column != 0):
        if (grid_jogo[line][column-1] == 0):
            return (line, column-1);
    return None;

def create_grid(master, create=[0,1,2,3,4,5,6,7,8]):
    global buttons_grid, grid_jogo, show_number;

    #print("------------");
    for i in range(0,3):
        for j in range(0,3):
            value = grid_jogo[i][j];
            if value in create:
                aux = i*3 + j;
                #print("created button " + str(aux));
                buttons_grid[aux] = create_grid_button(master, 
                                           grid_jogo[i][j]);
                buttons_grid[aux].grid(row=i, 
                                column=j, 
                                padx=PADX_GRID, 
                                pady=PADY_GRID);
    print("No create_grid : " + str(show_number));   
    if show_number:
        showNumbers();

def create_grid_button(master, content) -> Button:

    background_image = PhotoImage(file='img/image' + str(content) + '.png');
    figura = Label(master, 
                   image=background_image);
    figura.image = background_image;

    botao = Button(master, 
                  background=BACKGROUND_GRID, 
                  width=WIDTH_GRID, 
                  height=HEIGHT_GRID, 
                  font=MAIN_FONT, 
                  text=" ",
                  command=lambda m=content: move_tile(master, m),
                  fg=GRID_BUTTON_COLOR,
                  border=0,
                  image=background_image,
                  compound="c");
    
    return botao;

def move_tile(main, m):
    global grid_jogo;

    content_position = get_position(m);
    empty_location = check_surrounding(content_position[0], content_position[1]);

    if empty_location != None:
        grid_jogo[empty_location[0]][empty_location[1]] = m;
        grid_jogo[content_position[0]][content_position[1]] = 0;
    
    if grid_jogo == DEFAULT_GRID:
        main.config(bg="#ff0000");
    else:
        main.config(bg=MAIN_BACKGROUND);
    
    create_grid(main, create=[0,m]);

def mix_grid(target):
    global grid_jogo;

    p = get_position(0);
    table = tabuleiro(grid_jogo, p[0], p[1]);
    table.scramble(MIX_STEPS);
    table.show();

    grid_jogo = table.body; #cuidado com isso aq
    create_grid(target);

def restoreGrid(target):
    global grid_jogo;

    grid_jogo = [[0, 1, 2],[3, 4, 5],[6, 7, 8]];
    create_grid(target);

def changeShowNumber():
    global show_number;

    if show_number:
        show_number = False;
    else:
        show_number = True;
    
    print("No changeShowNumber : " + str(show_number));   
    showNumbers();

def showNumbers():
    global show_number, grid_jogo;
                                               
    if show_number:
        for i in range(0,9):
            valor = grid_jogo[i//3][i%3];
            buttons_grid[i].config(text=str(valor));
    else:
        for each in buttons_grid:
            each.config(text=' ');
        
def solver(answer_widget, search_type):
    global grid_jogo;
    global texto_resposta;
    
    position = get_position(0);
    print("Clicou no Solver");
    print(grid_jogo);
    tab = tabuleiro(grid_jogo, position[0], position[1]);
    head = Node(tab);
    arvore = ArvoreDeBusca(head);
    solution = arvore.buscar(arvore, search_type);
    direcoes = [];

    if type(solution) != str:
        for each in solution:
            if each.dir != None:
                direcoes.append(each.dir);
            else:
                direcoes.append("");
        texto_resposta = " ".join(direcoes);
    else:
        texto_resposta = solution;
    
    answer_widget.config(text=line_break(texto_resposta));

def key_pressed(event, widget):
    global grid_jogo;

    p = get_position(0);
    table = tabuleiro(grid_jogo, p[0], p[1]);
    table.show();

    if event.char == 'w' or event.char == 'W':
        table.move("TOP");
    elif event.char == 'd' or event.char == 'D':
        table.move("RIGHT");
    elif event.char == 's' or event.char == 'S':
        table.move("BOTTOM");
    elif event.char == 'a' or event.char == 'A':
        table.move("LEFT");
    changed_value = table.body[p[0]][p[1]];

    grid_jogo = table.body;
    create_grid(widget, [0, changed_value]);
