# 8_Puzzle_Game
# Desafio 1 para Disciplina de Inteligência Artificial - 2023.1
# Feito por: Breno Gabriel de Souza Coelho | Turma 2019.2
# Apresentado em 18/09/2023

from tkinter import *;
from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;
from interface.estilos import *;
from interface.grid import *;
from interface.show_button import *;
from interface.solve_button import *;
from interface.answer_widget import *;
from interface.scramble_button import *;
from interface.default_button import *;
from global_data import *;

from ctypes import windll;
windll.shcore.SetProcessDpiAwareness(1);

def create_window(root, master):
    global grid_jogo, shownum_button;

    container_grade = Frame(master,
                            width=420,
                            height=420);
    container_grade.grid(column=0, row=0);

    create_grid(container_grade);
    
    root.bind(sequence="<Key>", func=lambda event, main=container_grade: key_pressed(event, main));

    container_answer = Frame(master,
                            width=420,
                            height=420,
                            background=BACKGROUND_CONTAINER_ANSWER);
    container_answer.grid(column=1, row=0);

    answer = create_answer_widget(container_answer, r=0, c=0);
    
    solve_frame = Frame(container_answer,
                            width=420,
                            height=420,
                            background=BACKGROUND_CONTAINER_ANSWER);
    solve_frame.grid(row=1, column=0);
    solve_button = create_solve_button(solve_frame, answer, r=1, c=0, search_type=SEARCH_TYPE);

    function_buttons = Frame(container_answer,
                            width=420,
                            height=420,
                            background=BACKGROUND_CONTAINER_ANSWER);
    function_buttons.grid(row=1, column=1);

    shownum_button = create_show_number_button(function_buttons, r=0, c=0, target=container_grade);
    scramble_button = create_scramble_button(function_buttons, r=0,c=1, target=container_grade);
    default_button = create_default_button(function_buttons, r=0, c=2, target=container_grade);


buttons_grid = [0,0,0,0,0,0,0,0,0];
root = Tk();
root.geometry(WINDOW_RESOLUTION);
root.title("8-Puzzle Game");
root.configure(bg=MAIN_BACKGROUND);

main = Frame(root, 
             pady=PADY_GLOBAL,
             background=MAIN_BACKGROUND);
main.pack();

create_window(root, main);
root.mainloop();