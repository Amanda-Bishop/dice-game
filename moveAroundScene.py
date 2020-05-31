##############################################################################
## File Name: moveAroundScene.py                                            ##
## Description: This program moves a character around a scene which         ##
##              scrolls when they reach the edges of the window             ##
## Input: The user can move the ball up/down/left/right with the arrows.    ##
##############################################################################
import math
import pygame                           
pygame.init()
 
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
BLACK = (0,0,0)

OUTLINE=0

# RED player properties x,y,width,height and speeds                   
rx = 190
ry = 190
rw = 10
rh = 20
speed_x = 3                             
speed_y = 3

# background location properties
bgx = 0
bgy = 0

# determines how close to the edge of the screen the player gets before the background moves
edgeGap = 30

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    win.fill(GREEN)
    #draw the background based on it's properties
    win.blit(bg,(bgx,bgy))
    #draw the red rectangle based on it's properties
    pygame.draw.rect(win,BLACK,(rx,ry,rw,rh),OUTLINE)
    pygame.display.update()




#---------------------------------------#
# the main program begins here          #
#---------------------------------------#

# create game window
win=pygame.display.set_mode((400,400))
bg = pygame.image.load('dice1.png')

inPlay = True                                      
while inPlay:
    redraw_game_window()                
    pygame.time.delay(20)
    # check if user closes the window using mouse on 'X'
    for event in pygame.event.get(): 
         if event.type == pygame.QUIT:
            inPlay = False
    #move player by pressing keys                                                   
    keys = pygame.key.get_pressed()                                           
    if keys[pygame.K_ESCAPE]:           
        inPlay = False                  
    if keys[pygame.K_LEFT]:             
        rx -= speed_x       
    if keys[pygame.K_RIGHT]:            
        rx += speed_x        
    if keys[pygame.K_UP]:               
        ry -= speed_y       
    if keys[pygame.K_DOWN]:             
        ry += speed_y
        
    # if the player get's close to the edge, stop them moving
    # and adjust the draw position of the background so it appears to be moving
    if rx > win.get_width() - edgeGap - rw:
        bgx -= speed_x
        rx -= speed_x
    elif rx < edgeGap:
        bgx += speed_x
        rx += speed_x
    if ry > win.get_height() - edgeGap - rh:
        bgy -= speed_y
        ry -= speed_y
    elif ry < edgeGap:
        bgy += speed_y
        ry += speed_y
    
    

#---------------------------------------#                                        
pygame.quit()                           # always quit pygame when done!


















##def isCollision():
##    collision = False
##    if bx <= rx <= bx + bw or bx <= rx + rw <= bx + bw:
##        if by <= ry <= by + bh or by <= ry + rh <= by + bh:
##            collision = True
##    return collision
