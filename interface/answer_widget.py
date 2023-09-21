from interface.estilos import *;
from tkinter import *;
from logic.funcoesAuxiliares import *;
from global_data import *;

def create_answer_widget(master, r, c, texto_resposta) -> Label:
    #Isso é bem estranho, mas para fazer uma imagem funcionar
    #em um botão, é preciso criar um label como feito aqui embaixo
    #(sim, não faz sentido)
    pixelVirtual = PhotoImage(width=1, height=1);
    figura = Label(master, image=pixelVirtual);
    figura.image = pixelVirtual;

    answer = Label(master, 
                background=BACKGROUND_ANSWER, 
                image=pixelVirtual,
                width=WIDTH_ANSWER, 
                height=HEIGHT_ANSWER, 
                text=line_break(texto_resposta), 
                font=FONT_ANSWER,
                fg=FONT_ANSWER_COLOR,
                compound="c");
    answer.grid(column=c, 
                row=r, 
                padx=(PADX_LEFT_ANSWER, PADX_RIGHT_ANSWER), 
                pady=PADY_ANSWER, 
                columnspan=4);
    return answer;
