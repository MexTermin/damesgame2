from exceptions import *
from os import system

class Tab:

    def __init__(self):
        self.pos    = []
        self.symbol = ""

    def counter(self,player):
        if player.lower() == "b":
            return "n"
        elif player.lower()== "n":
            return "b"
    
    def dameValidation(self,matrice,y,x,step):
        by = y
        bx = x
        for i in range(1,step+1):
            y*=i
            x*=i
            if  (self.pos[0] + y) < 8 and ( self.pos[0] + y) > 0 and  (self.pos[1] + x ) < 8 and  (self.pos[1] + x) > 0:
                if matrice[self.pos[0]+y][self.pos[1]+x] != [] :  
                    if matrice[self.pos[0]+by*(i+1)][self.pos[1]+bx*(i+1)] != [] or  matrice[self.pos[0]+y][self.pos[1]+x].symbol == self.symbol:
                        return False
            y=by
            x=bx
        return True

    def mRightUp(self,matrice,step):
        x,y = step,step
        if step==1:
            if matrice[self.pos[0]-y][self.pos[1]+x] == [] and self.pos[0] >1 and self.pos[1]<8: 
                matrice[self.pos[0]-y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        else:
            if self.dameValidation(matrice,-1,1,step):
                matrice[self.pos[0]-y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] - y
        self.pos[1] = self.pos[1] + x 

    def mLeftUp(self,matrice,step):

        x,y = step,step
        if step == 1:
            if matrice[self.pos[0]-y][self.pos[1]-x] == [] and self.pos[0] >1 and self.pos[1]>1: 
                matrice[self.pos[0]-y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        else:
            if self.dameValidation(matrice,-1,-1,step):
                matrice[self.pos[0]-y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] - y
        self.pos[1] = self.pos[1] - x 
   
    def mLeftDown(self,matrice,step):

        x,y = step,step
        if step==1:
            if matrice[self.pos[0]+y][self.pos[1]-x] == [] and self.pos[0] <8 and self.pos[1]>1: 
                matrice[self.pos[0]+y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        else:
            if self.dameValidation(matrice,1,-1,step):
                matrice[self.pos[0]+y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] + y
        self.pos[1] = self.pos[1] - x 

    def mRightDown(self,matrice,step):

        x,y = step,step
        if step==1:
            if matrice[self.pos[0]+y][self.pos[1]+x] == [] and self.pos[0] <8 and self.pos[1]<8: 
                matrice[self.pos[0]+y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        else:
            if self.dameValidation(matrice,1,1,step):
                matrice[self.pos[0]+y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise InvalidMove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] + y
        self.pos[1] = self.pos[1] + x 

    def move(self,direction,turn,matrice):
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RU":
            if (turn == "n" and self.symbol =="n") :
                self.mRightUp(matrice,1)
                return self.counter(turn)

            elif self.symbol == self.symbol.upper():
                answer = int(input("please enter the box number to be moved: "))
                if answer < 1 or answer >8:
                    raise InvalidRange("please write a number in the range from 1 to 7")
                self.mRightUp(matrice,answer)
                return self.counter(turn)
            else:
                if self.symbol == turn.lower():
                    raise InvalidMove("you can't move here")
                else:
                    raise InvalidMove("you can't move this tab")
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LU":
            if (turn == "n" and self.symbol =="n") :
                self.mLeftUp(matrice,1)
                return self.counter(turn)

            elif self.symbol == self.symbol.upper():
                answer = int(input("please enter the box number to be moved: "))
                self.mLeftUp(matrice,answer)
                return self.counter(turn)
            else:
                if self.symbol == turn.lower():
                    raise InvalidMove("you can't move here")
                else:
                    raise InvalidMove("you can't move this tab")
        #-----------------------------------------------------------
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "LD":
            if (turn == "b" and self.symbol =="b") :
                self.mLeftDown(matrice,1)
                return self.counter(turn)

            elif self.symbol == self.symbol.upper():
                answer = int(input("please enter the box number to be moved: "))
                self.mLeftDown(matrice,answer)
                return self.counter(turn)
            else:
                if self.symbol == turn.lower():
                    raise InvalidMove("you can't move here")
                else:
                    raise InvalidMove("you can't move this tab")
        #-----------------------------------------------------------
        #-----------------------------------------------------------------------------------------------
        if direction.upper()  == "RD":
            if (turn == "b" and self.symbol =="b") :
                self.mRightDown(matrice,1)
                return self.counter(turn)

            elif self.symbol == self.symbol.upper():
                answer = int(input("please enter the box number to be moved: "))
                self.mRightDown(matrice,answer)
                return self.counter(turn)
            else:
                if self.symbol == turn.lower():
                    raise InvalidMove("you can't move here")
                else:
                    raise InvalidMove("you can't move this tab")
        #-----------------------------------------------------------
        #-----------------------------------------------------------------------------------------------
    
    def target(self,matrice,player):
        """[summary]
        
        Arguments:
            matrice {list} -- [receive an array where the location of all the chips is]
            player {string} -- [receive the player symbol that is n or b]
        
        returns:
            [tuple] -- [returns a tuple  with the card (only single tabs)  he can eat, the address, and in how many boxes is the enemy to eat ]
        """        
        targets = ()

        if matrice[self.pos[0]] [self.pos[1]] != []:
            if  self.pos[0] < 7 and self.pos[1] < 7:
            #----------------------------------------------------------------------------------------------------------------
                if  matrice[self.pos[0]+1] [self.pos[1]+1] != []:
                    if matrice[self.pos[0]+1][self.pos[1]+1].symbol.lower() == self.counter(player) and not self.symbol.isupper():
                        if  matrice[self.pos[0]+2][self.pos[1]+2] == []:
                            targets = (self.pos,"RD") 
                    
            if  self.pos[0] >2  and self.pos[1] < 7 :
            #----------------------------------------------------------------------------------------------------------------            
                if matrice[self.pos[0]-1][self.pos[1]+1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]+1].symbol.lower()  == self.counter(player) and not self.symbol.isupper():
                        if  matrice[self.pos[0]-2][self.pos[1]+2]  == []:
                            targets = (self.pos,"RU") 
  
            if self.pos[0] > 2 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]-1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]-1].symbol.lower()  == self.counter(player) and not self.symbol.isupper():
                        if  matrice[self.pos[0]-2][self.pos[1]-2]  == []:
                            targets = (self.pos,"LU") 

            if self.pos[0] < 7 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]+1][self.pos[1]-1] != []: 
                    if matrice[self.pos[0]+1][self.pos[1]-1].symbol.lower()  == self.counter(player ) and not self.symbol.isupper():
                        if matrice[self.pos[0]+2][self.pos[1]-2]  == []:
                            targets = (self.pos,"LD") 

        return targets

    def eat(self,direction,matrice,point,*args):
        validation = True
        if len(args) > 0 :
            try:
                answer = int(input("Write the final box after eating: "))
                if answer == 0:
                    raise Exception
            except:
                input("Type a correcty end pos ")
                self.eat(direction,matrice,point,args[0])
        if direction.upper() == "RU" :
            if len(args)==0:
                y1,x1,y2,x2 = -1,1,-2,2
            else:
                y1,x1,y2,x2 = -args[0], args[0], -args[0]-answer, args[0]+answer
                ty, tx = self.pos[0]+y2, self.pos[1]+x2
                if  ty > 1 and  tx < 8  :
                    validation = False if (matrice[ty][tx] != []) else True
                else:
                    validation = False

        elif direction.upper() == "LU" :
            if len(args)==0:
                y1,x1,y2,x2 = -1,-1,-2,-2
            else:               
                y1,x1,y2,x2 =  -args[0], -args[0], -args[0]-answer, -args[0]-answer
                ty, tx = self.pos[0]+y2, self.pos[1]+x2
                if  ty > 1 and  tx > 1 :
                    validation = False if (matrice[ty][tx] != []) else True
                else:
                    validation = False
        elif direction.upper() == "RD" :
            if len(args)==0:
                y1,x1,y2,x2 = 1,1,2,2
            else:               
                y1,x1,y2,x2 =  args[0] ,args[0], args[0]+answer, args[0]+answer
                ty, tx = self.pos[0]+y2, self.pos[1]+x2
                if  ty < 8 and  tx < 8:
                    validation = False if (matrice[ty][tx] != []) else True
                else:
                    validation = False
        elif direction.upper() == "LD" :
            if len(args)==0:
                y1,x1,y2,x2 = 1,-1,2,-2
            else:
                y1,x1,y2,x2 = args[0], -args[0], args[0]+answer, -args[0]-answer
                ty, tx = self.pos[0]+y2, self.pos[1]+x2
                if  ty < 8 and tx > 1 :
                    validation = False if (matrice[ty][tx] != []) else True
                else:
                    validation = False
        if validation == False:
            input("you can move here")
            self.eat(direction,matrice,point,args[0])
        #---------------- Make the eat----------------
        matrice[self.pos[0]+y2] [self.pos[1]+x2] = matrice[self.pos[0]] [self.pos[1]]
        matrice[self.pos[0]] [self.pos[1]] = []
        matrice[self.pos[0]+y1] [self.pos[1]+x1] = []
        self.pos[0] = self.pos[0] + y2
        self.pos[1] = self.pos[1] + x2
        point += 5

        if not self.symbol.isupper() :
            targt = self.target(matrice,self.symbol)
        else:
            targt = self.targetDame(matrice,self.symbol.lower())
        if len(targt)>0:
            for element in targt:
                if len(element) ==2:
                    if element[0] == self.pos[0] and  element[1] == self.pos[1] :
                        return  self.eat(targt[1],matrice,point)
                    else:
                        if element[0] == self.pos[0] and  element[1] == self.pos[1] :
                            return  self.eat(targt[1],matrice,point,targt[0][2])
        else:
            return matrice,self.counter(self.symbol),point

    def targetDame(self,matrice,player):
        """[summary]
        
        Arguments:
            matrice {list} -- [receive an array where the location of all the chips is]
            player {string} -- [receive the player symbol that is n or b]
        
        returns:
            [tuple] -- [returns a tuple  with the card(only dames tabs) he can eat, the address, and in how many boxes is the enemy to eat ]
        """        
        targets, y, x = [], self.pos[0], self.pos[1]
        for new in range(1,7):
            if matrice[self.pos[0]] [self.pos[1]] != []:
                #----------------------------------------------------------------------------------------------------------------
                if  (y + new) < 8 and (x + new) < 8:
                    if  matrice[y + new] [x + new] != []:
                        if matrice[y + new][x + new].symbol.lower() == self.counter(player) :
                            if  matrice[y + new + 1][x + new + 1] == []:
                                if self.dameValidation(matrice,1,1,new) :
                                    targets = (self.pos,"RD",new)
                #----------------------------------------------------------------------------------------------------------------            
                if ( y - new )> 1  and (x + new) < 8 :
                    if matrice[y - new][x + new] != []:
                        if matrice[y-new][x + new].symbol.lower()  == self.counter(player) :
                            if  matrice[y - new - 1][x + new + 1]  == []:
                                if self.dameValidation(matrice,-1,1,new) :
                                    targets = (self.pos,"RU",new) 
                #----------------------------------------------------------------------------------------------------------------                
                if (y - new) > 1 and (x - new ) > 1 :
                    if matrice[y - new][x - new] != []:
                        if matrice[y - new][x - new].symbol.lower()  == self.counter(player) :
                            if  matrice[y - new - 1][x - new - 1]  == []:
                                if self.dameValidation(matrice,-1,-1,new) :
                                    targets = (self.pos,"LU",new)
                #----------------------------------------------------------------------------------------------------------------                
                if (y + new) < 8 and (x-new )> 1 :
                    if matrice[y + new][x - new] != []: 
                        if matrice[y + new][ x- new].symbol.lower()  == self.counter(player ):
                            if matrice[y + new + 1][x - new - 1]  == []:
                                if self.dameValidation(matrice,1,-1,new) :
                                    targets = (self.pos,"LD",new) 
        return targets
 