from board import *
from modulotabs import *
from exceptions import *
import sys, os

tablet = Board()
tablet.makeMatriz()

# g = Tab()
# g.symbol="n"

tablet.teamsGenerate("b", 1, 1)
tablet.teamsGenerate("n", 2, 6)
# f = Tab()
# f.symbol = "N"
# f.isDame = True
# tablet.matrice[1][7] = f
# tablet.matrice[1][7].pos = [1,7]
# #------------------------------------
# f = Tab()
# f.symbol = "b"
# tablet.matrice[3][5] = f
# tablet.matrice[3][5].pos = [3,5]

# f = Tab()
# f.symbol = "b"
# tablet.matrice[5][3] = f
# tablet.matrice[5][3].pos = [5,3]

# f = Tab()
# f.symbol = "b"
# tablet.matrice[7][3] = f
# tablet.matrice[7][3].pos = [7,3]

# f = Tab()
# f.symbol = "b"
# tablet.matrice[8][7] = f
# tablet.matrice[8][7].pos = [8,7]


tablet

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


def start():
    tablet.clearWindows()
    if len(tablet.position(tablet.matrice)["n"]) == 0 and len(tablet.position(tablet.matrice)["N"]) == 0:
        tablet.clearWindows()
        input("                     Congratulation player *B* you have won the  game     ")
        return
    if len(tablet.position(tablet.matrice)["b"]) == 0 and len(tablet.position(tablet.matrice)["B"]) == 0:
        tablet.clearWindows()
        input("                     Congratulation player *N* you have won the  game    ")
        return

    if tablet.turn == "n":
        poin = tablet.pteam1
    else:
        poin = tablet.pteam2
    print("Is turn of the team -", tablet.turn, "- you have {} points".format(poin))
    print(tablet.view())
    # -------------------------------------------------------------------------------
    searching = ["n", "N"] if (tablet.turn == "n") else ["b", "B"]
    pos = tablet.position(tablet.matrice)
    killer = []
    # -------------------------------------------------make dame-----------------------------------------------
    tablet.makeDame()
    # ------------------------------------------------Multi-target------------------------------------------------
    for element in searching:
        for tabs in pos[element]:
            
            if element.isupper():
                if len(tabs.targetDame(tablet.matrice, tablet.turn)) > 0:
                    killer.append(tabs.targetDame(tablet.matrice, tablet.turn))
            elif len(tabs.target(tablet.matrice, tablet.turn)) > 0:
                killer.append(tabs.target(tablet.matrice, tablet.turn))
    # ----------------------------------------------Single eat(obligatory)-----------------------------1------------------------------
    if len(killer) == 1:
        input("You should eat whit the tab, " + str(killer[0]))
        if len(killer[0]) == 3:
            tablet.matrice, tablet.turn, poin,verification = tablet.matrice[killer[0][0][0]][killer[0][0][1]].eat(
                killer[0][1], tablet.matrice, poin, killer[0][2])
            if verification == False:
                start()

        else:
            tablet.matrice, tablet.turn, poin,verification = tablet.matrice[killer[0][0][0]][killer[0][0][1]].eat(
                killer[0][1], tablet.matrice, poin)
            if verification == False:
                start()

        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        tablet.makeDame()
        start()
    # ---------------------------------------------------------MultiEat---------------------------------------------------------------------
    elif len(killer) > 1:
        for i in range(len(killer)):
            view = killer[i]
            view[0][1] = tablet.translate(view[0][1])
            print("*"+str(i)+"*:"+str(view)+"  ", end="")
            view[0][1] = tablet.translate(view[0][1])

        try:
            answer = int(input("  Select one target to eat:  "))
            if answer < 0 or answer > len(killer):
                raise Exception
        except:
            tablet.clearWindows()
            input("You should type a number between 0 and {}: ".format( len(killer)-1 ))
            start()

        if len(killer[answer])==3:
            tablet.matrice, tablet.turn, poin,verification = tablet.matrice[killer[answer][0][0]][killer[answer][0][1]].eat(
                killer[answer][1], tablet.matrice, poin,  killer[answer][2])
            if verification == False:
                start()
        else:
            tablet.matrice, tablet.turn, poin,verification = tablet.matrice[killer[answer][0][0]][killer[answer][0][1]].eat(
            killer[answer][1], tablet.matrice, poin)
            if verification == False:
                start()

        # --addated point to each team--
        if tablet.turn == "n":
            tablet.pteam2 = poin
        else:
            tablet.pteam1 = poin
        start()

    # ------------------------------------------make the move--------------------------------------------------------------------------
    types = input(
        "Type de tab and its directions, example '3A RU' ").split(" ")
    try:
        # ----------------------------------Controller the steps------------------------------------
        tab = (int(types[0][0]), int(tablet.translate(types[0][1])))
        direction = str(types[1])
        if direction.upper() != "RD" and direction.upper() != "LD":
            if direction.upper() != "LU" and direction.upper() != "RU":
                tablet.clearWindows()
                input("You should typing correctly direction")
                start()
        tablet.turn = tablet.matrice[tab[0]][tab[1]].move( direction, tablet.turn, tablet.matrice)
        # ------------------------------------Controller the exceptions-----------------------------
    except InvalidMove as e:
        tablet.clearWindows()
        input(str(e))
    except InvalidTab as e:
        tablet.clearWindows()
        input(str(e))
    except InvalidRange as e:
        tablet.clearWindows()
        input(str(e))
    except:
        tablet.clearWindows()
        input("Type a correctly tab")
    # # -------------- verify is there's a new dame---------
    tablet.makeDame()

    start()


start()

while True:
    answer = input("Type 'Yes' if you wan play again, else type 'No': ")
    if answer.lower() == "yes":
        restart_program()
    elif answer.lower() == "no":
        exit()
