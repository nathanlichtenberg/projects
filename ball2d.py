import pygame
import random

W = 1000
H = 800

radius = 50

x = 10
y = 10

x_vel = random.randint(5,15)
y_vel = random.randint(6,16)

pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("moving_shapes")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if y <= 0 or y >= H - 2 * radius:
        y_vel = -1 * y_vel

    if x <= 0 or x >= W - 2 * radius:
        x_vel = -1 * x_vel


    x += x_vel
    y += y_vel
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, (0,0,0), (x, y, 2 * radius, 2 * radius))
    pygame.display.update()
    clock.tick(60)
    


