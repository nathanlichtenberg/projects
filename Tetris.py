import pygame
from pygame.math import Vector2
import random

W = 600
H = 700

GRID_W = 300
GRID_H = 600

#Number of blocks on bottom edge
BLOCK_COUNT = 10

# Width of a single square in pixels
SQUARE_WIDTH = GRID_W // BLOCK_COUNT

class Block:
    def __init__(self):
        x = random.randint(0,BLOCK_COUNT)
        y = random.randint(0,20)
        self.pos = Vector2(x,y)

    def left(self):
        self.pos[0]-= 1

    def right(self):
        self.pos[0]+= 1
        
    def draw(self, grid):
        pygame.draw.rect(grid.surface, (255, 0, 43), (SQUARE_WIDTH * self.pos[0], SQUARE_WIDTH * self.pos[1], SQUARE_WIDTH, SQUARE_WIDTH))
        grid.surface.update()

class Grid:
    def __init__(self):
        self.surface = pygame.Surface((GRID_W, GRID_H))
        self.surface.fill((0, 0, 0))

    def draw(self, screen):
        screen.blit(self.surface, (20, 80))


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        font = pygame.font.Font("LcdSolid-VPzB.ttf", 60)
        self.title = font.render("TETRIS", False, (255, 255, 255))
        self.title_rect = self.title.get_rect(center = (W // 2, 44))

        self.grid = Grid()
        self.block = Block()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_LEFT:
                        self.block.left()
                    if event.key == pygame.K_RIGHT:
                        self.block.right()

            self.screen.fill((160, 160, 160))
            self.screen.blit(self.title, self.title_rect)
            self.grid.draw(self.screen)
            self.block.draw(self.grid)
            pygame.display.update()
            self.clock.tick(60)


def main():
    g = Game()
    g.run()
    
if __name__ == "__main__":
    main()
