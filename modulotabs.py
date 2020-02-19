from exceptions import *

class tab:

    def __init__(self):
        self.pos    = []
        self.symbol = ""

    def counter(self,player):
        # return the counter to the players or tabs
        if player.lower() == "b":
            return "n"
        elif player.lower()== "n":
            return "b"
        else:
            return False
    
    def dameValidation(self,matrice,y,x,step):
        by = y
        bx = x
        for i in range(1,step+1):
            y*=i
            x*=i
            if matrice[self.pos[0]+y][self.pos[1]+x] !=[]:
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
                raise invalidmove("you cant move here")
        else:
            if self.dameValidation(matrice,-1,1,step):
                matrice[self.pos[0]-y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] - y
        self.pos[1] = self.pos[1] + x 

    def mLeftUp(self,matrice,step):
        # x,y = step, step
        # if matrice[self.pos[0]-y][self.pos[1]-x] == []  and self.pos[0] >1 and self.pos[1]>1:
           
        #     return -y,-x
        # else:
        #     raise invalidmove("you cant move here")
        x,y = step,step
        if step == 1:
            if matrice[self.pos[0]-y][self.pos[1]-x] == [] and self.pos[0] >1 and self.pos[1]>1: 
                matrice[self.pos[0]-y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        else:
            if self.dameValidation(matrice,-1,-1,step):
                matrice[self.pos[0]-y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] - y
        self.pos[1] = self.pos[1] - x 
   
    def mLeftDown(self,matrice,step):
        # x,y = step,step
        # if matrice[self.pos[0]+y][self.pos[1]-x] == []  and self.pos[0] <8 and self.pos[1]>1:
           
        #     return  y,-x
        # else:
        #     raise invalidmove("you cant move here")
        x,y = step,step
        if step==1:
            if matrice[self.pos[0]+y][self.pos[1]-x] == [] and self.pos[0] <8 and self.pos[1]>1: 
                matrice[self.pos[0]+y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        else:
            if self.dameValidation(matrice,1,-1,step):
                matrice[self.pos[0]+y][self.pos[1]-x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        matrice[self.pos[0]][self.pos[1]] = []
        self.pos[0] = self.pos[0] + y
        self.pos[1] = self.pos[1] - x 

    def mRightDown(self,matrice,step):
        # x,y = step,step
        # if matrice[self.pos[0]+x][self.pos[1]+y] == []  and self.pos[0] <8 and self.pos[1]<8:
            
        #     return  y,x
        # else:
        #     raise invalidmove("you cant move here")
        x,y = step,step
        if step==1:
            if matrice[self.pos[0]+y][self.pos[1]+x] == [] and self.pos[0] <8 and self.pos[1]<8: 
                matrice[self.pos[0]+y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
        else:
            if self.dameValidation(matrice,1,1,step):
                matrice[self.pos[0]+y][self.pos[1]+x] =  matrice[self.pos[0]][self.pos[1]]
            else:
                raise invalidmove("you cant move here")
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
                try:
                    answer = int(input("please enter the box number to be moved: "))
                    if answer < 1 or answer >8:
                        raise invalidrange("please write a number in the range from 1 to 8")
                except:
                    raise invalidrange("please write a number in the range from 1 to 8")

                self.mRightUp(matrice,answer)
                return self.counter(turn)
            else:
                raise invalidmove("you can't move this tab")
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
                raise invalidmove("you can't move this tab")
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
                raise invalidmove("you can't move this tab")     
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
                raise invalidmove("you can't move this tab")

        #-----------------------------------------------------------------------------------------------
    
    def target(self,matrice,player):
        # save oll target that can have the tabs
        targets = ()

        if matrice[self.pos[0]] [self.pos[1]] != []:

            if  self.pos[0] < 7 and self.pos[1] < 7:
            #----------------------------------------------------------------------------------------------------------------
                if  matrice[self.pos[0]+1] [self.pos[1]+1] != []:
                    if matrice[self.pos[0]+1][self.pos[1]+1].symbol.lower() == self.counter(player):
                        if  matrice[self.pos[0]+2][self.pos[1]+2] == []:
                            targets = (self.pos,"RD") 

            if  self.pos[0] >2  and self.pos[1] < 7 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]+1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]+1].symbol.lower()  == self.counter(player):
                        if  matrice[self.pos[0]-2][self.pos[1]+2]  == []:
                            targets = (self.pos,"RU") 

            if self.pos[0] > 2 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]-1][self.pos[1]-1] != []:
                    if matrice[self.pos[0]-1][self.pos[1]-1].symbol.lower()  == self.counter(player):
                        if  matrice[self.pos[0]-2][self.pos[1]-2]  == []:
                            targets = (self.pos,"LU") 

            if self.pos[0] < 7 and self.pos[1] > 2 :
            #----------------------------------------------------------------------------------------------------------------                
                if matrice[self.pos[0]+1][self.pos[1]-1] != []: 
                    if matrice[self.pos[0]+1][self.pos[1]-1].symbol.lower()  == self.counter(player ):
                        if matrice[self.pos[0]+2][self.pos[1]-2]  == []:
                            targets = (self.pos,"LD") 
     
        return targets

    def eat(self,direction,matrice,point): 
        #----------------Validating the eat-----------------
        if direction.upper() == "RU" :
            y1,x1,y2,x2 = -1,1,-2,2

        if direction.upper() == "LU" :
            y1,x1,y2,x2 = -1,-1,-2,-2


        if direction.upper() == "RD" :
            y1,x1,y2,x2 = 1,1,2,2
            
        if direction.upper() == "LD" :
            y1,x1,y2,x2 = 1,-1,2,-2
        #---------------- Make the eat----------------
        matrice[self.pos[0]+y2] [self.pos[1]+x2] = matrice[self.pos[0]] [self.pos[1]]
        matrice[self.pos[0]] [self.pos[1]] = []
        matrice[self.pos[0]+y1] [self.pos[1]+x1] = []
        self.pos[0] = self.pos[0] + y2
        self.pos[1] = self.pos[1] + x2
        targt = self.target(matrice,self.symbol)
        point += 5
        if len(targt)>0:

            for element in targt:
                if element[0] == self.pos[0] and  element[1] == self.pos[1] :
                    return  self.eat(targt[1],matrice,point)
        else:
            return matrice,self.counter(self.symbol),point