from board import *
from modulotabs import *
from os import system
from exceptions import *

tablet = board()
tablet.makematriz()
tablet.teamsGenerate("b",1,1)
tablet.teamsGenerate("n",2,6)

def start():
    if tablet.turn == "":
        tablet.turn == "n"

    system("cls")
    print("is turn of the team ",tablet.turn)
    print(tablet.view())
    # ---------------------------------------------------------------------
    types = input("type de tab an its directions, ejemplo '3A R' ").split(" ")


    try:
        tab = (int(types[0][0]),int(types[0][1]))
        direction =  str(types[1])
        tablet.turn = tablet.matrice[tab[0]][tab[1]].move(direction,tablet.turn,tablet.matrice)
    except invalidmove as e:
        system("cls")
        input(str(e))
    except invalidtab as e:
        system("cls")
        input(str(e))
    except:
        system("cls")
        input("type a correctly tab")

    start()


start()




