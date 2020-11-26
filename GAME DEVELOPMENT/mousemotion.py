import pygame
pygame.init()
screen = pygame.display.set_mode((800,500))
clock = pygame.time.Clock()
white = 255,255,255
from pygame.locals import *

def game():
    while True:
        screen.fill(white)
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                position=pygame.mouse.get_pos()
                print(position)

        pygame.display.flip()
        clock.tick(60)


game()
                

            
