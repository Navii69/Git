import pygame, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1 ) # x pos
        self.y = random.randint(0, cell_number - 1) # y pos
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

def draw_block():
    screen.fill((pygame.Color("gold"))) # If we dont use this line, the previous block will remain there
    screen.blit(block,(block_x,block_y))
    pygame.display.update()

if __name__ == "__main__":# __name__ = file name
    pygame.init() #Doesnt work without this line

# Game Screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))
screen.fill((pygame.Color("gold")))# Alternative pygame.color()(inside the rgb tuple) to use predefined colours
clock = pygame.time.Clock()# helps in fps lock(so game speed is same in every pc)

block = pygame.image.load("snake_game/resources/block.png").convert() # Block png imported
block_x = 100
block_y = 100
screen.blit(block,(block_x,block_y))

running = True

fruit= FRUIT()
# Game Loop
while running ==  True :
    fruit.draw_fruit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block_y -=10
                draw_block()
            elif event.key == pygame.K_DOWN:
                block_y += 10
                draw_block()
            elif event.key == pygame.K_LEFT:
                block_x -= 10
                draw_block()
            elif event.key == pygame.K_RIGHT:
                block_x += 10
                draw_block()
    
    pygame.display.update()
    clock.tick(60)# limited the fps to 60 frames