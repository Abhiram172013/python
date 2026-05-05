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
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for _i in range(6):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,SCREENWIDTH-64))
    enemyY.append(random.randint(ENEMYSTART_Y_MIN,ENEMYSTART_Y_MAX))
    enemyX_change.append(ENEMYSPEED_X)
    enemyY_change.append(ENEMYSPEED_Y)

bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=PLAYERSTART_Y
bulletX_change=0
bulletY_change=BULLETSPEED_Y
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"      
    screen.blit(bulletImg,(x+16,y+10))
def isCollission(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return distance < COLLISIONDISTANCE
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.quit:
            runing=False
        if event.type==pygame.KEYDOWN:
            if event.type==pygame.k_LEFT:
                playerx_change=-5
            if event.type==pygame.k_RIGHT:
                 playerx_change=-5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletX=playerx
                fire_bullet(bulletX,bulletY)
        



