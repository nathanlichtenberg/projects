import random
from ast import If

import pygame
from pygame.math import Vector2

W = 600
H = 700

GRID_W = 300
GRID_H = 600

# Number of blocks on bottom edge
BLOCK_COUNT_W = 10
BLOCK_COUNT_H = 20

# Width of a single square in pixels
SQUARE_WIDTH = GRID_W // BLOCK_COUNT_W


class Block:
    def __init__(self, shape, color, grid):
        self.pos = Vector2(BLOCK_COUNT_W // 2, 0)
        self.blocks = shape
        self.color = color
        self.grid = grid

    def rotate(self):
        rotated_blocks = [block.rotate(-90) for block in self.blocks]

        if all([0 <= self.pos[0] + block[0] <= BLOCK_COUNT_W - 1 for block in rotated_blocks]):
            self.blocks = rotated_blocks

    def left(self):
        if all([self.pos[0] + block[0] > 0 for block in self.blocks]):
            self.pos[0] -= 1

    def right(self):
        if all([self.pos[0] + block[0] < BLOCK_COUNT_W - 1 for block in self.blocks]):
            self.pos[0] += 1

    def down(self):
        if all([self.pos[1] + block[1] < BLOCK_COUNT_H - 1 for block in self.blocks]):
            self.pos[1] += 1
        else:
            self.grid.freeze_shape(self)

    def soft_drop(self):
        self.down()

    def hard_drop(self):
        self.pos[1] = BLOCK_COUNT_H - 1
        
    def draw(self, grid):
        for block in self.blocks:
            block_pos = self.pos + block
            pygame.draw.rect(
                grid.surface, (255, 0, 43),
                (SQUARE_WIDTH * block_pos[0], SQUARE_WIDTH * block_pos[1], SQUARE_WIDTH, SQUARE_WIDTH)
            )


class Grid:
    def __init__(self):
        self.surface = pygame.Surface((GRID_W, GRID_H))
        self.surface.fill((0, 0, 0))
        self.grid = [[(0, 0, 0)] * BLOCK_COUNT_W for _ in range(BLOCK_COUNT_H)]
        
    def draw(self, screen):
        screen.blit(self.surface, (20, 80))
        self.surface.fill((0, 0, 0))
        for i in range(BLOCK_COUNT_H):
            for j in range(BLOCK_COUNT_W):
                pygame.draw.rect(self.surface, self.grid[i][j], (SQUARE_WIDTH * i, SQUARE_WIDTH * j, SQUARE_WIDTH, SQUARE_WIDTH))
    
    def freeze_shape(self, shape):
        blocks = [shape.pos + block for block in shape.blocks]

        for x,y in blocks:
            self.grid[int(y)][int(x)] = shape.color


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 300)

        font = pygame.font.Font("LcdSolid-VPzB.ttf", 60)
        self.title = font.render("TETRIS", False, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(W // 2, 44))

        self.grid = Grid()
        choice = random.randint(0, 4)
        self.block = Block(self.shapes[choice], self.colors[choice], self.grid)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                # if event.type == self.SCREEN_UPDATE:
                    # self.block.down()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.block.soft_drop()
                    if event.key == pygame.K_LEFT:
                        self.block.left()
                    if event.key == pygame.K_RIGHT:
                        self.block.right()
                    if event.key == pygame.K_SPACE:
                        self.block.hard_drop()

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
