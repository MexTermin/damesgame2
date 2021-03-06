from modulotabs import *
from coloreshell import *
import os
class Board:

    def __init__(self):

        self.matrice = []
        self.turn = "n"
        self.pteam1 = 0
        self.pteam2 = 0

    def makeMatriz(self):
        # this method make the principal matrice
        for ypos in range(0,9):
            self.matrice.append([])
            for xpos in range (0,9):
                self.matrice[ypos].append([])

    def teamsGenerate(self,simbol,start,row):
        """[summary]
            this function generate the teams
        Arguments:
            simbol {[string]} -- [a letter that represents the teams]
            start {[int]} -- [is the initial column of the board where the symbol will be place]
            row {[int]} -- [is the initial row of the board where the symbol will be place]
        """        
        start = start
        for ypos in range(row,row+3):
            for xpos in range(1,9,2):
                f = Tab()
                f.symbol = simbol
                if start == 2:
                    f.pos =[ypos,xpos+1]
                    self.matrice[ypos][xpos+1]=f
                else:
                    f.pos =[ypos,xpos]
                    self.matrice[ypos][xpos]=f
            start = 1 if (start == 2) else 2

    def view(self):
        #--------------------------------this method render de principal view of the program--------------------
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
                if self.matrice[vertical][i] != []:
                    if self.matrice[vertical][i].symbol.upper() == "N" :
                        c = Colour.WHITE3
                tabla += c +  pos +  Colour.END
                colour = 1  if (colour == 0) else  0 
            indicator = 1 if  (indicator == 0) else 0
        return tabla
            
    def position(self, matrice):
        # save all position for any tabs
        allPos = { "n": [], "b":[],"N":[],"B":[] }
        for element in matrice:
            for ovject in element:
                if ovject != []:
                    if  ovject.symbol == "n":
                        allPos["n"].append(ovject)
                    elif  ovject.symbol == "b":
                        allPos["b"].append(ovject)
                    elif  ovject.symbol == "N":
                        allPos["N"].append(ovject)
                    elif  ovject.symbol == "B":
                        allPos["B"].append(ovject)
        
        return allPos
    
    def makeDame(self):
        # this method verify is there's any new dame in the tablet
        for element in range(1,9,7 ):
            for tabs in range(1,9):
                if element == 1:
                    if self.matrice[element][tabs] != []:
                        if self.matrice[element][tabs].symbol == "n": 
                            self.matrice[element][tabs].symbol = "N"
                            self.matrice[element][tabs].isDame = True
                if element == 8:
                    if self.matrice[element][tabs] != []:
                        if self.matrice[element][tabs].symbol == "b": 
                            self.matrice[element][tabs].symbol = "B"
                            self.matrice[element][tabs].isDame = True
                              
    def clearWindows(self):
        if os.name == "posix":
            os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            os.system ("cls")
    
    def translate(self,string):
        # this method translate the input
        if not isinstance(string,int):
            string = string.lower()
        listing = {
             "a":1,
             "b":2,
             "c":3,
             "d":4,
             "e":5,
             "f":6,
             "g":7,
             "h":8,

             1:"a",
             2:"b",
             3:"c",
             4:"d",
             5:"e",
             6:"f",
             7:"g",
             8:"h"

        }
        return listing[string]
