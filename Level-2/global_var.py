import board
import objects
import config 
from colorama import init as cinit
from colorama import Fore, Back, Style
from time import time
import random

mp = board.Map()

time1= round(time())
time2= round(time())
paddle_ground = mp.height - len(config.paddle) - 1
paddle = objects.Paddle(config.paddle, 5, paddle_ground-1, config.lives)
boss = objects.Boss(config.boss, 5, paddle_ground-33, config.lives)

# a=random.choice([50,60,70,80])
# Thru_Ball=objects.thruball(config.powerup_Thru_Ball,a,6)
# b=random.choice([10,20,30,40])
# exp_paddle=objects.expand(config.powerup_ExpandPaddle,b,6)
# c=random.choice([10,20,30,40])
# shrink_paddle=objects.shrink(config.powerup_ShrinkPaddle,c,16)
# d=random.choice([10,20,30,40])
# fast_ball=objects.fastball(config.powerup_fastball,d,16)
# e=random.choice([10,20,30,40])
# paddle_grab=objects.grab(config.powerup_grab,e,10)
# # multiplier=objects.multiplier(config.powerup_multiplier,75,16)
# bomb=objects.Bomb(config.Bombo,boss._posx+3, paddle_ground-33)
a=10
Thru_Ball=objects.thruball(config.powerup_Thru_Ball,10,6)
b=20
exp_paddle=objects.expand(config.powerup_ExpandPaddle,20,6)
shoot_paddle=objects.shoot(config.powerup_ShootPaddle,45,17)

c=55
shrink_paddle=objects.shrink(config.powerup_ShrinkPaddle,55,16)
d=65
fast_ball=objects.fastball(config.powerup_fastball,65,16)
e=75
paddle_grab=objects.grab(config.powerup_grab,75,16)
# multiplier=objects.multiplier(config.powerup_multiplier,75,16)

ball = objects.Ball(config.ball, paddle.xget() + 4, paddle.yget()-1)


    
redbricks=[]
bluebricks=[]
greenbricks=[]
rainbowbricks=[]
graybricks=[]
magentabricks=[]

########## LEVEL1 ############
j=5
for i in range(0,9):   
    brck=objects.RedBricks(j,6)
    redbricks.append(brck)
    j+=10

j=23
for i in range(0,6):   
    brck=objects.MagentaBricks(j,9)
    magentabricks.append(brck)
    j+=10
    
j=10
for i in range(0,8):   
    brck=objects.BlueBricks(j,8)
    bluebricks.append(brck)
    j+=10

j=5
for i in range(0,9):   
    brck=objects.GreenBricks(j,10)
    greenbricks.append(brck)
    j+=10

j=20
for i in range(0,6):   
    brck=objects.GrayBricks(j,13)
    graybricks.append(brck)
    j+=10
  

j=10
for i in range(0,8):   
    brck=objects.GreenBricks(j,16)
    greenbricks.append(brck)
    j+=10


########## LEVEL2 ############
j=5
for i in range(0,9):  
    if(i%2==1): 
        brck=objects.RedBricks(j,5)
        redbricks.append(brck)
        j+=10
    
    else:
        brck=objects.RedBricks(j,6)
        redbricks.append(brck)
        j+=10

    
j=10
for i in range(0,8):  
    if(i%2==1): 
        brck=objects.BlueBricks(j,9)
        bluebricks.append(brck)
        j+=10
    else: 
        brck=objects.BlueBricks(j,8)
        bluebricks.append(brck)
        j+=10

j=5
for i in range(0,9):   
    if(i%2==1):
        brck=objects.GreenBricks(j,12)
        greenbricks.append(brck)
        j+=10
    
    else:
        brck=objects.GreenBricks(j,11)
        greenbricks.append(brck)
        j+=10

    
########## LEVEL3 ############


j=35
for i in range(0,3):   
    brck=objects.GrayBricks(j,16)
    graybricks.append(brck)
    j+=10

j=5
for i in range(0,9):   
    brck=objects.GreenBricks(j,12)
    greenbricks.append(brck)
    j+=10

j=5
for i in range(0,9):   
    brck=objects.BlueBricks(j,20)
    bluebricks.append(brck)
    j+=10
    

def clearblast():
    if(config.blastflag==1):
        
        for i in range (0,9):
            if(redbricks[i]._posy==config.blasty+1 or redbricks[i]._posy==config.blasty-1 ):
                redbricks[i].strength=0
                redbricks[i].isthere=1
                redbricks[i].clear()
        
        for i in range (0,8):
            if(bluebricks[i]._posy==config.blasty+1 or bluebricks[i]._posy==config.blasty-1 ):
                bluebricks[i].strength=0
                bluebricks[i].isthere=1
                bluebricks[i].clear()
        
        for i in range (0,17):
            if(greenbricks[i]._posy==config.blasty+1 or greenbricks[i]._posy==config.blasty-1 ):
                greenbricks[i].strength=0
                greenbricks[i].isthere=1
                greenbricks[i].clear()
        
        for i in range (0,6):
            if(graybricks[i]._posy==config.blasty+1 or graybricks[i]._posy==config.blasty-1 ):
                graybricks[i].strength=0
                graybricks[i].isthere=1
                graybricks[i].clear()        
        
        for i in range (0,6):
            if(magentabricks[i]._posy==config.blasty ):
                magentabricks[i].strength=0
                magentabricks[i].isthere=1
                magentabricks[i].clear()
    
def callthru_ball():
    Thru_Ball.clear()
    Thru_Ball.move_powerup()
    Thru_Ball.start_pow()
    Thru_Ball.render()
    Thru_Ball.stop_pow()

def callexpand():
    exp_paddle.clear()
    exp_paddle.move_powerup()
    exp_paddle.start_pow()
    exp_paddle.stop_pow()
    exp_paddle.render()

def callshoot():
    shoot_paddle.clear()
    shoot_paddle.move_powerup()
    shoot_paddle.start_pow()
    shoot_paddle.stop_pow()
    shoot_paddle.render()


def callshrink():
    shrink_paddle.clear()
    shrink_paddle.move_powerup()
    shrink_paddle.start_pow()
    shrink_paddle.stop_pow()
    shrink_paddle.render()

def callfastball():
    fast_ball.clear()
    fast_ball.move_powerup()
    fast_ball.start_pow()
    fast_ball.stop_pow()
    fast_ball.render()

def callpaddlegrab():
    paddle_grab.clear()
    paddle_grab.move_powerup()
    paddle_grab.start_pow()
    paddle_grab.stop_pow()
    paddle_grab.render()









