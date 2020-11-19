import pygame
import random
pygame.init()

width=1000
height=500
frogwidth=50
frogheight = 70
img = pygame.image.load('mariobg.png')
white=255,255,255

gameBoard = pygame.display.set_mode((500,300))
gameBoard.fill(white)
  
def main():
    x=0
    y=0
    movex=0
    movey=0
    while True:
        gameBoard.fill(white)
        gameBoard.blit(img,(x,y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    movex = 3
            
                elif event.key == pygame.K_LEFT:
                    movex=-3
                    
            else:
                movex=0
        x+=movex
        
                    
        pygame.display.flip()
        

main()
