import pygame
from pygame.math import Vector2
import random

W = 600
H = 700

GRID_W = 300
GRID_H = 600

#Number of blocks on bottom edge
BLOCK_COUNT_W = 10
BLOCK_COUNT_H = 20

#Width of a single square in pixels
SQUARE_WIDTH = GRID_W//BLOCK_COUNT_W

class Block:
    def __init__(self, shape, color):
        self.pos = Vector2(BLOCK_COUNT_W//2, 0)
        self.blocks = shape
        self.color = color
        
    def rotate(self):
        rotated_blocks = [block.rotate(-90) for block in self.blocks]

        if all([0 <= self.pos[0] + block[0] <= BLOCK_COUNT_W - 1 for block in rotated_blocks]):
            self.blocks = rotated_blocks

    def left(self):
        if all([self.pos[0] + block[0] > 0 for block in self.blocks]):
            self.pos[0]-= 1

    def right(self):
        if all([self.pos[0] + block[0] < BLOCK_COUNT_W - 1 for block in self.blocks]):
            self.pos[0]+= 1

    def down(self):
        if all([self.pos[1] + block[1] < BLOCK_COUNT_H - 1 for block in self.blocks]):
            self.pos[1]+= 1

    def soft_drop(self):
        self.down()

    def hard_drop(self):
        self.pos[1] = BLOCK_COUNT_H - 1
        
    def draw(self, grid):
        for block in self.blocks:
            block_pos = self.pos + block
            pygame.draw.rect(grid.surface, self.color, (SQUARE_WIDTH * block_pos[0], SQUARE_WIDTH * block_pos[1], SQUARE_WIDTH, SQUARE_WIDTH))

class Grid:
    def __init__(self):
        self.surface = pygame.Surface((GRID_W,GRID_H))
        self.surface.fill((0,0,0))
        self.grid = [[(0,0,0)] * BLOCK_COUNT_W for _ in range(BLOCK_COUNT_H)]
        
    def draw(self, screen):
        screen.blit(self.surface,(20,80))
        self.surface.fill((0,0,0))
        for i in range(BLOCK_COUNT_H):
            for j in range(BLOCK_COUNT_W):
                pygame.draw.rect(self.surface, self.grid[i][j], (SQUARE_WIDTH * i, SQUARE_WIDTH * j, SQUARE_WIDTH, SQUARE_WIDTH))
                




class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 300)

        font = pygame.font.Font("LcdSolid-VPzB.ttf", 60)
        self.title = font.render("TETRIS", False, (255,255,255))
        self.title_rect = self.title.get_rect(center = (W//2, 44))

        self.shapes = [
            [Vector2(0,0), Vector2(-1,0),Vector2(-1,-1),Vector2(-1,1)],    #Triangle shape
            [Vector2(0,0), Vector2(0,1),Vector2(0,2),Vector2(0,-1)],     #Vertical Line
            [Vector2(0,0), Vector2(-1,1),Vector2(0,1),Vector2(0,-1)],     #left L-Shape
            [Vector2(0,0), Vector2(1,1),Vector2(0,1),Vector2(0,-1)],     #right L-Shape
            [Vector2(0,0), Vector2(-1,-1),Vector2(0,-1),Vector2(1,0)],    #The "S" Shape         
        ]
        self.colors = [(255,12,114),(15,255,115),(255,142,14),(245,56,255),(255,225,56)]
        
        self.grid = Grid()
        choice = random.randint(0,4)
        self.block = Block(self.shapes[choice],self.colors[choice])
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    self.block.down()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.block.rotate()
                    if event.key == pygame.K_DOWN:
                        self.block.soft_drop()
                    if event.key == pygame.K_LEFT:
                        self.block.left()
                    if event.key == pygame.K_RIGHT:
                        self.block.right()
                    if event.key == pygame.K_SPACE:
                        self.block.hard_drop()

            self.screen.fill((160,160,160))
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
