# -*- coding: utf-8 -*-
import pygame
import random
import math
import time
from pygame.math import Vector2

W = 1000
H = 800


class Ball:
    def __init__(self, width, color):
        self.color = color
        self.width = width
        self.rect = pygame.Rect(W // 2, H // 2, self.width, self.width)
        self.direction = Vector2()
        self.show = False
        
    def move(self, screen):
        if self.rect.y <= 0 or self.rect.y >= H - 2 * self.rect.width:
            self.direction[1] *= -1

        self.rect.move_ip(self.direction[0], self.direction[1])

        if self.show:
            pygame.draw.rect(screen, self.color, self.rect)

    def increase_speed(self):
        speed = self.direction.length()
        speed += 0.5
        self.direction.scale_to_length(speed)

    def spawn_ball(self):
        self.show = True
        self.rect = pygame.Rect(W // 2, H // 2, self.width, self.width)
        angle = math.radians(random.choice([0, 90, 180, 270]) + random.randint(20, 60))
        speed = random.randint(8, 12)
        self.direction = Vector2(math.cos(angle), -math.sin(angle))
        self.direction.scale_to_length(speed)


class Paddle:
    def __init__(self, pos, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        
    def move(self, amount):
        self.rect.move_ip(0, amount)
        if self.rect.top < 10:
            self.rect.top = 10
        if self.rect.bottom > H - 10:
            self.rect.bottom = H - 10


class Score:
    def __init__(self, pos, font):
        self.pos = pos
        self.font = font
        self.score = 0

    def draw(self, surface):
        score_text = self.font.render(str(self.score), True, (255, 255, 255))
        surface.blit(score_text, self.pos)


class StartScreen:
    def __init__(self, font):
        self.show = True
        self.button = font.render(str("Start"), True, (0, 0, 0), (255, 255, 255))
        self.button_rect = self.button.get_rect()
        self.button_rect.center = (W // 2, H // 2)
        self.background = pygame.Surface((W, H))
        self.background.fill((0, 0, 0))
        # self.title = pygame.Surface((W - 700,H - 700))
        # self.title.fill((255, 255, 255))
            
    def draw(self, surface):
        if self.show:
            surface.blit(self.background, (0, 0))
            # surface.blit(self.title,(350, 350))
            surface.blit(self.button, self.button_rect)

    def hide(self):
        self.show = False


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Pong")
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 150)
        
        self.p1_score = Score((418, 25), self.font)
        self.p2_score = Score((550, 25), self.font)
        self.left_paddle = Paddle((35, H // 2), 20, 130)
        self.right_paddle = Paddle((W - 35, H // 2), 20, 130)
        self.ball = Ball(25, (255, 255, 255))
        self.start_screen = StartScreen(self.font)
        
        self.play_round = False
        self.start = True
        self.start_round = pygame.USEREVENT

    def draw_net(self):
        value = 25
        for _ in range(16):
            pygame.draw.rect(self.screen, (255, 255, 255), (W // 2, value, 25, 25))
            value += 50

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.start:
                        if self.start_screen.button_rect.collidepoint(event.pos):
                            self.start_screen.hide()
                            time.sleep(0.5)
                            self.play_round = True
                            self.ball.spawn_ball()
                            self.start = False

                elif event.type == self.start_round:
                    self.play_round = True
                    self.ball.spawn_ball()

            self.screen.fill((0, 0, 0))
            self.draw_net()
            
            keys = pygame.key.get_pressed()
        
            if keys[pygame.K_UP]:
                self.right_paddle.move(-104)
            elif keys[pygame.K_DOWN]:
                self.right_paddle.move(104)
            if keys[pygame.K_w]:
                self.left_paddle.move(-104)
            elif keys[pygame.K_s]:
                self.left_paddle.move(104)

            if self.play_round:
                if self.ball.rect.colliderect(self.left_paddle):
                    if self.ball.direction[0] < 0:
                        self.ball.direction[0] *= -1
                        self.ball.increase_speed()

                if self.ball.rect.colliderect(self.right_paddle):
                    if self.ball.direction[0] > 0:
                        self.ball.direction[0] *= -1
                        self.ball.increase_speed()

                if self.ball.rect.x < self.ball.width * -1:
                    self.play_round = False
                    self.p2_score.score += 1
                    if self.p2_score.score != 5:
                        pygame.time.set_timer(self.start_round, 3000, 1)

                if self.ball.rect.x > W:
                    self.play_round = False
                    self.p1_score.score += 1
                    if self.p1_score.score != 5:
                        pygame.time.set_timer(self.start_round, 3000, 1)

            self.p1_score.draw(self.screen)
            self.p2_score.draw(self.screen)
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.ball.move(self.screen)
            self.start_screen.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


def main():
    g = Game()
    g.run()


if __name__ == "__main__":
    main()
