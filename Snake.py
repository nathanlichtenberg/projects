# -*- coding: utf-8 -*-
import pygame
from pygame.math import Vector2
import random

W = 600
H = 600

# Width of a single square in pixels
SQUARE_WIDTH = 40
# Number of blocks on an edge
BLOCK_COUNT = W // SQUARE_WIDTH


class Snake:
    def __init__(self):
        self.snake_pos = [Vector2(9, 9), Vector2(9, 9), Vector2(9, 9)]
        self.tail = self.snake_pos[0]
        self.direction = Vector2()
        self.direction_modified = False

    def draw(self, screen):
        for block in self.snake_pos:
            pygame.draw.rect(screen, (77, 153, 0), (SQUARE_WIDTH * int(block[0]), SQUARE_WIDTH * int(block[1]), SQUARE_WIDTH, SQUARE_WIDTH))

    def move(self):
        self.tail = self.snake_pos[0]
        self.snake_pos = self.snake_pos[1:]
        last_block = self.snake_pos[-1]
        self.snake_pos.append(last_block + self.direction)
        self.direction_modified = False

        snake_head = self.get_head()
        if snake_head[0] < 0 or snake_head[0] >= BLOCK_COUNT:
            self.reset()
            return True
        if snake_head[1] < 0 or snake_head[1] >= BLOCK_COUNT:
            self.reset()
            return True
        if snake_head in self.snake_pos[:-1]:
            self.reset()
            return True

        return False
            
    def get_head(self):
        return self.snake_pos[-1]

    def grow(self):
        for i in range(35):
            self.snake_pos.insert(0, self.tail)

    def change_direction(self, direction):
        if not self.direction_modified:
            self.direction = direction
            self.direction_modified = True
        
    def reset(self):
        self.snake_pos = [Vector2(7, 7), Vector2(7, 7), Vector2(7, 7)]
        self.direction = Vector2()
        self.direction_modified = False

        
class Fruit:
    def __init__(self):
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        self.pos = Vector2(x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 43), (SQUARE_WIDTH * int(self.pos[0]), SQUARE_WIDTH * int(self.pos[1]), SQUARE_WIDTH, SQUARE_WIDTH))

    def reset(self):
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        self.pos = Vector2(x, y)


class Score:
    def __init__(self, font):
        self.font = font
        self.score = 0

    def draw(self, surface):
        score_text = self.font.render(str(self.score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(W // 2, 35))
        surface.blit(score_text, score_rect)

    def increase(self):
        self.score += 1

    def reset(self):
        self.score = 0


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.screen = pygame.display.set_mode((W, H))
        self.clock = pygame.time.Clock()

        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, 100)

        self.bite_sound = pygame.mixer.Sound("CHOMP.mp3")
        self.bite_sound.set_volume(1)

        self.font = pygame.font.SysFont(None, 75)
        self.score = Score(self.font)

        self.fruit = Fruit()
        self.snake = Snake()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == self.SCREEN_UPDATE:
                    if self.snake.move():
                        self.score.reset()
                    if self.snake.get_head() == self.fruit.pos:
                        self.snake.grow()
                        self.score.increase()
                        pygame.mixer.Sound.play(self.bite_sound)
                        self.fruit.reset()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != Vector2(y=1):
                        self.snake.direction = Vector2(y=-1)
                    if event.key == pygame.K_DOWN and self.snake.direction != Vector2(y=-1):
                        self.snake.direction = Vector2(y=1)
                    if event.key == pygame.K_LEFT and self.snake.direction != Vector2(1):
                        self.snake.direction = Vector2(-1)
                    if event.key == pygame.K_RIGHT and self.snake.direction != Vector2(-1):
                        self.snake.direction = Vector2(1)

            self.screen.fill((0, 0, 0))
            self.fruit.draw(self.screen)
            self.snake.draw(self.screen)
            self.score.draw(self.screen)
            pygame.display.update()
            self.clock.tick(60)


def main():
    g = Game()
    g.run()

    
if __name__ == "__main__":
    main()
