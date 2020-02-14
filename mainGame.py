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
    if len(tablet.position(tablet.matrice)["n"]) == 0 and len(tablet.position(tablet.matrice)["N"])  == 0:
        system("cls")
        input("Congratulation player *B* you have won the  game")
        return
    if len(tablet.position(tablet.matrice)["b"]) == 0 and len(tablet.position(tablet.matrice)["B"])  == 0:
        system("cls")
        input("Congratulation player *N* you have won the  game")
        return
    #----------------------doing the selection to begginig game---------------------
    # if tablet.turn == "":
    #     select = input("type your tab team 'N or B' ").split(" ")
    #     if select[0].lower() == "n":
    #         tablet.turn = "n"

    #     elif select[0].lower()  == "b":
    #         tablet.turn = "b"
    #     else:
    #         input("type a correctly team ")
    #         start()
    #----------------------Make the view to the tablet -----------------------------
    if tablet.turn == "n":
        poin = tablet.pteam1
    else:
        poin = tablet.pteam2
    print("Is turn of the team -",tablet.turn, "- you have {} points".format(poin))
    print(tablet.view())
    #-------------------------------------------------------------------------------
    searching = ["n","N"] if  (tablet.turn == "n") else ["b","B"]
    pos = tablet.position(tablet.matrice)
    targets = []
    #-------------------------------------------------make dame-----------------------------------------------
    tablet.makedame()

    #------------------------------------------------Multi-target------------------------------------------------
    for element in searching:
        for tabs in pos[element]:
            if len(tabs.target(tablet.matrice,tablet.turn) ) > 0: 
                targets.append(tabs.target(tablet.matrice,tablet.turn) )
    #----------------------------------------------Single eat(obligatory)-----------------------------------------------------------
    if len(targets) == 1:
        input("You should eat whit the tab, "+ str(targets[0]))
        tablet.matrice,tablet.turn,poin = tablet.matrice[targets[0][0][0]] [targets[0][0][1]].eat(targets[0][1],tablet.matrice,poin)
        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        tablet.makedame()
        start()
    #---------------------------------------------------------MultiEat---------------------------------------------------------------------
    elif len(targets) > 1:
        print(targets)
        # -----------------------------------------------------Watching targets-------------------------------------------------------------------
        for i in range(len(targets)):
            print("       ",i,"        ",end="")

        try:
            answer = int(input("  Select one target to eat:  "))
        except :
            input( "You should type a number between ", len(targets) )
            start()
        tablet.matrice,tablet.turn,poin= tablet.matrice[targets[answer][0][0] ] [ targets[answer][0][1] ].eat(targets[answer][1],tablet.matrice,poin)
        #--addated point to each team--
        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        start()
    # ------------------------------------------make the move--------------------------------------------------------------------------
    
    types = input("Type de tab and its directions, example '3A RU' ").split(" ")

    try:
        #----------------------------------Controller the steps------------------------------------
        tab = (int(types[0][0]),int( tablet.translate(types[0][1])) )
        direction =  str(types[1])
        if direction.upper() != "RD" and direction.upper() != "LD":
            if direction.upper() != "LU" and direction.upper() != "RU":
                system("cls")
                input("You should typing correctly direction")
                start()
        tablet.turn = tablet.matrice[tab[0]][tab[1]].move(direction,tablet.turn,tablet.matrice)
        #------------------------------------Controller the exceptions-----------------------------
    except invalidmove as e:
        system("cls")
        input(str(e))

    except invalidtab as e:
        system("cls")
        input(str(e))
    except:
        system("cls")
        input("Type a correctly tab")
    #-------------- verify is there's a new dame---------
    tablet.makedame()
    start()

start()
