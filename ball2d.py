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

    def move(self):
        if self.pos[1] <= 0 or self.pos[1] >= H - 2 * self.radius:
            self.direction[1] = -1 * self.direction[1]

        if self.pos[0] <= 0 or self.pos[0] >= W - 2 * self.radius:
            self.direction[0] = -1 * self.direction[0]


        self.pos = self.pos + self.direction

        pygame.draw.ellipse(screen, self.color, (self.pos[0], self.pos[1], 2 * self.radius, 2 * self.radius))

    


pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("ball")
clock = pygame.time.Clock()

ball1 = Ball(Vector2(10,10),Vector2(20,20),30,(132,255,123))
ball2 = Ball(Vector2(390,390),Vector2(13,13),50,(71,28,182))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255,255,255))
    ball1.move()
    ball2.move()
   
    pygame.display.update()
    clock.tick(60)
    


