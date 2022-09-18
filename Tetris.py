import pygame
from pygame.math import Vector2
from random import *
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
    def __init__(self, grid):
        self.shapes = [
            [Vector2(0,0), Vector2(-1,0),Vector2(-1,-1),Vector2(-1,1)],  #Triangle shape
            [Vector2(0,0), Vector2(0,1),Vector2(0,2),Vector2(0,-1)],     #Vertical Line
            [Vector2(0,0), Vector2(-1,1),Vector2(0,1),Vector2(0,-1)],    #left L-Shape
            [Vector2(0,0), Vector2(1,1),Vector2(0,1),Vector2(0,-1)],     #right L-Shape
            [Vector2(0,0), Vector2(-1,-1),Vector2(0,-1),Vector2(1,0)],   #The "S" Shape 
            [Vector2(0,0), Vector2(0,-1),Vector2(1,-1),Vector2(1,0)],    #The Square Shape
        ]
        
        self.colors = [(255,12,114),(15,255,115),(255,142,14),(245,56,255),(255,225,56),(16,194,255)]

        self.grid = grid

        self.respawn()

    def respawn(self):
        choice = randint(0,5)
        self.pos = Vector2(BLOCK_COUNT_W//2, 0)
        self.blocks = self.shapes[choice]
        self.color = self.colors[choice]
        
    def rotate(self):
        #Don't rotate square shape
        if self.blocks == [Vector2(0,0), Vector2(0,-1),Vector2(1,-1),Vector2(1,0)]:
            return

        rotated_blocks = [block.rotate(-90) for block in self.blocks]

        if all([0 <= self.pos[0] + block[0] <= BLOCK_COUNT_W - 1 for block in rotated_blocks]):
            temp = self.blocks
            self.blocks = rotated_blocks
            if self.is_overlapping():
                self.blocks = temp

    def left(self):
        if all([self.pos[0] + block[0] > 0 for block in self.blocks]):
            self.pos[0]-= 1
            if self.is_overlapping():
                self.pos[0]+= 1

    def right(self):
        if all([self.pos[0] + block[0] < BLOCK_COUNT_W - 1 for block in self.blocks]):
            self.pos[0]+= 1
            if self.is_overlapping():
                self.pos[0]-= 1

    # returns true if block respawns otherwise returns false
    def down(self):
        self.pos[1]+= 1
        if self.is_overlapping():
            self.pos[1] -= 1
            self.grid.freeze_shape(self)
            self.respawn()
            return True
        return False

    def soft_drop(self):
        self.down()
        self.grid.score.score += 2

    def hard_drop(self):
        while True:
            if self.down():
                break
        self.grid.score.score += 10

    
    def should_be_frozen(self):
        if all([self.pos[1] + block[1] < BLOCK_COUNT_H - 1 for block in self.blocks]):
            return False
        if any([self.pos[1] + block[1] + 1 for block in self.blocks]):
            return True
        return False
    
    def is_overlapping(self):
        if not all([self.pos[1] + block[1] < BLOCK_COUNT_H for block in self.blocks]):
            return True
        for block in self.blocks:
            x,y = self.pos + block
            if self.grid.grid[int(y)][int(x)] != (0,0,0):
                return True
        return False
        
    def draw(self, grid):
        for block in self.blocks:
            block_pos = self.pos + block
            pygame.draw.rect(grid.surface, self.color, (SQUARE_WIDTH * block_pos[0], SQUARE_WIDTH * block_pos[1], SQUARE_WIDTH, SQUARE_WIDTH))

class Grid:
    def __init__(self, score):
        self.surface = pygame.Surface((GRID_W,GRID_H))
        self.surface.fill((0,0,0))
        self.grid = [[(0,0,0)] * BLOCK_COUNT_W for _ in range(BLOCK_COUNT_H)]
        self.score = score

    def draw(self, screen):
        screen.blit(self.surface,(20,80))
        self.surface.fill((0,0,0))
        for x in range(BLOCK_COUNT_W):
            for y in range(BLOCK_COUNT_H):
                pygame.draw.rect(self. surface, self.grid[y][x], (SQUARE_WIDTH * x, SQUARE_WIDTH * y, SQUARE_WIDTH, SQUARE_WIDTH))
    
    def freeze_shape(self, shape):  
        blocks = [shape.pos + block for block in shape.blocks]

        for x,y in blocks:
            if y < 0:
                exit()
            self.grid[int(y)][int(x)] = shape.color

        self.clear_rows()
        self.score.score += 20

    def clear_rows(self):
        for i in range(len(self.grid)):
            if not any([x == (0,0,0) for x in self.grid[i]]):
                self.grid.pop(i)
                self.grid.insert(0, [(0,0,0)] * BLOCK_COUNT_W)
                self.score.increase(100)

class Score:

    def __init__(self, font, pos):
        self.font = font
        self.pos = pos
        self.score = 0

    def draw(self, surface):
        score_text = self.font.render(str(self.score), True, (255,255,255))
        score_rect = score_text.get_rect(center = self.pos)
        background_rect = score_rect.copy()
        background_rect.width += 40
        background_rect.center = self.pos
        pygame.draw.rect(surface,(0,0,0),background_rect)
        surface.blit(score_text,score_rect)

    def increase(self, amount):
        self.score += amountc


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Tetris")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 200)

        title_font = pygame.font.Font("LcdSolid-VPzB.ttf", 60)
        self.title = title_font.render("TETRIS", False, (255,255,255))
        self.title_rect = self.title.get_rect(center = (W//2, 44))
        
        score_font = pygame.font.Font("score_font.ttf", 60)
        self.score = Score(score_font, (460,400))

        self.grid = Grid(self.score)
        self.block = Block(self.grid)

        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    #self.block.down()
                    pass

                keys = pygame.key.get_pressed()

                if keys[pygame.K_UP]:
                    self.block.rotate()
                elif keys[pygame.K_DOWN]:
                    print("foot")
                    self.block.soft_drop()
                if keys[pygame.K_LEFT]:
                    self.block.left()
                elif keys[pygame.K_RIGHT]:
                    self.block.right()
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_UP:
                        #self.block.rotate()
                    #if event.key == pygame.K_DOWN:
                    #     self.block.soft_drop()
                    # if event.key == pygame.K_LEFT:
                    #     self.block.left()
                    # if event.key == pygame.K_RIGHT:
                    #     self.block.right()
                    # if event.key == pygame.K_SPACE:
                    #     self.block.hard_drop()

            self.screen.fill((160,160,160))
            self.screen.blit(self.title, self.title_rect)
            self.grid.draw(self.screen)
            self.score.draw(self.screen)
            self.block.draw(self.grid)
            pygame.display.update()
            self.clock.tick(60)

def main():
    g = Game()
    g.run()
    
if __name__ == "__main__":
    main()
