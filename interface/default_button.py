import sys;
sys.path.append("..");

from interface.estilos import *;
from interface.grid import *;

def create_default_button(master, r, c, target):
    #Isso é bem estranho, mas para fazer uma imagem funcionar
    #em um botão, é preciso criar um label como feito aqui embaixo
    #(sim, não faz sentido)
    visionImage = PhotoImage(file="img/restore_80.png");
    figura = Label(master, image=visionImage);
    figura.image = visionImage;

    default_button = Button(master,
                            background=BACKGROUND_DEFAULT_BUTTON,
                            activebackground=BACKGROUND_DEFAULT_BUTTON,
                            image=visionImage,
                            height=HEIGHT_DEFAULT_BUTTON,
                            width=WIDTH_DEFAULT_BUTTON,
                            font=FONT_DEFAULT_BUTTON,
                            command=lambda: restoreGrid(target),
                            border=0);
    default_button.grid(column=c,
                        row=r,
                        padx=PADX_DEFAULT_BUTTON,
                        pady=PADY_DEFAULT_BUTTON);
    return default_button;
