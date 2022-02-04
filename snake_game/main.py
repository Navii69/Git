import pygame, random , sys
from pygame.math import Vector2

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    
    def check_fail(self):
        if not 0<= self.snake.body[0].x < cell_number:
            self.game_over()
        
        elif not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)

        for row in range(cell_number):
            if row%2 == 0:
                for col in range(cell_number):
                    if col%2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen,(167,209,61), bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,(56,74,12), bg_rect,2)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x) * cell_size
            y_pos = int(block.y) * cell_size
            block_rect = pygame.Rect(x_pos, y_pos,cell_size,cell_size)
            screen.blit(block1,block_rect)
            #pygame.draw.rect(screen,(13,111,122),block_rect)
    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        
class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1 ) # x pos
        self.y = random.randint(0, cell_number - 1) # y pos
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1 ) # x pos
        self.y = random.randint(0, cell_number - 1) # y pos
        self.pos = Vector2(self.x,self.y)

if __name__ == "__main__":# __name__ = file name
    pygame.init() #Doesnt work without this line

# Game Screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))
clock = pygame.time.Clock()# helps in fps lock(so game speed is same in every pc)
apple = pygame.image.load("snake_game/resources/apple.png").convert_alpha()
block1 = pygame.image.load("snake_game/resources/block.png").convert_alpha()
game_font = pygame.font.Font("snake_game/resources/Dancing Minotaur.ttf",25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)# 150 is in milliseconds

main_game = MAIN()
# Game Loop
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y !=1:
                    main_game.snake.direction = Vector2(0,-1)
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y !=-1:
                    main_game.snake.direction = Vector2(0,1)
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x !=1:
                    main_game.snake.direction = Vector2(-1,0)
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x !=-1:
                    main_game.snake.direction = Vector2(1,0)
            
    screen.fill((pygame.Color("gold")))# Alternative pygame.color()(inside the rgb tuple) to use predefined colours
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)# limited the fps to 60 frames