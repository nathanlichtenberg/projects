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



def spawn_ball(mouse_pos,speed):
    center = Vector2(W/2,H/2)
    mouse_pos = Vector2(mouse_pos)
    direction = mouse_pos-center

    direction.scale_to_length(speed)
    return Ball(center,direction,40,(0,0,0))

    
pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("ball_bounce_spawn")
clock = pygame.time.Clock()

#ball1 = Ball(Vector2(10,10),Vector2(15,15),30,(132,255,123))
#ball2 = Ball(Vector2(390,390),Vector2(10,10),50,(71,28,182))

balls = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                balls.append(spawn_ball(pygame.mouse.get_pos(),30))

        
    screen.fill((255,255,255))
    for ball in balls:
        ball.move()
    pygame.display.update()
    clock.tick(60)
    


