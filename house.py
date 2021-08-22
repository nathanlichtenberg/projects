import pygame

pygame.init() 

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Basics of Pygame')

clock = pygame.time.Clock()

window = pygame.image.load("window-removebg-preview.png").convert_alpha()
window = pygame.transform.scale(window,(45,45))

door = pygame.image.load("door-removebg-preview.png").convert_alpha()
door = pygame.transform.scale(door,(60,60))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          pygame.quit()

    screen.fill((123,123,123))

    # draw a red rectangle
    pygame.draw.rect(screen,(255,255,255),(200, 170, 100, 100))

    pygame.draw.polygon(screen, (255,0,0), [(200,170), (300,170), (250,100)])

    screen.blit(window, (200,175))

    screen.blit(door, (240,210)) 
    pygame.display.update()

    clock.tick(60)

