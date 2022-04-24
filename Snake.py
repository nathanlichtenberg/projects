# -*- coding: utf-8 -*-
import pygame
from pygame.math import Vector2
import random

W = 800
H = 800

# Width of a single square in pixels
SQUARE_WIDTH = 40
# Number of blocks on an edge
BLOCK_COUNT = W // SQUARE_WIDTH


class Snake:
    def __init__(self):
        self.snake_pos = [Vector2(9, 9), Vector2(9, 9), Vector2(9, 9)]
        self.tail = self.snake_pos[0]
        self.direction = Vector2()

    def draw(self, screen):
        for block in self.snake_pos:
            pygame.draw.rect(screen, (77, 153, 0), (SQUARE_WIDTH * int(block[0]), SQUARE_WIDTH * int(block[1]), SQUARE_WIDTH, SQUARE_WIDTH))

    def move(self):
        self.tail = self.snake_pos[0]
        self.snake_pos = self.snake_pos[1:]
        last_block = self.snake_pos[-1]
        self.snake_pos.append(last_block + self.direction)

        snake_head = self.get_head()
        if snake_head[0] < 0 or snake_head[0] > 19:
            self.reset()
        if snake_head[1] < 0 or snake_head[1] > 19:
            self.reset()
            
    def get_head(self):
        return self.snake_pos[-1]

    def grow(self):
        self.snake_pos.insert(0, self.tail)
        
    def reset(self):
        self.snake_pos = [Vector2(9, 9), Vector2(9, 9), Vector2(9, 9)]
        self.tail = self.snake_pos[0]
        self.direction = Vector2()


class Fruit:
    def __init__(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        self.pos = Vector2(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 43), (SQUARE_WIDTH * int(self.pos[0]), SQUARE_WIDTH * int(self.pos[1]), SQUARE_WIDTH, SQUARE_WIDTH))

    def reset(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        self.pos = Vector2(x, y)
        

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((W, H))
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
                    if self.snake.get_head() == self.fruit.pos:
                        self.snake.grow()
                        self.fruit.reset()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Vector2(y=1):
                        self.snake.direction = Vector2(y=-1)
                    if event.key == pygame.K_DOWN and self.snake.direction != Vector2(y=-1):
                        self.snake.direction = Vector2(y=1)
                    if event.key == pygame.K_LEFT and self.snake.direction != Vector2(1):
                        self.snake.direction = Vector2(-1)
                    if event.key == pygame.K_RIGHT and self.snake.direction != Vector2(-1):
                        self.snake.direction = Vector2(1)

            self.screen.fill((0, 0, 0))
            # pygame.draw.rect(self.screen, (0,179,30), (350, 350, 40, 40)
            self.fruit.draw(self.screen)
            self.snake.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


def main():
    g = Game()
    g.run()

    
if __name__ == "__main__":
    main()
