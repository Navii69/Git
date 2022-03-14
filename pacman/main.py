import pygame, sys

pygame.init()

cell_size = 50
cell_number = 20

screen = pygame.display.set_mode((cell_size * cell_number , cell_size * cell_number))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()
    