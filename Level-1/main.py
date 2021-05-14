from input import *
import os
import global_var
from global_var import paddle, ball 
import global_funct
import objects
import config
from time import time, sleep
flag=0
if(__name__=="__main__"):
    Get_obj=Get()
    while(1):
        paddle.clear()
        ball.check_collision()
        inp= input_to(Get_obj)
        sys.stdout.write("\033c")
        if(inp!=None):
            sleep(0.05)

        if(inp =='q'):
            break
        
        if inp == 'd':
            if paddle.xget() <= global_var.mp.start_index + config.columns - 3 - paddle._width and paddle.xget() <= 1090:
                paddle.xset(4)
            
        if inp == 'a':
            if paddle.xget() > global_var.mp.start_index + 1:
                paddle.xset(-4)
        
    
        if config.lives == 0:
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
        

        for i in range (0,9):
            global_var.redbricks[i].render()
            global_var.redbricks[i].check_collision_brick()
            
        for i in range (0,8):
            global_var.bluebricks[i].render()
            global_var.bluebricks[i].check_collision_brick()
            
        for i in range (0,17):
            global_var.greenbricks[i].render()
            global_var.greenbricks[i].check_collision_brick() 
        
        for i in range (0,6):
            global_var.graybricks[i].render()
            global_var.graybricks[i].check_collision_brick() 

        for i in range (0,6):
            global_var.magentabricks[i].render()
            global_var.magentabricks[i].check_collision_brick() 
        
        if(config.thru_flag1==1):
            global_var.callthru_ball()
        
        if(config.expand_flag1==1):
            global_var.callexpand()

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
       

