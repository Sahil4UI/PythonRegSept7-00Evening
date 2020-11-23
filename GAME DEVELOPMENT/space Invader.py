import pygame
import random

pygame.init()

width=1000
height=700
craftwidth=60
craftheight=80



img=pygame.image.load("back1.jpg")
img=pygame.transform.scale(img,(width,height))
img01=pygame.image.load("back1.jpg")
img01=pygame.transform.scale(img01,(width,height))


img2=pygame.image.load("spacecraft.png")
img2=pygame.transform.scale(img2,(craftwidth,craftheight))
enemyWidth = 100
enemyHeight = 50
enemyImg = pygame.image.load('enemy1.png')
enemyImg = pygame.transform.scale(enemyImg,(enemyWidth,enemyHeight))
enemyImg = pygame.transform.rotate(enemyImg,180)
gameboard=pygame.display.set_mode((width,height))

white=255,255,255
red=255,0,0
black=0,0,0
blue=0,0,255
newcolor=random.randint(0,255),random.randint(0,255),random.randint(0,255)

def score(counter):
    font=pygame.font.SysFont(None,40)
    text=font.render(f"Score:{counter}",True,red)
    gameboard.blit(text,(50,50))


def spacecraft():
    b_x1=0
    b_y1=0
    b_x2=0
    b_y2=-height
    
    x=200
    y=620
    counter=0
    movex=0
    movey=0
    a=3
    bulletWidth = 8
    bulletHeight = 14
    bulletY = y+20
    shoot = False
    moveBullet=0
    
    
    enemyList = []
    nrow = 5
    ncol = width//enemyWidth
    enemyRectList = []

    for i in range(nrow):
        for j in range(ncol):
            enemy = (enemyWidth+45)*j,(enemyHeight+45)*i
            enemyList.append(enemy)
            enemyRect = pygame.Rect((enemyWidth+45)*j,(enemyHeight+45)*i,enemyWidth,enemyHeight)
            enemyRectList.append(enemyRect)
            
    while True:
        if shoot==False:
            bulletX = x+(craftwidth//2)-(bulletWidth//2)
        gameboard.blit(img,(b_x1,b_y1))
        gameboard.blit(img01,(b_x2,b_y2))
        bulletRect = pygame.draw.rect(gameboard,red,[bulletX,bulletY,bulletWidth,bulletHeight])
        spacecraft=pygame.Rect(x,y,craftwidth,craftheight)        
        gameboard.blit(img2,(x,y))

        for i in range(len(enemyList)):
            gameboard.blit(enemyImg,enemyList[i])
            
        if b_y1 > height:
            b_y1=-height
        if b_y2 >height:
            b_y2=-height

        b_y1+=5
        b_y2+=5
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_RIGHT:
                    movex=a

                    
                if event.key==pygame.K_LEFT:
                    movex=-a

                if event.key==pygame.K_SPACE:
                    moveBullet=-3
                    shoot=True
                    
                    
            else:movex=0

        x+=movex
        bulletY += moveBullet
        
        for i in range(len(enemyRectList)):
            if enemyRectList[i].colliderect(bulletRect):
                del enemyRectList[i]
                del enemyList[i]
                moveBullet=0
                bulletY = y+20
                bulletX = x+(craftwidth//2)-(bulletWidth//2)
                shoot = False
                break
        if x<0:
            x=950

        if x>(width-craftwidth):
            x=0

        if bulletY<0:
            moveBullet=0
            bulletY=y+20
            #bulletX = x+(craftwidth//2)-(bulletWidth//2)
            shoot=False

        
            
        pygame.display.flip()
    

def start():
    font=pygame.font.SysFont(None,100)
    text=font.render("SPACE INVADING GAME",True,red)
    font2=pygame.font.SysFont(None,50)
    text2=font2.render("Press Enter to start the Game",True,red)

    while True:
        gameboard.blit(img,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_RETURN:
                    spacecraft()
                    
        gameboard.blit(text2,(200,400))
        gameboard.blit(text,(100,100))
        pygame.display.flip()

 
     

start()

