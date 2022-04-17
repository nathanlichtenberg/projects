import pygame
from pygame.math import Vector2

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
        self.snake_pos = self.snake_pos[1:]
        last_block = self.snake_pos[-1]
        self.snake_pos.append(last_block + self.direction)

    def reset(self):
        self.snake_pos = [Vector2(9,9), Vector2(9,9), Vector2(9,9)]
        self.direction = Vector2(0,0)
        
class Fruit:
    def __init__(self):
        self.pos = Vector2(18,18)
        

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,43), (SQUARE_WIDTH * self.pos[0], SQUARE_WIDTH * self.pos[1], SQUARE_WIDTH, SQUARE_WIDTH))

class Grid:
    pass

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        self.fruit = Fruit()
        self.snake = Snake()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    self.snake.move()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Vector2(0,1):
                        self.snake.direction = Vector2(0,-1)
                    if event.key == pygame.K_DOWN and self.snake.direction != Vector2(0,-1):
                        self.snake.direction = Vector2(0,1)
                    if event.key == pygame.K_LEFT and self.snake.direction != Vector2(1,0):
                        self.snake.direction = Vector2(-1,0)
                    if event.key == pygame.K_RIGHT and self.snake.direction != Vector2(-1,0):
                        self.snake.direction = Vector2(1,0)

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
