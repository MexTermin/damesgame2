from exceptions import *

class tab:

    def __init__(self):
        self.pos    = []
        self.dame   = False
        self.symbol = ""

    def counter(self,player):

        if player.lower() == "b":
            return "n"
        elif player.lower()== "n":
            return "b"
        else:
            return False

    def move(self,direction,turn,matrice):
#-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RU":
            if (turn == "n" and self.symbol =="n") or self.symbol == self.symbol.upper():
                if matrice[self.pos[0]-1][self.pos[1]+1] == []:
                    y1,x1 = -1,1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant move this tab")
#-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LU":
            if (turn == "n" and self.symbol =="n" )or self.symbol == self.symbol.upper():
                if matrice[self.pos[0]-1][self.pos[1]-1] == []:
                    y1,x1 = -1,-1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant vome this tab")
#-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LD":
            if (turn == "b" and self.symbol =="b") or self.symbol == self.symbol.upper():
                if matrice[self.pos[0]+1][self.pos[1]-1] == []:
                    y1,x1 = 1,-1
                else:
                    raise invalidmove("you cant move here")
            else:
                raise invalidmove("klk you cant vome this tab")         
#-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RD":
            if (turn == "b" and self.symbol =="b") or self.symbol == self.symbol.upper():
                if matrice[self.pos[0]+1][self.pos[1]+1] == []:
                    x1,y1 = 1,1

                else:
                    raise invalidmove("you cant move here")
#-----------------------------------------------------------------------------------------------                
            else:
                raise invalidmove("klk you cant vome this tab")

        matrice[self.pos[0]+y1][self.pos[1]+x1] =  matrice[self.pos[0]][self.pos[1]]
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] + y1
        self.pos[1] = self.pos[1] + x1  
        return self.counter(turn)
#-----------------------------------------------------------------------------------------------
    def target(self,matrice,player):

        targets = ()

        if matrice[self.pos[0]] [self.pos[1]] != []:

            if  self.pos[0] < 7 and self.pos[1] < 7:
            #----------------------------------------------------------------------------------------------------------------
                if  matrice[self.pos[0]+1] [self.pos[1]+1] != []:
                    if self.symbol == "b" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]+1][self.pos[1]+1].symbol.lower() == self.counter(player):
                            if  matrice[self.pos[0]+2][self.pos[1]+2] == []:
                                targets = (self.pos,"RD") 

            if  self.pos[0] >2  and self.pos[1] < 7 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]+1] != []:
                    if self.symbol == "n" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]-1][self.pos[1]+1].symbol.lower()  == self.counter(player):
                            if  matrice[self.pos[0]-2][self.pos[1]+2]  == []:
                                targets = (self.pos,"RU") 

            if self.pos[0] > 2 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]-1] != []:
                    if self.symbol == "n" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]-1][self.pos[1]-1].symbol.lower()  == self.counter(player):
                            if  matrice[self.pos[0]-2][self.pos[1]-2]  == []:
                                targets = (self.pos,"LU") 

            if self.pos[0] < 7 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]+1][self.pos[1]-1] != []:
                    if self.symbol == "b" or self.symbol == self.symbol.upper():
                        if matrice[self.pos[0]+1][self.pos[1]-1].symbol.lower()  == self.counter(player ):
                            if matrice[self.pos[0]+2][self.pos[1]-2]  == []:
                                targets = (self.pos,"LD") 
     
        return targets

    def eat(self,direction,matrice,point): 
        #----------------------------------Refactorizar----------------------------------
        #--------------------------------------------------------------------------------
        if direction.upper() == "RU" :
            if (self.symbol == "n" or self.symbol == self.symbol.upper()):
                matrice[self.pos[0]-2] [self.pos[1]+2] = matrice[self.pos[0]] [self.pos[1]]
                matrice[self.pos[0]] [self.pos[1]] = []
                matrice[self.pos[0]-1] [self.pos[1]+1] = []
                self.pos[0] = self.pos[0] - 2
                self.pos[1] = self.pos[1] + 2

        if direction.upper() == "LU" :
            if   (self.symbol == "n" or self.symbol == self.symbol.upper()) :
                matrice[self.pos[0]-2] [self.pos[1]-2] = matrice[self.pos[0]] [self.pos[1]]
                matrice[self.pos[0]] [self.pos[1]] = []
                matrice[self.pos[0]-1] [self.pos[1]-1] = []
                self.pos[0] = self.pos[0] - 2
                self.pos[1] = self.pos[1] - 2


        if direction.upper() == "RD" :
            if  (self.symbol == "b" or self.symbol == self.symbol.upper()):
                matrice[self.pos[0]+2] [self.pos[1]+2] = matrice[self.pos[0]] [self.pos[1]]
                matrice[self.pos[0]] [self.pos[1]] = []
                matrice[self.pos[0]+1] [self.pos[1]+1] = []
                self.pos[0] = self.pos[0] + 2
                self.pos[1] = self.pos[1] + 2
            
        if direction.upper() == "LD" :
            if (self.symbol == "b" or self.symbol == self.symbol.upper()):
                matrice[self.pos[0]+2] [self.pos[1]-2] = matrice[self.pos[0]] [self.pos[1]]
                matrice[self.pos[0]] [self.pos[1]] = []
                matrice[self.pos[0]+1] [self.pos[1]-1] = []
                self.pos[0] = self.pos[0] + 2
                self.pos[1] = self.pos[1] - 2

        targt = self.target(matrice,self.symbol)
        point += 5
        if len(targt)>0:

            for element in targt:
                if element[0] == self.pos[0] and  element[1] == self.pos[1] :
                    return  self.eat(targt[1],matrice,point)
        else:
            return matrice,self.counter(self.symbol),point