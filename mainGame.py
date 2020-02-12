from board import *
from modulotabs import *
from os import system
from exceptions import *

tablet = board()
tablet.makematriz()
tablet.teamsGenerate("b",1,1)
tablet.teamsGenerate("n",2,6)

def start():
    system("cls")
    #----------------------doing the selection to begginig game---------------------
    if tablet.turn == "":
        select = input("type your tab team 'N or B' ").split(" ")
        if select[0].lower() == "n":
            tablet.turn = "n"

        elif select[1].lower()  == "b":
            tablet.turn = "b"
        else:
            input("type a correctly team ")
            start()
    #---------------------Make the view to the tablet ----------------------------
    system("cls")
    print("is turn of the team ",tablet.turn)
    print(tablet.view())
    #----------------------------------------------------------------------------
    searching = ["n","N"] if  (tablet.turn == "n") else ["b","B"]
    pos = tablet.position(tablet.matrice)
    targets = []

    for element in searching:
        for tabs in pos[element]:
            if len(tabs.target(tablet.matrice,tablet.turn) ) > 0: 
                targets.append(tabs.target(tablet.matrice,tablet.turn) )
  
    if len(targets) >0:
        print("the targest are")
        print(targets)
        for i in range(len(targets)):
            print("       ",i,"        ",end="")

        try:
            answer = int(input("  ...Select your answer: "))

        except :
            input( "You should type a number between ", len(targets) )
            start()
        tablet.matrice,tablet.turn = tablet.matrice[targets[answer][0][0][0] ] [ targets[answer][0][0][1] ].eat(targets[answer][0][1],tablet.matrice)
        start()


    # ---------------------------------------------------------------------
    types = input("type de tab an its directions, ejemplo '3A R' ").split(" ")


    try:
        tab = (int(types[0][0]),int( tablet.translate(types[0][1])) )
        direction =  str(types[1])
        if direction.upper() != "RD" and direction.upper() != "LD":
            if direction.upper() != "LU" and direction.upper() != "RU":
                input("you should typing correctly direction")
                start()
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

