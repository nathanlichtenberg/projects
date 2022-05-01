import pygame
from pygame.math import Vector2
import random

W = 800
H = 800

#Width of a single square in pixels
SQUARE_WIDTH = 40
#Number of blocks on an edge
BLOCK_COUNT = W//SQUARE_WIDTH

class Snake:
    def __init__(self):
        self.reset()

    def draw(self, screen):
        for block in self.snake_pos:
            pygame.draw.rect(screen, (77,153,0), (SQUARE_WIDTH * block[0], SQUARE_WIDTH * block[1], SQUARE_WIDTH, SQUARE_WIDTH))

    def move(self):
        self.tail = self.snake_pos[0]
        self.snake_pos = self.snake_pos[1:]
        last_block = self.snake_pos[-1]
        self.snake_pos.append(last_block + self.direction)
        self.direction_modified = False

        snake_head = self.get_head()
        if snake_head[0] < 0 or snake_head[0] > 19:
            self.reset()
        if snake_head[1] < 0 or snake_head[1] > 19:
            self.reset()
        if snake_head in self.snake_pos[:-1]:
            self.reset()
            
    def get_head(self):
        return self.snake_pos[-1]

    def grow(self):
        self.snake_pos = [self.tail] + self.snake_pos

    def change_direction(self, direction):
        if self.direction_modified == False:
            self.direction = direction
            self.direction_modified = True
        
    def reset(self):
        self.snake_pos = [Vector2(9,9), Vector2(9,9), Vector2(9,9)]
        self.direction = Vector2(0,0)
        self.direction_modified = False
        
class Fruit:
    def __init__(self, fruit_pic):
        self.fruit_pic = fruit_pic
        self.reset()

    def draw(self, screen):
        #pygame.draw.rect(screen, (255,0,43), (SQUARE_WIDTH * self.pos[0], SQUARE_WIDTH * self.pos[1], SQUARE_WIDTH, SQUARE_WIDTH))
        screen.blit(self.fruit_pic,self.pos)
        
    def reset(self):
        x = random.randint(0,19)
        y = random.randint(0,19)
        self.pos = Vector2(x,y)
        

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        fruit_pic = pygame.image.load("fruit.png").convert_alpha()
        fruit_pic = pygame.transform.scale(fruit_pic,(SQUARE_WIDTH, SQUARE_WIDTH))

        self.fruit = Fruit(fruit_pic)
        self.snake = Snake()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    self.snake.move()
                    if self.snake.get_head() == self.fruit.pos:
                        self.snake.grow()
                        self.fruit.reset()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Vector2(0,1):
                        self.snake.change_direction(Vector2(0,-1))
                    if event.key == pygame.K_DOWN and self.snake.direction != Vector2(0,-1):
                        self.snake.change_direction(Vector2(0,1))
                    if event.key == pygame.K_LEFT and self.snake.direction != Vector2(1,0):
                        self.snake.change_direction(Vector2(-1,0))
                    if event.key == pygame.K_RIGHT and self.snake.direction != Vector2(-1,0):
                        self.snake.change_direction(Vector2(1,0))

            self.screen.fill((0,0,0))
            #pygame.draw.rect(self.screen, (0,179,30), (350, 350, 40, 40)
            self.fruit.draw(self.screen)
            self.snake.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)




def main():
    g = Game()
    g.run()
    
if __name__ == "__main__":
    main()
