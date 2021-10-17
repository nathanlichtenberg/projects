import pygame
import random
from pygame.math import Vector2

W = 1000
H = 800
#          Gray          Red       Yellow      Blue
colors = [(140,140,140),(255,0,0),(255,255,0),(0,0,255)]
choice = 0

class Ball:

    def __init__(self,position,radius,color):
        self.pos = position
        self.radius = radius
        self.color = color
        self.show = True

    def move(self):
        self.pos = pygame.mouse.get_pos()
        pygame.draw.ellipse(screen, self.color, (self.pos[0]-self.radius, self.pos[1]-self.radius, 2 * self.radius, 2 * self.radius))

class Point:

    def __init__(self,pos,color):
        self.pos = pos
        self.color = color

    
pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("cursorchaser")
clock = pygame.time.Clock()

ball = Ball(Vector2(10,10),15,colors[choice])
click_pos = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            point = Point(pygame.mouse.get_pos(),colors[choice])
            click_pos.append(point)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                choice += 1
                if choice == len(colors):
                    choice = 0
                ball.color = colors[choice]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                click_pos = []
    screen.fill((255,255,255))
    for point in click_pos:
        color = point.color
        pos = point.pos
        pygame.draw.ellipse(screen, color, (pos[0]-ball.radius, pos[1]-ball.radius, 2 * ball.radius, 2 * ball.radius))
    ball.move()
    pygame.display.update()
    clock.tick(100)
