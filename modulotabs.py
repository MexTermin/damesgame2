from exceptions import *

class tab:


    def __init__(self):
        self.pos    = []
        self.dame   = False
        self.symbol = ""
        if self.dame == True:
            self.symbol = self.symbol.upper()

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
                    self.pos[0] = self.pos[0] - 1
                    self.pos[1] = self.pos[1] + 1
                else:
                    raise invalidmove("you cant move here")

            else:
                raise invalidmove("klk you cant move this tab")
        if direction.upper()  == "LU":
            if turn == "n":
                if matrice[self.pos[0]-1][self.pos[1]-1] == []:
                    matrice[self.pos[0]-1][self.pos[1]-1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
                    self.pos[0] = self.pos[0] - 1
                    self.pos[1] = self.pos[1] - 1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant vome this tab")
        if direction.upper()  == "LD":
            if turn == "b":
                if matrice[self.pos[0]+1][self.pos[1]-1] == []:
                    matrice[self.pos[0]+1][self.pos[1]-1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
                    self.pos[0] = self.pos[0] + 1
                    self.pos[1] = self.pos[1] - 1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant vome this tab")          
        if direction.upper()  == "RD":
            if turn == "b":
                if matrice[self.pos[0]+1][self.pos[1]+1] == []:
                    matrice[self.pos[0]+1][self.pos[1]+1] =  matrice[self.pos[0]][self.pos[1]]
                    matrice[self.pos[0]][self.pos[1]] = []
                    self.pos[0] = self.pos[0] + 1
                    self.pos[1] = self.pos[1] + 1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant vome this tab")       
        return self.counter(turn)

    def target(self,matrice,player):
        targets = []

        if matrice[self.pos[0]] [self.pos[1]] != []:

            if  self.pos[0] < 7 and self.pos[1] < 7:
            #----------------------------------------------------------------------------------------------------------------
                if  matrice[self.pos[0]+1] [self.pos[1]+1] != []:
                    if matrice[self.pos[0]+1][self.pos[1]+1].symbol == self.counter(player):
                        if  matrice[self.pos[0]+2][self.pos[1]+2] == []:
                            targets.append( (self.pos,"RD") )

            if  self.pos[0] >2  and self.pos[1] < 7 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]+1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]+1].symbol == self.counter(player):
                        if  matrice[self.pos[0]-2][self.pos[1]+2]  == []:
                            targets.append( (self.pos,"RU") )

            if self.pos[0] > 2 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]-1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]-1].symbol == self.counter(player):
                        if  matrice[self.pos[0]-2][self.pos[1]-2]  == []:
                            targets.append( (self.pos,"LU") )

            if self.pos[0] < 7 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]+1][self.pos[1]-1] != []:
                    if matrice[self.pos[0]+1][self.pos[1]-1].symbol == self.counter(player ):
                        if matrice[self.pos[0]+2][self.pos[1]-2]  == []:
                            targets.append( (self.pos,"LD") )
     
        return targets

    def eat(self,direction,matrice):
        if direction.upper() == "RU":
            matrice[self.pos[0]-2] [self.pos[1]+2] = matrice[self.pos[0]] [self.pos[1]]
            matrice[self.pos[0]] [self.pos[1]] = []
            matrice[self.pos[0]-1] [self.pos[1]+1] = []
            self.pos[0] = self.pos[0] - 2
            self.pos[1] = self.pos[1] + 2

        if direction.upper() == "LU":
            matrice[self.pos[0]-2] [self.pos[1]-2] = matrice[self.pos[0]] [self.pos[1]]
            matrice[self.pos[0]] [self.pos[1]] = []
            matrice[self.pos[0]-1] [self.pos[1]-1] = []
            self.pos[0] = self.pos[0] - 2
            self.pos[1] = self.pos[1] - 2


        if direction.upper() == "RD":
            matrice[self.pos[0]+2] [self.pos[1]+2] = matrice[self.pos[0]] [self.pos[1]]
            matrice[self.pos[0]] [self.pos[1]] = []
            matrice[self.pos[0]+1] [self.pos[1]+1] = []
            self.pos[0] = self.pos[0] + 2
            self.pos[1] = self.pos[1] + 2
            
        if direction.upper() == "LD":
            matrice[self.pos[0]+2] [self.pos[1]-2] = matrice[self.pos[0]] [self.pos[1]]
            matrice[self.pos[0]] [self.pos[1]] = []
            matrice[self.pos[0]+1] [self.pos[1]-1] = []
            self.pos[0] = self.pos[0] - 2
            self.pos[1] = self.pos[1] + 2

        targt = self.target(matrice,self.symbol)
        if len(targt)>0:
            for element in targt:
                if element[0][0] == self.pos[0] and  element[0][1] == self.pos[1] :
                    return  self.eat(element[1],matrice)
        else:
            return matrice,self.counter(self.symbol)