# Formula_bem_formulada
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
from global_data import *;

from ctypes import windll;
windll.shcore.SetProcessDpiAwareness(1);

def create_window(root, master):
    global grid_jogo;

    container_grade = Frame(master,
                            width=420,
                            height=420);
    container_grade.grid(column=0, row=0);

    create_grid(container_grade, grid_jogo);
    
    root.bind(sequence="<Key>", func=lambda event, main=container_grade: key_pressed(event, main));

    container_answer = Frame(master,
                            width=420,
                            height=420,
                            background=BACKGROUND_CONTAINER_ANSWER);
    container_answer.grid(column=1, row=0);

    answer = create_answer_widget(container_answer, r=0, c=0, texto_resposta='');
    solve_button = create_solve_button(container_answer, answer, r=1, c=0);
    shownum_button = create_show_number_button(container_answer, r=1, c=2, target=container_grade);
    scramble_button = create_scramble_button(container_answer, r=1,c=3, target=container_grade);

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