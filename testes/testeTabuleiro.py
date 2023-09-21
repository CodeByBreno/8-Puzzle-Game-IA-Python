import sys;
sys.path.append("..");

from tabuleiro import *;

tab_teste = tabuleiro();

tab_teste.show();
print();

tab_teste.move("BOTTOM");
tab_teste.show();
print();

tab_teste.move("RIGHT");
tab_teste.show();
print();

print("Pode mover para cima? " + str(tab_teste.can_move("TOP")));
resultado = tab_teste.move("TOP");
tab_teste.show();
#resultado.show();
print();

resultado = tab_teste.move("LEFT");
tab_teste.show();
#resultado.show();
print();

print("Pode mover para cima? " + str(tab_teste.can_move("TOP")));
tab_teste.move("TOP")
tab_teste.show();
print();