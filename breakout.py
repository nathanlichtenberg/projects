import pygame
import time
from pygame.math import Vector2

W = 1000
H = 800

class Block:
    pass

class Ball:
    def __init__():
        pass

    def move(self,screen):
        pass

    def spawn_ball(self):
        pass

class Paddle:
    def __init__(self,pos,width,height):
        self.rect = pygame.Rect(0,0,width,height)
        self.rect.center = pos

    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,255),self.rect)

    def move(self,amount):
        pass

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()

        self.paddle = Paddle()
        self.ball = Ball()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.paddle.draw(self.screen)
            self.ball.move(self.screen)
            pygame.display.update()
            self.clock.tick(60)

def main():
    g = Game()
    g.run()

if __name__ == "__main__":
    main()
