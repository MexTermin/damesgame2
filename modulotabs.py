from exceptions import *
class tab:


    def __init__(self):
        self.pos    = []
        self.dame   = False
        self.symbol = ""


    def counter(self,player):

        if player == "b":
            return "n"
        elif player == "n":
            return "b"
        else:
            return False

    def move(self,direction,turn,matrice):
        if direction.upper()  == "RU":
            if turn == "n":
                if matrice[self.pos[0]-1][self.pos[1]+1] == []:
                    matrice[self.pos[0]-1][self.pos[1]+1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
            else:
                raise invalidmove("klk you cant vome this tab")
        if direction.upper()  == "LU":
            if turn == "n":
                if matrice[self.pos[0]-1][self.pos[1]-1] == []:
                    matrice[self.pos[0]-1][self.pos[1]-1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
            else:
                raise invalidmove("klk you cant vome this tab")
        if direction.upper()  == "LD":
            if turn == "b":
                if matrice[self.pos[0]+1][self.pos[1]-1] == []:
                    matrice[self.pos[0]+1][self.pos[1]-1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
            else:
                raise invalidmove("klk you cant vome this tab")          
        if direction.upper()  == "RD":
            if turn == "b":
                if matrice[self.pos[0]+1][self.pos[1]+1] == []:
                    matrice[self.pos[0]+1][self.pos[1]+1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
            else:
                raise invalidmove("klk you cant vome this tab")       
        return self.counter(turn)

    def target(self,matrice):
        # targets = []
        # if matrice[pos]
        pass

    def eat(self):
        pass
