from __future__ import annotations

import os
import sys
import random
import pygame
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 780, 600
ROW = 9
COL = 9
CELL = 60
INIT_LEN = 4

def random_pos():
    return CELL*random.randint(0, ROW), CELL*random.randint(0, COL)

class Snake:
    def __init__(self):
        self.length = INIT_LEN
        self.nodes = [Head(*random_pos())]
        for _ in range(self.length-1):
            x, y = self.nodes[0].rect.topleft
            self.nodes.insert(0, Node(x-CELL, y, 1, 0, "yellow"))

        self.speed = 1

    def update(self):
        for i, node in enumerate(self.nodes):
            if type(node) is Head:
                node.update()
            else:
                node.update(self.nodes[i+1])

    def turn(self, vx, vy):
        self.head.turn(vx, vy)

    def add_node(self):
        x, y = self.nodes[0].rect.topleft
        vx, vy = self.nodes[0].vx, self.nodes[0].vy
        node = Node(x-vx*CELL, y-vy*CELL, vx, vy, "green")
        self.nodes.insert(0, node)
        self.length += 1

    def is_on_node(self): return self.head.rect in self.get_rects()[:-1]

    def right(self): self.turn(1, 0)
    def left(self): self.turn(-1, 0)
    def up(self): self.turn(0, -1)
    def down(self): self.turn(0, 1)


    @property
    def head(self):
        return self.nodes[-1]

    def get_rects(self):
        return [node.rect for node in self.nodes]


class Node:
    def __init__(self, x, y, vx, vy, color):
        self.surface = pygame.Surface((CELL, CELL), SRCALPHA)
        self.rect = pygame.Rect(x, y, CELL, CELL)
        self.vx, self.vy = vx, vy
        pygame.draw.circle(self.surface, color, (CELL/2, CELL/2), CELL/2)


    def update(self, parent_node:Node):
        if self.is_on_grid():
            self.vx = parent_node.vx
            self.vy = parent_node.vy

        self.rect.move_ip(self.vx, self.vy)

    def is_on_grid(self): return self.rect.top%CELL == 0 and self.rect.left%CELL == 0


class Head(Node):
    def __init__(self, x, y):
        super().__init__(x, y, 1, 0, "white")
        self.next_vx, self.next_vy = self.vx, self.vy

    def turn(self, vx, vy):
        self.next_vx, self.next_vy = vx, vy

    def update(self):
        if self.is_on_grid():
            self.vx = self.next_vx
            self.vy = self.next_vy
        self.rect.move_ip(self.vx, self.vy)


class Apple:
    def __init__(self, excepts):
        self.set_rect(excepts)
        self.surface = pygame.image.load("img/apple.png").convert_alpha()

    def set_rect(self, excepts):
        while True:
            self.rect = pygame.Rect(random_pos(), (CELL, CELL))
            if not self.rect in excepts:
                break

class Window:
    def __init__(self, game:Game):
        self.game = game

        self.fps = 120
        self.title = "TEST"
        pygame.display.set_caption(self.title)
        pygame.display.set_mode(SIZE)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT: self.game.snake.left()
                if event.key == K_RIGHT: self.game.snake.right()
                if event.key == K_UP: self.game.snake.up()
                if event.key == K_DOWN: self.game.snake.down()

        # pressed = pygame.key.get_pressed()
        # if pressed[K_LEFT]: self.game.snake.left()
        # if pressed[K_RIGHT]: self.game.snake.right()
        # if pressed[K_UP]: self.game.snake.up()
        # if pressed[K_DOWN]: self.game.snake.down()



    def update(self):
        self.game.update()
        self.screen.blit(self.game.surface, (0, 0))
        pygame.display.update()


    def start(self):
        self.game.start()
        while True:
            self.key_handler()
            self.update()
            self.clock.tick(self.fps)


class Game:
    def __init__(self):
        self.surface = pygame.Surface(SIZE)
        self.snake:Snake
        self.apple:Apple
        self.is_gameover = False
        self.gameover_font = pygame.font.Font(None, 120)
        self.gameover_surface = self.gameover_font.render("Game Over", False, "red", "white")
        self.gameover_rect = self.gameover_surface.get_rect()
        self.gameover_rect.center = (WIDTH/2, HEIGHT/2)

    def start(self):
        self.snake = Snake()
        self.apple = Apple(self.snake.get_rects())

    def update(self):
        if not self.is_gameover:
            self.snake.update()
        self.surface.fill((0,0,0))
        self.surface.blit(self.apple.surface, self.apple.rect)
        for node in self.snake.nodes:
            self.surface.blit(node.surface, node.rect)

        if self.is_on_apple():
            self.snake.add_node()
            self.apple.set_rect(self.snake.get_rects())

        if self.snake.head.is_on_grid():
            if self.snake.is_on_node():
                self.is_gameover = True

        if self.is_gameover:
            self.surface.blit(self.gameover_surface, self.gameover_rect)

    def is_on_apple(self):
        return self.apple.rect == self.snake.head.rect

    def show_scores(self):
        print(self.snake.length*100)

if __name__ == '__main__':
    pygame.init()
    os.chdir(os.path.dirname(__file__))
    game = Game()
    window = Window(game)
    window.start()