import pygame, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x) * cell_size
            y_pos = int(block.y) * cell_size
            block_rect = pygame.Rect(x_pos, y_pos,cell_size,cell_size)
            pygame.draw.rect(screen,(13,111,122),block_rect)
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1 ) # x pos
        self.y = random.randint(0, cell_number - 1) # y pos
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

if __name__ == "__main__":# __name__ = file name
    pygame.init() #Doesnt work without this line

# Game Screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))
screen.fill((pygame.Color("gold")))# Alternative pygame.color()(inside the rgb tuple) to use predefined colours
clock = pygame.time.Clock()# helps in fps lock(so game speed is same in every pc)

running = True

fruit= FRUIT()
snake= SNAKE()
# Game Loop
while running ==  True :
    fruit.draw_fruit()
    snake.draw_snake()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()
    clock.tick(60)# limited the fps to 60 frames