import os
import numpy as np
from colorama import init as cinit
from colorama import Fore, Back, Style
import random
import global_var 
import global_funct
import config
from time import time,sleep
import random

color_matrix=["Fore.GREEN + Back.GREEN","Fore.BLUE + Back.BLUE","Fore.RED + Back.RED"]
class Object():
    
    def __init__(self, character, x, y):
        self._posx = x
        self._posy = y
        self._width = len(character[0])
        self._height = len(character)
        self._shape = character
        self.buff=0

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    def xget(self):
        return self._posx

    def yget(self):
        return self._posy
    
    def xdset(self, x):
        self._posx = x
    
    def ydset(self, x):
        self._posy = x

    def xset(self, x):
        self._posx += x
    
    def yset(self, x):
        self._posy += x

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx ] = " "


class Paddle(Object):
    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        self.__lives = 3
        self.__coins = 0
        self.__score = 0
        self._width=len(character[0])

    def lives(self):
        return self.__lives
    
    def score(self):
        return self.__score

    def get_width(self):
        return self._width

class Boss(Object):
    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        self.__lives = 12
        self.__coins = 0
        self.__score = 0
        self._width=len(character[0])
    def move_boss(self):
        self._posx= global_var.paddle._posx
        self._posy =global_var.paddle._posy-32
        # print(self._posx)
    def lives(self):
        return self.__lives
    
    def score(self):
        return self.__score

    def get_width(self):
        return self._width

class Bomb(Object):
    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._width=len(character[0])
        self.speed=1
        self.check=0

    def move_bomb(self):
        if(self.yget()==global_var.paddle.yget() and self.xget()>=global_var.paddle.xget() and self.xget()<=global_var.paddle.xget()+global_var.paddle._width and self.check==0):
            self.FLAG=1
            self.speed=0
            self._shape=" "
            self.check=1
            config.lives-=1
            os.system('aplay -q ./sounds/losinglife.wav&')
            
        if(self.yget()!=global_var.paddle_ground+1):
            self.yset(self.speed) 
        return 0

class Bullet(Object):
    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._width=len(character[0])
        self.speed=-1
        self.check=0

    def move_bullet(self):
        self.yset(self.speed)
        

    
class Ball(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self.check_ball2=0

    def initial_movement(self):
        self._posx= global_var.paddle.xget()+4

    def move_ball(self):
        if(self.xget() >= 97):
            config.Ball_speedx*=-1
            os.system('aplay -q ./sounds/wall.wav&')
            config.Ball_speedx1*=-1
        elif(self.yget() <= 4):
            config.Ball_speedy*=-1
            config.Ball_speedy1*=-1
        elif(self.yget() == config.rows-1 and config.Ball_speedy > 0):
            self._posx=global_var.paddle._posx
            self._posy=global_var.paddle._posy-2
            config.check=0
            config.lives-=1
            os.system('aplay -q ./sounds/losinglife.wav&')
            config.thru_flag1=0
            config.thru_flag=0
            config.expand_flag=0
            config.expand_flag1=0
            if(config.shrink_flag==1 or config.shrink_flag1==0):
                config.shrink_flag=0
                config.shrink_flag1=0
                global_var.paddle._shape=config.paddle1
                global_var.paddle._width=10
            
            config.paddle_grab_flag=0
            config.paddle_grab_flag1=0
            global_var.paddle_grab.stop_pow()

        elif(self.xget() <= 1):
            config.Ball_speedx*=-1
            config.Ball_speedx1*=-1
            os.system('aplay -q ./sounds/wall.wav&')
            # self._posx=global_var.paddle._posx

        if(self.check_ball2!=1):
            self.xset(config.Ball_speedx)
            self.yset(config.Ball_speedy)
        else:
            self.xset(config.Ball_speedx1)
            self.yset(config.Ball_speedy1)
        
    def cleared(self):
        if(global_var.mp.matrix[self._posy][self._posx]=="*"):
            global_var.mp.matrix[self._posy][self._posx] = " "

    def render(self):
        global_var.mp.matrix[self._posy][self._posx] = "*"
            
    def check_collision(self):
        if(self.yget()==global_var.paddle._posy and config.Ball_speedy>0):
            for i in range (0,global_var.paddle._width):
                if(i==0 or i==global_var.paddle._width -1 or i==1 or i==global_var.paddle._width -2 ):
                    j=1
                else:
                    j=0

                if(self.xget() ==global_var.paddle.xget()+i):
                    os.system('aplay -q ./sounds/collisionballwithbrick.wav&')
                    if(config.ff==1):
                        config.gg=1
                    if(config.paddle_grab_flag==1):
                        self._posx= global_var.paddle.xget()+4
                        self._posy=global_var.paddle.yget()-1
                        config.check=0
                        config.paddle_grab_flag=0
                        

                    if(i==0 or i==1):
                        config.Ball_speedx-=j
                        config.Ball_speedy*=-1

                    elif(i==global_var.paddle._width -1 or i==global_var.paddle._width -2):
                        config.Ball_speedx+=j
                        config.Ball_speedy*=-1
                    
                    else:
                        config.Ball_speedx+=j
                        config.Ball_speedy*=-1

    def check_collision_boss(self):
        if(self.yget()<=global_var.boss._posy+5 and config.Ball_speedy <0):
            for i in range (0,15):
                if(self.xget()==global_var.paddle.xget()+i):
                    config.Ball_speedy*=-1
                    config.boss_live-=1
                    

class Powerups():
    def __init__(self, character ,x, y):
        self._posx = x
        self._posy = y
        self._width = len(character[0])
        self._height = len(character)
        self._shape = character
        self.FLAG=0
        self.speed=1
        self.speedx=0
        self.samay=0
        self.check=0
        self.ll=0

    def xget(self):
        return self._posx

    def yget(self):
        return self._posy
    
    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]
    
    def stat_pow(self):
        if(self.FLAG==1):
            config.checkii=1

    def move_powerup(self):
        
        if(self.yget()==global_var.paddle.yget() and self.xget()>=global_var.paddle.xget() and self.xget()<=global_var.paddle.xget()+global_var.paddle._width and self.check==0):
                self.FLAG=1
                self.samay=round(time())
                config.pow_beg=self.samay
                self.speed=0
                self.speedx=0
                self._shape=" " 
                self.check=1
                
        if(self.yget()!=global_var.paddle_ground+1):
            if(self.ll<=2):
                self.yset(-self.speed)
                self.ll+=1
            else:
                self.yset(self.speed)

            self.xset(self.speedx)
            return 0
        
        if(self.xget() >= 97):
            self.speedx*=-1
        
        elif(self.xget() <= 1):
            self.speedx*=-1
            

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
    
    def xset(self, x):
        self._posx += x
    
    def yset(self, x):
        self._posy += x

class thruball(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y) 
        
    def start_pow(self):
        if(self.FLAG==1):
            config.thru_flag=1

    def stop_pow(self):

        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG=0
            config.thru_flag=0
            config.thru_flag1=0 
            

class expand(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)  
    
    def start_pow(self):
        if(self.FLAG==1):
            global_var.paddle._shape=config.paddle2
            global_var.paddle._width=12
            config.expand_flag=1
    
    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG=0
            config.expand_flag=0
            config.expand_flag1=0
            global_var.paddle._shape=config.paddle1
            global_var.paddle._width=10


class shoot(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)  
    
    def start_pow(self):
        if(self.FLAG==1):
            global_var.paddle._shape=config.paddle4
            global_var.paddle._width=10
            config.shoot_flag=1
    
    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG=0
            config.shoot_flag=0
            config.shoot_flag1=0
            global_var.paddle._shape=config.paddle1
            global_var.paddle._width=10


class shrink(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)  
    
    def start_pow(self):
        if(self.FLAG==1):
            global_var.paddle._shape=config.paddle3
            global_var.paddle._width=5
            config.shrink_flag=1

    def stop_pow(self):
        if(round(time())-self.samay >= 5 and self.FLAG==1):
            
            config.shrink_flag=0
            config.shrink_flag1=0
            global_var.paddle._shape=config.paddle1
            global_var.paddle._width=10
            self.FLAG=0

class multiplier(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)  
    
    def start_pow(self):
        if(self.FLAG==1):
            config.multiplier_flag=1


class fastball(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)   
        self.check1=0
    def start_pow(self):
        if(self.FLAG==1):
            if (config.Ball_speedx<0 and self.check1==0):
                config.Ball_speedx-=1
                self.check1=1
                # print("badhiya baa  ")

            elif(config.Ball_speedx>=0 and self.check1==0):
                config.Ball_speedx+=1
                self.check1=1
                # print("kaisan baaa")


    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG=0
            config.fast_flag=0
            if (config.Ball_speedx<0):
                config.Ball_speedx+=1
            else:
                config.Ball_speedx-=1

class grab(Powerups):
    def __init__ (self,character,x,y):
        super().__init__(character,x, y)  
    
    def start_pow(self):
        if(self.FLAG==1):
            config.paddle_grab_flag=1
    
    def stop_pow(self):
        if(round(time())-self.samay >= 10) and self.FLAG==1:
            self.FLAG=0
            config.paddle_grab_flag=0
            config.paddle_grab_flag1=0



class Brick():
    def __init__(self,x,y):   
        self.height=1
        self.width=9
        self.shape= [["$","$","$","$","$","$","$","$","$"]]
        self._posx=x
        self._posy=y
        self.isthere = 0
                
    def clear(self):
        for i in range(self.width):
            for j in range(self.height):
                global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
            

    def render(self):
        if(self.isthere==0):
            for i in range(self.width):
                for j in range(self.height):
                    if(self.strength==3):
                        global_var.mp.matrix[j+self._posy][i+self._posx] = Fore.RED+ Back.RED + self.shape[j][i]
                    elif(self.strength==2):
                        global_var.mp.matrix[j+self._posy][i+self._posx] = Fore.BLUE+ Back.BLUE + self.shape[j][i]
                    elif(self.strength==1):
                        global_var.mp.matrix[j+self._posy][i+self._posx] = Fore.GREEN+ Back.GREEN+ self.shape[j][i]


    def move_brick(self):
        if(round(time())-global_var.time2)==20:
            config.ff=1

    def down_brick(self):
        if(config.gg==1):
            self._posy+=1
                  
    def check_collision_brick(self):
            for i in range(self.width):
                for j in range(self.height):       
                    if i + self._posx==global_var.ball.xget() + config.Ball_speedx and self._posy==global_var.ball.yget()+ config.Ball_speedy and self.isthere==0:
                        
                        if(config.thru_flag==1):
                            self.strength=0
                            self.isthere=1       
                            config.score+=1
                            for i in range(self.width):
                                for j in range(self.height):
                                    global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                    
                        else:
                            config.Ball_speedy*=-1
                            self.strength-=1
                            os.system('aplay -q ./sounds/collisionballwithbrick.wav&')
                            if(self.strength==0):
                                self.isthere=1
                                config.score+=1
                                for i in range(self.width):
                                    for j in range(self.height):
                                        global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                            
                                if(self._posx<=global_var.a and self._posx+self.width-1>=global_var.a  and self._posy==6):
                                    config.thru_flag1=1

                                if(self._posx<=global_var.b and self._posx+self.width-1>=global_var.b and self._posy==6):
                                    config.expand_flag1=1

                                if(self._posx<=global_var.c and self._posx+self.width-1>=global_var.c and self._posy==16):
                                    config.shrink_flag1=1   
                                    global_var.shrink_paddle.speedx=config.Ball_speedx
                                if(self._posx<=global_var.d and self._posx+self.width-1>=global_var.d and self._posy==16):
                                    config.fast_flag=1
                                    global_var.fast_ball.speedx=config.Ball_speedx

                                if(self._posx<=global_var.e and self._posx+self.width-1>=global_var.e and self._posy==16):
                                    config.paddle_grab_flag1=1

    def reduce_brick(self,x,y):
        for i in range(self.width):
            for j in range(self.height):       
                if i + self._posx==x and self._posy==y and self.isthere==0:
                        self.strength-=1
                        if(self.strength==0):
                            self.isthere=1
                            config.score+=1
                            for i in range(self.width):
                                for j in range(self.height):
                                    global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                            
                                

class RedBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color = Fore.RED+ Back.RED
        self.strength = 3
                        
                    
class BlueBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color = Fore.BLUE + Back.BLUE
        self.strength = 2
                        

class GreenBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color = Fore.GREEN + Back.GREEN
        self.strength = 1
    
class RainbowBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
    
        if(config.rainbow_flag==0):
            if(round(time())%3==0):
                self.color = Fore.GREEN + Back.GREEN
                self.strength = 1
            
            elif(round(time())%3==1):
                self.color = Fore.BLUE + Back.BLUE
                self.strength = 2

            elif(round(time())%3==2):
                self.color = Fore.RED + Back.RED
                self.strength = 3
        
    def check_collision_brick(self):
            for i in range(self.width):
                for j in range(self.height):       
                    if i + self._posx==global_var.ball.xget() + config.Ball_speedx and self._posy==global_var.ball.yget()+ config.Ball_speedy and self.isthere==0:
                        
                        if(config.thru_flag==1):
                            self.strength=0
                            self.isthere=1       
                            config.score+=1
                            for i in range(self.width):
                                for j in range(self.height):
                                    global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                    
                        else:
                            config.Ball_speedy*=-1
                            self.strength-=1
                            config.rainbow_flag=1
                            if(self.strength==0):
                                self.isthere=1
                                config.score+=1
                                for i in range(self.width):
                                    for j in range(self.height):
                                        global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                                config.shoot_flag1=1
                                

class GrayBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color = Fore.WHITE + Back.WHITE
        self.strength = 100

    def render(self):
        if(self.isthere==0):
            for i in range(self.width):
                for j in range(self.height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self.color + self.shape[j][i]
        
                    
class MagentaBricks(Brick):
    def __init__ (self,x,y):
        super().__init__(x, y)
        self.color = Fore.MAGENTA + Back.MAGENTA 
        self.strength = 1
        
    def render(self):
        if(self.isthere==0):
            for i in range(self.width):
                for j in range(self.height):
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self.color + self.shape[j][i]
                
    def check_collision_brick(self):
            for i in range(self.width):
                for j in range(self.height):    
                    if i + self._posx==global_var.ball.xget() +  config.Ball_speedx and self._posy==global_var.ball.yget()+config.Ball_speedy and self.isthere==0:
                        if(config.thru_flag==1):
                            self.strength=0
                            config.blastflag=1
                            config.blasty=self._posy
                            if(self.strength==0):
                                self.isthere=1                
                                for i in range(self.width):
                                    for j in range(self.height):
                                        global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                        
                        else:
                            config.Ball_speedy*=-1
                            self.strength-=1
                            config.blastflag=1
                            config.blasty=self._posy
                            if(self.strength==0):
                                os.system('aplay -q ./sounds/Explosion.wav&')
                                config.score+=13
                                self.isthere=1                
                                for i in range(self.width):
                                    for j in range(self.height):
                                        global_var.mp.matrix[j+self._posy][i+self._posx ] = " "
                        