import pygame
import random
from pygame.math import Vector2

W = 1000
H = 800
#               Gray                     Red           Yellow           Blue
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_pos.append(pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0]:
            click_pos.append(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                click_pos = []
            if event.key == pygame.K_s:
                choice += 1
                if choice == len(colors):
                    choice = 0
                ball.color = colors[choice]
        
    screen.fill((255,255,255))
    for pos in click_pos:
         pygame.draw.ellipse(screen, colors[choice], (pos[0]-ball.radius, pos[1]-ball.radius, 2 * ball.radius, 2 * ball.radius))
    ball.move()
    pygame.display.update()
    clock.tick(100)