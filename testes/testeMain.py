import sys;
sys.path.append("..");

from main import *;

exemplo = Node();
actions = exemplo.possible_actions();

for each in actions:
    each[0].show_all();
