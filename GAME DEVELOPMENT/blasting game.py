import pygame
import random

pygame.init()

width=1000
height=700
craftwidth=60
craftheight=80



img=pygame.image.load("space.jpg")
img=pygame.transform.scale(img,(width,height))
img2=pygame.image.load("spacecraft.png")
img2=pygame.transform.scale(img2,(craftwidth,craftheight))

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

def shoot():
    x=200
    y=620
    for i in range(y):
        pygame.draw.rect(gameboard,white,(x,y,30,30))
        y-=1


  

def spacecraft():
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
    while True:
        if shoot==False:
            bulletX = x+(craftwidth//2)-(bulletWidth//2)
        gameboard.blit(img,(0,0))
        bulletRect = pygame.draw.rect(gameboard,red,[bulletX,bulletY,bulletWidth,bulletHeight])
        spacecraft=pygame.Rect(x,y,craftwidth,craftheight)        
        gameboard.blit(img2,(x,y))
        
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
        
        

        if x<0:
            x=950

        if x>(width-craftwidth):
            x=0

        if bulletY<0:
            moveBullet=0
            bulletY=y+20
            bulletX = x+(craftwidth//2)-(bulletWidth//2)
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

def Gameover():
    font=pygame.font.SysFont(None,200)
    text=font.render("Game Over",True,red)
    font2=pygame.font.SysFont(None,50)
    text2=font2.render("If you want to repeat press SpaceBar or press q to exit",True,red)
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key==pygame.K_SPACE:
                    main()

        gameboard.blit(text,(70,100))
        gameboard.blit(text2,(100,250))
        pygame.display.flip()
    
def Lives():
    font=pygame.SysFont(None,40)
    text=font.render(f"Score:{counter}",True,red)
    #pygame.blit(text,(50,50))     

start()

