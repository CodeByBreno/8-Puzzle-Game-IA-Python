import sys;
sys.path.append("..");

from interface.estilos import *;
from interface.grid import *;
from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;
from global_data import *;

def create_solve_button(master, answer_widget, r, c) -> Button:
    global show_number;

    botao = PhotoImage(file="img/button.png");
    figura = Label(master, image=botao);
    figura.image = botao;

    solve_button = Button(master, 
                          background=BACKGROUND_SOLVE_BUTTON,
                          activebackground=BACKGROUND_SOLVE_BUTTON,
                          activeforeground=ACTIVE_FONT_BUTTON_COLOR,
                          image=botao,
                          width=WIDTH_SOLVE_BUTTON, 
                          height=HEIGHT_SOLVE_BUTTON, 
                          text=TEXTO_SOLVE_BUTTON, 
                          font=FONT_BUTTON, 
                          command=lambda: solver(answer_widget),
                          fg=FONT_BUTTON_COLOR,
                          compound="c",
                          border=0);
    solve_button.grid(column=c, 
                      row=r,
                      padx=PADX_SOLVE_BUTTON, 
                      pady=PADY_SOLVE_BUTTON,
                      columnspan=3);
    return solve_button;