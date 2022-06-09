# -*- coding: utf-8 -*-
import pygame
from pygame.math import Vector2
import random

W = 600
H = 600

# Width of a single square in pixels
SQUARE_WIDTH = 40
# Number of blocks on an edge
BLOCK_COUNT = W // SQUARE_WIDTH


class Fruit:
    def __init__(self):
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        self.pos = Vector2(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 43), (SQUARE_WIDTH * self.pos[0], SQUARE_WIDTH * self.pos[1], SQUARE_WIDTH, SQUARE_WIDTH))

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        self.fruit = Fruit()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    pass
                if event.type == pygame.KEYDOWN:
                    pass

            self.screen.fill((0,0,0))
            self.fruit.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


def main():
    g = Game()
    g.run()
    
if __name__ == "__main__":
    main()
