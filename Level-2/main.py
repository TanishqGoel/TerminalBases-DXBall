from input import *
import os
import global_var
from global_var import paddle, ball , boss
import global_funct
import objects
import config
from time import time, sleep
flag=0
lg=0
bulletl=[]
bulletr=[]

if(__name__=="__main__"):
    Get_obj=Get()
    while(1):
        if(config.Game_Level>=4):
            message = "Game over!"
            global_funct.display_ending(message)
            break
  
        paddle.clear()
        
        ball.check_collision()
        inp= input_to(Get_obj)
        sys.stdout.write("\033c")
        if(inp!=None):
            sleep(0.1)

        if(inp =='q'):
            break
        
        if inp == 'd':
            if paddle.xget() <= global_var.mp.start_index + config.columns - 3 - paddle._width and paddle.xget() <= 1090:
                paddle.xset(4)
            
        if inp == 'a':
            if paddle.xget() > global_var.mp.start_index + 1:
                paddle.xset(-4)
        
        if inp=='k' or (config.score%22==0 and config.score!=0):
            config.score+=1
            config.Game_Level+=1
            config.time2=round(time())
            config.gg=0
            ball.clear()
            ball._posx=global_var.paddle._posx
            ball._posy=global_var.paddle._posy-2
            config.check=0
            config.thru_flag1=0
            config.thru_flag=0
            config.expand_flag=0
            config.expand_flag1=0
            config.Ball_speedx=0
            if(config.shrink_flag==1 or config.shrink_flag1==0):
                config.shrink_flag=0
                config.shrink_flag1=0
                global_var.paddle._shape=config.paddle1
                global_var.paddle._width=10

        if config.lives == 0:
            os.system('aplay -q ./sounds/gameover.wav&')
            message = "Game over!"
            global_funct.display_ending(message)
            break
    
        if config.boss_live == 0:
            config.win_flag=1
            os.system('aplay -q ./sounds/gameover.wav&')
            message = "Game over!"
            global_funct.display_ending(message)
            break

        if(config.check!=1):
            ball.render()
            ball.cleared()
            ball.initial_movement()
            ball.render()

        if(inp=='e' or config.check==1):
            config.check=1
            ball.cleared()
            ball.move_ball()
            ball.cleared()
            ball.render()
        

        for i in range (0,len(global_var.redbricks)):
            if(global_var.redbricks[i]._posy>=35 and lg==0):
                os.system('aplay -q ./sounds/gameover.wav&')
                config.Game_Level=4
                lg=1
                message = "Game over!"
                global_funct.display_ending(message)
                exit
            

        for i in range (0,len(global_var.bluebricks)):
            if(global_var.bluebricks[i]._posy>=35 and lg==0):
                os.system('aplay -q ./sounds/gameover.wav&')
                config.Game_Level=4
                lg=1
                message = "Game over!"
                global_funct.display_ending(message)
                break
        
        for i in range (0,len(global_var.greenbricks)):
            if(global_var.greenbricks[i]._posy>=35 and lg==0):
                os.system('aplay -q ./sounds/gameover.wav&')
                config.Game_Level=4
                lg=1
                message = "Game over!"
                global_funct.display_ending(message)
                break
        
        for i in range (0,len(global_var.graybricks)):
            if(global_var.graybricks[i]._posy>=35 and lg==0):
                os.system('aplay -q ./sounds/gameover.wav&')
                config.Game_Level=4
                lg=1
                message = "Game over!"
                global_funct.display_ending(message)
                break
        
        for i in range (0,len(global_var.magentabricks)):
            if(global_var.magentabricks[i]._posy>=35 and lg!=0):
                os.system('aplay -q ./sounds/gameover.wav&')
                config.Game_Level=4
                lg=1
                message = "Game over!"
                global_funct.display_ending(message)
                break        
                

        if(config.Game_Level==1):
            for i in range (0,9):
                global_var.redbricks[i].render()
                global_var.redbricks[i].move_brick()
                global_var.redbricks[i].check_collision_brick()
                
            for i in range (0,8):
                global_var.bluebricks[i].render()
                global_var.bluebricks[i].move_brick()
                global_var.bluebricks[i].check_collision_brick()
            
            for i in range (0,17):
                global_var.greenbricks[i].render()
                global_var.greenbricks[i].move_brick()
                global_var.greenbricks[i].check_collision_brick() 
            
            for i in range (0,6):
                global_var.graybricks[i].render()
                global_var.graybricks[i].move_brick()
                global_var.graybricks[i].check_collision_brick() 

            
            for i in range (0,6):
                global_var.magentabricks[i].render()
                global_var.magentabricks[i].move_brick()
                global_var.magentabricks[i].check_collision_brick() 
            
            if(config.gg==1):
                for i in range (0,9):
                    global_var.redbricks[i].clear()
                    global_var.redbricks[i].down_brick()
                for i in range (0,8):
                    global_var.bluebricks[i].clear()
                    global_var.bluebricks[i].down_brick()
                for i in range (0,17):
                    global_var.greenbricks[i].clear()
                    global_var.greenbricks[i].down_brick()
                for i in range (0,6):
                    global_var.graybricks[i].clear()
                    global_var.magentabricks[i].clear()
                    global_var.graybricks[i].down_brick()
                    global_var.magentabricks[i].down_brick()
                config.gg=0

        elif(config.Game_Level==2):
            for i in range (0,9):
                global_var.redbricks[i].clear()
                
            for i in range (0,8):
                global_var.bluebricks[i].clear()
            
            for i in range (0,18):
                global_var.greenbricks[i].clear()
            
            for i in range (0,6):
                global_var.graybricks[i].clear()

            
            for i in range (0,6):
                global_var.magentabricks[i].clear()

            for i in range (9,18):
                global_var.redbricks[i].render()
                global_var.redbricks[i].move_brick()
                global_var.redbricks[i].check_collision_brick()
                
            for i in range (8,16):
                global_var.bluebricks[i].render()
                global_var.bluebricks[i].move_brick()
                global_var.bluebricks[i].check_collision_brick()
            
            for i in range (17,26):
                global_var.greenbricks[i].render()
                global_var.greenbricks[i].move_brick()
                global_var.greenbricks[i].check_collision_brick() 
            
            if(config.rainbow_flag==0):
                brock1=objects.RainbowBricks(45,17)
                
            brock1.render()
            brock1.move_brick()
            brock1.check_collision_brick()

            if(config.gg==1):
                for i in range (9,18):
                    global_var.redbricks[i].clear()
                    global_var.redbricks[i].down_brick()
                for i in range (8,16):
                    global_var.bluebricks[i].clear()
                    global_var.bluebricks[i].down_brick()
                for i in range (17,26):
                    global_var.greenbricks[i].clear()
                    global_var.greenbricks[i].down_brick()
                brock1.clear()
                brock1.down_brick()
                config.gg=0

            if(config.shoot_flag==1):
                if(config.go%4==0):
                    bullet1=objects.Bullet(config.Bullet,paddle._posx,paddle._posy)
                    bullet2=objects.Bullet(config.Bullet,paddle._posx+11,paddle._posy)
                    bulletl.append(bullet1)
                    bulletr.append(bullet2)

                for i in range(0,config.go//4):
                    bulletl[i].clear()
                    bulletl[i].move_bullet()
                    bulletl[i].render()

                    bulletr[i].clear()
                    bulletr[i].move_bullet()
                    bulletr[i].render()

                    if(bulletl[i]._posy<=4):
                        bulletl[i].speed=0
                        bulletl[i].clear()
                        

                    if(bulletr[i]._posy<=4):
                        bulletr[i].speed=0
                        bulletr[i].clear()
                        

                    for j in range (9,18):
                        global_var.redbricks[j].reduce_brick(bulletl[i]._posx,bulletl[i]._posy)
                        global_var.redbricks[j].reduce_brick(bulletr[i]._posx,bulletr[i]._posy)
                    for j in range (8,16):
                        global_var.bluebricks[j].reduce_brick(bulletl[i]._posx,bulletl[i]._posy)
                        global_var.bluebricks[j].reduce_brick(bulletr[i]._posx,bulletr[i]._posy)
                    
                    for j in range (17,26):
                        global_var.greenbricks[j].reduce_brick(bulletl[i]._posx,bulletl[i]._posy)
                        global_var.greenbricks[j].reduce_brick(bulletr[i]._posx,bulletr[i]._posy)
                    
                config.go+=1
            
            else:
                for i in range(0,config.go//4):
                    bulletl[i].clear()
                    bulletr[i].clear()
        
        elif(config.Game_Level==3):
            for i in range (9,18):
                global_var.redbricks[i].clear()
                
            for i in range (8,16):
                global_var.bluebricks[i].clear()
            
            for i in range (17,26):
                global_var.greenbricks[i].clear()
            
            brock1.clear()
            ball.check_collision_boss()
            if(round(time())-config.bomb_time >=10):
                config.bomb_time=round(time())
                bomb=objects.Bomb(config.Bombo,boss._posx+7, global_var.paddle_ground-31)
            bomb.clear()
            bomb.move_bomb()
            bomb.render()
            for i in range (6,9):
                global_var.graybricks[i].render()
                global_var.graybricks[i].check_collision_brick() 

            if(config.boss_live <= 6):
                for i in range (26,35):
                    global_var.greenbricks[i].render()
                    global_var.greenbricks[i].check_collision_brick() 

            if(config.boss_live <= 3):
                for i in range (16,25):
                    global_var.bluebricks[i].render()
                    global_var.bluebricks[i].check_collision_brick() 
            


            boss.clear()
            boss.move_boss()
            boss.render()
    
        
        if(config.thru_flag1==1):
            global_var.callthru_ball()
        
        if(config.expand_flag1==1):
            global_var.callexpand()
        
        if(config.shoot_flag1==1):
            global_var.callshoot()

        if(config.shrink_flag1==1):
            global_var.callshrink()
        
        if(config.fast_flag==1):
            global_var.callfastball()
        
        if(config.paddle_grab_flag1==1):
            global_var.callpaddlegrab()
        
        # if(config.multiplier_flag1==1):
        #     global_var.callmultiplier()
        
        global_var.clearblast()
        
        
        
        paddle.render()
        
        global_funct.print_board()
       

