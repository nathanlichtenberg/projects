import pygame

W = 600
H = 800

radius = 50

y = H - 2 * radius
up = True

pygame.init()
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("moving_shapes")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if y <= 0:
        up = False
    if y >= H - 2 * radius:

        up = True

    if up:
        y -= 6
    else:
        y += 6

    
    screen.fill((255,255,255))
    pygame.draw.ellipse(screen, (0,0,0), (W/2 - radius, y, 2 * radius, 2 * radius))
    pygame.display.update()
    clock.tick(60)

    


