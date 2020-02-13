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

        elif select[0].lower()  == "b":
            tablet.turn = "b"
        else:
            input("type a correctly team ")
            start()
    #----------------------Make the view to the tablet -----------------------------
    system("cls")
    if tablet.turn == "n":
        poin = tablet.pteam1
    else:
        poin = tablet.pteam2
    print("is turn of the team ",tablet.turn, "you have {} points".format(poin))
    print(tablet.view())
    #-------------------------------------------------------------------------------
    searching = ["n","N"] if  (tablet.turn == "n") else ["b","B"]
    pos = tablet.position(tablet.matrice)
    targets = []
    #-------------------------------------------------make dame-----------------------------------------------
    for element in range(1,9,7 ):
        for tabs in range(1,9):
            if element == 1:
                if tablet.matrice[element][tabs] != []:
                    if tablet.matrice[element][tabs].symbol == "n": 
                        tablet.matrice[element][tabs].symbol = "N"
            if element == 8:
                if tablet.matrice[element][tabs] != []:
                    if tablet.matrice[element][tabs].symbol == "b": 
                        tablet.matrice[element][tabs].symbol = "B"

    #-------------------------------------------------------------------Multi-eat------------------------------------------------
    for element in searching:
        for tabs in pos[element]:
            if len(tabs.target(tablet.matrice,tablet.turn) ) > 0: 
                targets.append(tabs.target(tablet.matrice,tablet.turn) )
    if len(targets) == 1:
        input("you should eat whit the tab, "+ str(targets[0]))
        tablet.matrice,tablet.turn,poin = tablet.matrice[targets[0][0][0]] [targets[0][0][1]].eat(targets[0][1],tablet.matrice,poin)
        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        start()
    elif len(targets) > 1:
        print("the targest are")
        print(targets)
        for i in range(len(targets)):
            print("       ",i,"        ",end="")

        try:
            answer = int(input("  ...Select your answer: "))

        except :
            input( "You should type a number between ", len(targets) )
            start()
        tablet.matrice,tablet.turn,poin= tablet.matrice[targets[answer][0][0] ] [ targets[answer][0][1] ].eat(targets[answer][1],tablet.matrice,poin)
        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin

        start()
    # ------------------------------------------------------------------make the move--------------------------------------------
    
    types = input("type de tab and its directions, example '3A R' ").split(" ")

    try:
        #--------------------------------------Controller the steps----------------------------------------
        tab = (int(types[0][0]),int( tablet.translate(types[0][1])) )
        direction =  str(types[1])
        if direction.upper() != "RD" and direction.upper() != "LD":
            if direction.upper() != "LU" and direction.upper() != "RU":
                input("you should typing correctly direction")
                start()
        tablet.turn = tablet.matrice[tab[0]][tab[1]].move(direction,tablet.turn,tablet.matrice)
        #---------------------------------------Controller the exceptions-----------------------------------

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

