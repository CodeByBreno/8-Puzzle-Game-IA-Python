from main import *;

state = Node();

while(True):
    state.table.show(); 
    print("\nUse W-A-S-D para selecionar a próxima jogada");
    escolha = input();
    if (escolha == 'W' or escolha == 'w'):
        state.table.move("TOP");
    elif (escolha == 'A' or escolha == 'a'):
        state.table.move("LEFT");
    elif (escolha == 'S' or escolha == 's'):
        state.table.move("BOTTOM");
    elif (escolha == 'D' or escolha == 'd'):
        state.table.move("RIGHT");
