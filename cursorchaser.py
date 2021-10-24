import pygame
import random
from pygame.math import Vector2

W = 1000
H = 800

class Ball:

    def __init__(self,position,velocity,radius,color):
        self.pos = position
        self.vel = velocity
        self.radius = radius
        self.color = color
        self.show = True

    def move(self):
        self.pos = pygame.mouse.get_pos()
        
        pygame.draw.ellipse(screen, self.color, (self.pos[0]-self.radius, self.pos[1]-self.radius, 2 * self.radius, 2 * self.radius))


    
pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("cursorchaser")
clock = pygame.time.Clock()

ball = Ball(Vector2(10,10),Vector2(0,0),30,(0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.fill((255,255,255))
    ball.move()
    pygame.display.update()
    clock.tick(60)
    


