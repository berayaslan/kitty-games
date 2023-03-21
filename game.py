from turtle import back
import pygame
import math
import random

pygame.init() 

screen = pygame.display.set_mode((800,600))

#baslik ve logo
pygame.display.set_caption("kitty games") 
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon) 

#oyuncu
playerImg = pygame.image.load('cat.png')
playerX = 370 
playerY= 480 
playerX_change=0

#arkaplan
background = pygame.image.load('background.png')


#dusman

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=4

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('rat.png'))
    enemyX.append(random.randint(0,720))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0)
    enemyY_change.append(2)

#mermi
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=3
bullet_state="ready"

#skor

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX=10
textY=10

def show_Score(x,y):
    score = font.render("Score: " + str(score_value),True,(255, 102, 153))
    screen.blit(score,(x,y))

def player(x,y):
    screen.blit(playerImg,(x,y)) 

def enemy(x,y,i): 
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def is_Collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +( math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    return False


#game dongusu
running = True
while running: 

    # RGB = RED - GREEN - BLUE
    screen.blit(background,(0,0))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

     
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_a: 
                playerX_change=-2.5
            if event.key == pygame.K_d:
                playerX_change=2.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d: 
                playerX_change=0

    
    playerX+=playerX_change 

    if playerX<= 0: 
        playerX=0
    elif playerX>=720:
        playerX=720

    #dusman hareketleri
    enemyY+=enemyY_change 
    for i in range(num_of_enemies):
        if enemyY[i]<= 0:
            enemyX_change[i]=0
            enemyY[i]+=enemyY_change[i]
        elif enemyY[i]>=720:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]

        #collision
        collision = is_Collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value +=1
            enemyX[i] = random.randint(0,720)
            enemyY[i] = random.randint(50,150)
        
        enemy(enemyX[i],enemyY[i],i)


    #mermi hareketleri
    if bulletY <=0:
        bulletY=480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    

    player(playerX,playerY) 
    show_Score(textX,textY)
    pygame.display.update() 
