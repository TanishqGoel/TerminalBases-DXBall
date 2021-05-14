import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
# import objects
from math import pi
import numpy as np 

columns = 100
rows = 40
score=0
lives = 3
check=0
paddle1 = [["Y", "Y", "Y", "Y", "Y", "Y","Y","Y","Y","Y"]]
paddle2 = [["Y", "Y", "Y", "Y", "Y", "Y","Y","Y","Y","Y","Y","Y"]]
paddle3 = [["Y", "Y", "Y", "Y", "Y"]]
# paddle_width=9
ball=[["*"]]
powerup_Thru_Ball=[["T"]]
powerup_ExpandPaddle=[["E"]]
powerup_ShrinkPaddle=[["S"]]
powerup_fastball=[["F"]]
powerup_multiplier=[["M"]]
powerup_grab=[["G"]]
Ball_speedx=0
Ball_speedy=-1
Ball_speedx1=1
Ball_speedy1=-1
pow_speed=1
thru_flag1=0
thru_flag=0
fast_flag=0
expand_flag=0
expand_flag1=0
multiplier_flag=0
multiplier_flag1=0
shrink_flag=0
shrink_flag1=0
blastflag=0
blasty=-2
shrink_flag=0
checkii=0
paddle_grab_flag=0
paddle_grab_flag1=0

if(expand_flag==1):
    paddle=paddle2

elif(shrink_flag==1):
    paddle=paddle3
else:
    paddle=paddle1

# art="   _____                         ____                 
#   / ____|                       / __ \                
#  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
#  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
#  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
#   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   "