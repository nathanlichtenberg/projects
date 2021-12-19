import pygame
import random
import math
import time
from pygame.math import Vector2

W = 1000
H = 800

class Ball:

    def __init__(self,position,width,color):
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], width, width)
        self.spawn_ball()
    def move(self,screen):
        if self.rect.y <= 0 or self.rect.y >= H - 2 * self.rect.width:
            self.direction[1] = -1 * self.direction[1]

        self.rect.move_ip(self.direction[0], self.direction[1])
        
        pygame.draw.rect(screen, self.color, self.rect)



    def spawn_ball(self):
        center = Vector2(W/2,H/2)
        angle = math.radians(random.choice([0,90,180,270]) + random.randint(20,60))
        speed = random.randint(8,12)
        self.direction = Vector2(math.cos(angle),-1*math.sin(angle))
        
        self.direction.scale_to_length(speed)

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
        self.ball = Ball((W//2, H//2),25,(255,255,255))

    def draw_net(self):
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,25,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,75,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,125,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,175,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,225,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,275,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,325,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,375,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,425,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,475,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,525,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,575,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,625,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,675,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,725,25,25))
        pygame.draw.rect(self.screen,(255,255,255),(W//2-12.5,775,25,25))


    def draw_menu(self):
        pygame.draw.rect(self.screen,(64,0,128),(W//2-250,H-300,500,100), border_radius = 20)
        font = pygame.font.SysFont("Arial", 60, True, False)
        text = font.render('Start Game', True, (77,255,255))
        self.screen.blit(text,(200,200,200,200))
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            self.screen.fill((0,0,0))
            self.draw_net()
            self.draw_menu()
            

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_UP]:
                self.right_paddle.move(-10)
            elif keys[pygame.K_DOWN]:
                self.right_paddle.move(10)
            if keys[pygame.K_w]:
                self.left_paddle.move(-10)
            elif keys[pygame.K_s]:
                self.left_paddle.move(10)



            if self.ball.rect.colliderect(self.left_paddle):
                if self.ball.direction[0] < 0:
                    self.ball.direction[0] *= -1

            if self.ball.rect.colliderect(self.right_paddle):
                if self.ball.direction[0] > 0:
                    self.ball.direction[0] *= -1
                
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.ball.move(self.screen)
            pygame.display.update()
            self.clock.tick(60)

def main():
    g = Game()
    g.run()


if __name__ == "__main__":
    main()
