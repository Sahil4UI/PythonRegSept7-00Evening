import pygame
import random
pygame.init()

width=1000
height=500
frogwidth=50
frogheight = 70
img = pygame.image.load('frog.png')
img = pygame.transform.scale(img,(frogwidth,frogheight))
gameBoard=pygame.display.set_mode((width,height))

white=255,255,255
black=0,0,0
red=255,0,0
color=100,100,50
gameBoard.fill(white)
x=0
y=0
rectWidth=30
rectHeight=30
movex=0
movey=0
frogx = random.randint(0,width-frogwidth)
frogy = random.randint(0,height-frogheight)
#audio = pygame.mixer.Sound('sound.wav')
counter=0

def Score(counter):
    font = pygame.font.SysFont(None,30)
    #anti-aliasing
    text = font.render(f"Score : {counter}",True,red)
    gameBoard.blit(text,(10,10))

while True:
#   audio.play()
    gameBoard.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                movex = 3
                movey=0
            elif event.key == pygame.K_LEFT:
                movex=-3
                movey=0
            if event.key == pygame.K_UP:
                movey=-3
                movex=0
            elif event.key == pygame.K_DOWN:
                movey=3
                movex=0
       
            
    newcolor = random.randint(0,255) , random.randint(0,255) , random.randint(0,255)
    snake = pygame.draw.rect(gameBoard, black,[x,y,rectWidth,rectHeight])
    gameBoard.blit(img,(frogx,frogy))
    frog = pygame.Rect((frogx,frogy,frogwidth,frogheight))
    Score(counter)
    if snake.colliderect(frog):
        frogx = random.randint(0,width-frogwidth)
        frogy = random.randint(0,height-frogheight)
        counter+=1
        

    x+=movex
    y+=movey
    if x>width-rectWidth:
        movex=-3
    elif x<0:
        movex=3
    if y>height-rectHeight:
         movey=-3
    elif y<0:
        movey=3
   
    pygame.display.flip()
