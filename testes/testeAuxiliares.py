import sys;
sys.path.append("..");

from funcoesAuxiliares import *;

resultado = copy([[1, 0, 2],
                  [5, 3, 7],
                  [4, 6, 8]]);

print(resultado);

list = [1,2,3,4,5,6,7];
print(list.pop(0));
print(list);

list2 = ['a', 'b', 'c'];
print(list + list2);
print(list2 + list);