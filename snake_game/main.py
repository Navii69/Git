import pygame
from pygame.locals import *

def draw_block():
    surface.fill((0,0,0)) # If we dont use this line, the previous block will remain there
    surface.blit(block,(block_x,block_y))
    pygame.display.update()

if __name__ == "__main__":
    pygame.init() #Doesnt work without this line

# Game Screen
surface = pygame.display.set_mode((800,600))
surface.fill((0,0,0))

block = pygame.image.load("snake_game/resources/block.png").convert() # Block png imported
block_x = 100
block_y = 100
surface.blit(block,(block_x,block_y))

pygame.display.update()

running = True

# Game Loop
while running ==  True :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                block_y -=10
                draw_block()
            elif event.key == K_DOWN:
                block_y += 10
                draw_block()
            elif event.key == K_LEFT:
                block_x -= 10
                draw_block()
            elif event.key == K_RIGHT:
                block_x += 10
                draw_block()