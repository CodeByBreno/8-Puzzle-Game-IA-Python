import sys;
sys.path.append("..");

from interface.estilos import *;
from interface.grid import *;

def create_scramble_button(master, r, c, target):
    #Isso é bem estranho, mas para fazer uma imagem funcionar
    #em um botão, é preciso criar um label como feito aqui embaixo
    #(sim, não faz sentido)
    scrambleButton = PhotoImage(file="img/scramble_80.png");
    figura = Label(master, image=scrambleButton);
    figura.image = scrambleButton;

    scramble_button = Button(master,
                             background=BACKGROUND_SCRAMBLE,
                             activebackground=BACKGROUND_SCRAMBLE,
                             image=scrambleButton,
                             width=WIDTH_SCRAMBLE,
                             height=HEIGHT_SCRAMBLE,
                             font=FONT_SCRAMBLE,
                             command=lambda: mix_grid(target),
                             border=0);
    scramble_button.grid(column=c,
                         row=r,
                         padx=PADX_SCRAMBLE,
                         pady=PADY_SCRAMBLE);
    return scramble_button;
    