# Handles all the logic of the game
from Snake import *
from A_star import *
from World import *
import sys

def main(gui):
    if gui == True:
        gui = GUI()
        


if __name__ == "__main__":
    if sys.argv[1] == "gui":
        main(True)
    else:
        main(False)