import sys;
sys.path.append("..");

from interface.estilos import *;
from interface.grid import *;

def create_show_number_button(master, r, c, target):
    #Isso é bem estranho, mas para fazer uma imagem funcionar
    #em um botão, é preciso criar um label como feito aqui embaixo
    #(sim, não faz sentido)
    visionImage = PhotoImage(file="img/show_80.png");
    figura = Label(master, image=visionImage);
    figura.image = visionImage;

    show_num_button = Button(master,
                             background=BACKGROUND_show_number,
                             activebackground=BACKGROUND_show_number,
                             image=visionImage,
                             width=WIDTH_show_number,
                             height=HEIGHT_show_number,
                             font=FONT_SHOW_BUTTON,
                             command=lambda: showNumbers(target),
                             border = 0);
    show_num_button.grid(column=c,
                         row=r,
                         padx=PADX_SHOW_BUTTON,
                         pady=PADY_SHOW_BUTTON);
    return show_num_button;
