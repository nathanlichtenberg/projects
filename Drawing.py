import pygame
import random
from pygame.math import Vector2

W = 1000
H = 800

RADIUS = 15
#          Gray          Red       Yellow      Blue
colors = [(140,140,140),(255,0,0),(255,255,0),(0,0,255)]

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

class Button:

    def __init__(self,x,y,width,height,screen,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.screen = screen
        self.color = color
        
    def paint(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("cursorchaser")
clock = pygame.time.Clock()

ball = Ball(Vector2(10,10),RADIUS,colors[0])
click_pos = []
button_gray = Button(W-50,0,50,50,screen,colors[0])
button_red = Button(W-50,50,50,50,screen,colors[1])
button_yellow = Button(W-50,100,50,50,screen,colors[2])
button_blue = Button(W-50,150,50,50,screen,colors[3])
buttons = [button_gray, button_red, button_yellow, button_blue]

trash_icon = pygame.image.load("trash_icon.jpeg").convert_alpha()
trash_icon = pygame.transform.scale(trash_icon,(80,80))
trash_rect = trash_icon.get_rect(bottomright = (W,H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            point = Point(pygame.mouse.get_pos(),ball.color)
            click_pos.append(point)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        ball.color = button.color
                if trash_rect.collidepoint(event.pos):
                    click_pos = []
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos.append(None)
    screen.fill((255,255,255))
    for point_index in range(len(click_pos)):
        if click_pos[point_index] is None:
            continue
        point = click_pos[point_index]
        color = point.color
        pos = point.pos
        pygame.draw.ellipse(screen, color, (pos[0]-ball.radius, pos[1]-ball.radius, 2 * ball.radius, 2 * ball.radius))
        if point_index >= 1 and click_pos[point_index - 1] is not None and click_pos[point_index] is not None:
            pygame.draw.line(screen, color, pos, click_pos[point_index - 1].pos, (2 * ball.radius) + 6)
    for button in buttons:
        button.paint()
    screen.blit(trash_icon,trash_rect)
    ball.move()
    pygame.display.update()
    clock.tick(100)