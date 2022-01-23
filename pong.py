import pygame
import random
import math
import time
from pygame.math import Vector2

W = 1000
H = 800

class Ball:

    def __init__(self,width,color):
        self.color = color
        self.width = width
        self.rect = pygame.Rect(W//2, H//2, self.width, self.width)
        self.direction = Vector2(0,0)
        self.show = False
        
    def move(self,screen):
        if self.rect.y <= 0 or self.rect.y >= H - 2 * self.rect.width:
            self.direction[1] = -1 * self.direction[1]

        self.rect.move_ip(self.direction[0], self.direction[1])

        if self.show:
            pygame.draw.rect(screen, self.color, self.rect)



    def spawn_ball(self):
        self.show = True
        self.rect = pygame.Rect(W//2, H//2, self.width, self.width)
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
        self.ball = Ball(25,(255,255,255))
        self.play_round = False
        self.start = True
        self.start_round = pygame.USEREVENT

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.start:
                        time.sleep(0.5)
                        self.play_round = True
                        self.ball.spawn_ball()
                        self.start = False

                elif event.type == self.start_round:
                    self.play_round = True
                    self.ball.spawn_ball()

                
            self.screen.fill((0,0,0))
            self.draw_net()
                
                
            if self.play_round:
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

                if self.ball.rect.x < self.ball.width * -1:
                    self.play_round = False
                    pygame.time.set_timer(self.start_round,3000)

                if self.ball.rect.x > W:
                    self.play_round = False
                    pygame.time.set_timer(self.start_round,3000)
                
                
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
