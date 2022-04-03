import pygame
from pygame.math import Vector2

W = 800
H = 800

#Width of a single square in pixels
SQUARE_WIDTH = 40
#Number of blocks on an edge
BLOCK_COUNT = W//SQUARE_WIDTH

class Snake:
    pass


class Fruit:
    def __init__(self):
        self.pos = Vector2(4, 4)

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

        self.fruit = Fruit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill((0,0,0))
            #pygame.draw.rect(self.screen, (0,179,30), (350, 350, 40, 40)
            self.fruit.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)




def main():
    g = Game()
    g.run()
    
if __name__ == "__main__":
    main()
