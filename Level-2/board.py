import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import global_var

class Map(object):

    height = int(config.rows) 
    width = int(config.columns)

    def __init__(self):
        self.matrix = [[" " for i in range(self.width)] for j in range(self.height)]

        self.start_index = 0
        self.create_sky()
        self.create_ground()
        self.create_left()
        self.create_right()


    def render(self):
        for y in range(3, self.height):
            pr = []
            abc=''
            for x in range(self.start_index, self.start_index + config.columns):
                if y == 3:
                    pr.append(Fore.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                elif y == self.height - 1:
                    pr.append(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                else:
                    pr.append(self.matrix[y][x] + Style.RESET_ALL)
            abc=(''.join(pr))
            print(abc)

    def create_ground(self):
        y = self.height - 1
        for x in range(self.width):
            self.matrix[y][x] = "T"


    def create_sky(self): 
        for x in range(self.width):
            self.matrix[3][x] = "X"


    def create_left(self):
        x = 0
        for y in range(self.height):
            self.matrix[y][x] = "X"


    def create_right(self): 
        x=self.width-1
        for y in range(self.height):
            self.matrix[y][x] = "X"
        
