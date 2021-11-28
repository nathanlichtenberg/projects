import pygame
import random
import math
from pygame.math import Vector2

W = 1000
H = 800

class Ball:

    def __init__(self,position,radius,color):
        self.pos = position
        self.radius = radius
        self.color = color
        self.show = True
        self.spawn_ball()

    def move(self):
        if self.pos[1] <= 0 or self.pos[1] >= H - 2 * self.radius:
            self.direction[1] = -1 * self.direction[1]

        #if self.pos[0] <= 0 or self.pos[0] >= W - 2 * self.radius:
            #self.show = False

        self.pos = self.pos + self.direction
        
        pygame.draw.ellipse(screen, self.color, (self.pos[0], self.pos[1], 2 * self.radius, 2 * self.radius))



    def spawn_ball(self):
        center = Vector2(W/2,H/2)
        angle = math.radians(random.randint(0,360))
        speed = random.randint(4,10)
        self.direction = Vector2(math.cos(angle),math.sin(angle))
        
        direction.scale_to_length(speed)
        return Ball(center,direction,30,(0,0,0))

class Paddle:
    def __init__(self,pos,width,height):
        self.rect = pygame.Rect(0,0,width,height)
        self.rect.center = pos

        
    def draw(self,surface):
        pygame.draw.rect(surface,(255,255,255),self.rect)

    def move(self,amount):
        self.rect.move_ip(0, amount)
        if self.rect.top < 10:
            self.rect.top = 10
        if self.rect.bottom > H - 10:
            self.rect.bottom = H - 10

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((W,H))
        self.clock = pygame.time.Clock()
        self.left_paddle = Paddle((35,H//2),20,130)
        self.right_paddle = Paddle((W-35,H//2),20,130)

    def draw_net(self):
        pygame.draw.rect(self.screen,(255,255,255),(W//2,25,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,75,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,125,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,175,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,225,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,275,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,325,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,375,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,425,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,475,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,525,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,575,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,625,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,675,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,725,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2,775,25,25))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            self.screen.fill((0,0,0))
            self.draw_net()
            pygame.draw.rect(self.screen,(255,255,255),(800,500,25,25))


            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_UP]:
                self.right_paddle.move(-10)
            elif keys[pygame.K_DOWN]:
                self.right_paddle.move(10)
            if keys[pygame.K_w]:
                self.left_paddle.move(-10)
            elif keys[pygame.K_s]:
                self.left_paddle.move(10)

                
            #self.left_paddle.draw(self.screen)
            #self.right_paddle.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)

def main():
    g = Game()
    g.run()


if __name__ == "__main__":
    main()
