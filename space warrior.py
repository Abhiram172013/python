import math
import random
import pygame
SCREENWIDTH=800
SCREENHEIGHT=500
PLAYERSTART_X=370
PLAYERSTART_Y=380
ENEMYSTART_Y_MIN=50
ENEMYSTART_Y_MAX=150
ENEMYSPEED_X=5
ENEMYSPEED_Y=10
BULLETSPEED_Y=10
COLLISSIONDISTANCE=27
pygame.init()

screen=pygame.dislay.set_mode((SCREENWIDTH,SCREENHEIGHT))

background=pygame.image.load('backgroundspacewarrior.png')
pygame.display.set_caption('space invader')
#playerdetails
playerImg=pygame.image.load('player png')
playerx=PLAYERSTART_X
playery=PLAYERSTART_Y
playerx_change=0

enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6

