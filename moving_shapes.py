# -*- coding: utf-8 -*-
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("moving_shapes")
clock = pygame.time.Clock()

x = 200
y = 200
vel = 7  # Velocity

show = False

ape = pygame.transform.scale(pygame.image.load("ape.jpeg").convert_alpha(), (50, 80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                show = True
            if event.key == pygame.K_h:
                show = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if y >= 10:
            y -= vel
    if keys[pygame.K_DOWN]:
        if y <= 510:
            y += vel
    if keys[pygame.K_LEFT]:
        if x >= 10:
            x -= vel
    if keys[pygame.K_RIGHT]:
        if x <= 540:
            x += vel

    screen.fill((255, 255, 255))
    if show:
        screen.blit(ape, (x, y))
    else:
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 50, 80))
    pygame.display.update()
    clock.tick(60)
