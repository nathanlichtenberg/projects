import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), (200,200,50,80))
    pygame.display.update()
    clock.tick(60)


