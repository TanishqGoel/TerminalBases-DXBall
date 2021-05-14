import config
import random
import os
import global_var
from colorama import init, Fore, Back, Style
from time import time


def create_header():
    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + 
    ("SCORE: " + str(config.score) + "   |  LIVES: " + str(config.lives) + "   |  TIME: " + str(round(time())-global_var.time1)).center(config.columns))
    print(Style.RESET_ALL)

def create_footer():
    print("\033[41;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + 
    ("Boss Health Left: " + str(config.boss_live) ).center(config.columns))
    print(Style.RESET_ALL)

def create_Shootingfooter():
    print("\033[41;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT + 
    ("Powerup left: " + str(10-(round(time()-config.pow_beg))) ).center(config.columns))
    print(Style.RESET_ALL)

def display_ending(message):
    os.system('tput reset')
    # print(Fore.CYAN + Style.BRIGHT + (config.art).center(config.columns))
    # print(Style.RESET_ALL)
    if(config.win_flag==1):
        print(("\ \   / /          \ \        / (_)        ").center(config.columns))
        print((" \ \_/ /__  _   _   \ \  /\  / / _ _ __    ").center(config.columns))
        print(("  \   / _ \| | | |   \ \/  \/ / | | '_ \   ").center(config.columns))
        print(("   | | (_) | |_| |    \  /\  /  | | | | |  ").center(config.columns))
        print(("   |_|\___/ \__,_|     \/  \/   |_|_| |_|  ").center(config.columns))
    else:
        print(("    _____                         ____                 ").center(config.columns))
        print(("   / ____|                       / __ \                ").center(config.columns))
        print(("  | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ").center(config.columns))
        print(("  | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|").center(config.columns))
        print(("  | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ").center(config.columns))
        print(("   \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ").center(config.columns))
        print(Style.RESET_ALL)
        print(Fore.CYAN + Style.BRIGHT + ("SCORE: " + str(config.score)).center(config.columns))
        print(Style.RESET_ALL)
        print(Fore.CYAN + Style.BRIGHT + ("LIVES: " + str(config.lives)).center(config.columns))
        print(Style.RESET_ALL)
        print(Fore.CYAN + Style.BRIGHT + ("TIME: " + str(round(time())-global_var.time1)).center(config.columns))
        print(Style.RESET_ALL)
    return

def print_board():
    create_header()
    global_var.mp.render()
    global_var.paddle.render()
    if(config.Game_Level==3):
        create_footer()
    elif(config.shoot_flag==1):
        create_Shootingfooter()

def Brick_Recursion():
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