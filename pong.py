import pygame
import random
from pygame.math import Vector2

W = 1000
H = 800

class Ball:

    def __init__(self,position,direction,radius,color):
        self.pos = position
        self.direction = direction
        self.radius = radius
        self.color = color
        self.show = True

    def move(self):
        if self.pos[1] <= 0 or self.pos[1] >= H - 2 * self.radius:
            self.direction[1] = -1 * self.direction[1]

        #if self.pos[0] <= 0 or self.pos[0] >= W - 2 * self.radius:
            #self.show = False

        self.pos = self.pos + self.direction
        
        pygame.draw.ellipse(screen, self.color, (self.pos[0], self.pos[1], 2 * self.radius, 2 * self.radius))



    def spawn_ball(self,mouse_pos,speed):
        center = Vector2(W/2,H/2)
        mouse_pos = Vector2(mouse_pos)
        direction = mouse_pos-center




        direction.scale_to_length(speed)
        return Ball(center,direction,30,(0,0,0))

class Paddle:
    def __init__(self,pos,width,height):
        self.rect = pygame.Rect(0,0,width,height)
        self.rect.center = pos



        
    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,255),self.rect)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()
        self.left_paddle = Paddle((35,H//2),20,130)
        self.right_paddle = Paddle((W-35,H//2),20,130)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen,(255,255,255),(500,500,25,25))
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)

def main():
    g = Game()
    g.run()


if __name__ == "__main__":
    main()
