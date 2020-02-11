from modulotabs import *
from coloreshell import *
class board:
    def __init__(self):

        self.matrice = []
        self.turn = "n"
    def makematriz(self):
        for ypos in range(0,9):
            self.matrice.append([])
            for xpos in range (0,9):
                self.matrice[ypos].append([])

    def teamsGenerate(self,simbol,start,row):
        start = start
        for ypos in range(row,row+3):
            for xpos in range(1,9,2):
                f = tab()
                f.symbol = simbol
                if start == 2:
                    f.pos =[ypos,xpos+1]
                    self.matrice[ypos][xpos+1]=f
                else:
                    f.pos =[ypos,xpos]
                    self.matrice[ypos][xpos]=f
            start = 1 if (start == 2) else 2

    def view(self):
        indicator = 0
        colour = 0
        pos = ""
        tabla = "  a  b  c  d  e  f  g  h "
        for vertical in range(1,len(self.matrice)):
            colour = 0 if  (indicator == 1) else 1
            tabla+="\n" + str(vertical)
            for i in range(1,9):
                c = Colour.BLACK if (colour ==0) else Colour.WHITE1
                pos =   "   "  if (self.matrice[vertical][i] == [])  else " "   +   str(self.matrice[vertical][i].symbol)  +   " "
                tabla += c +  pos +  Colour.END
                colour = 1  if (colour == 0) else  0 
            indicator = 1 if  (indicator == 0) else 0
        return tabla
            
    def position(self):
        pass
