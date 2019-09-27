import pygame
from enum import Enum


class BulletDirection(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Bullet:
    def __init__(self, display, tile_size, direction, pos_x, pos_y):
        self.display = display
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tile_size = tile_size
        self.direction = direction
        self.move_speed = 5
        self.size = self.tile_size / 8
        self.damage_group = 0
        self.damage_value = 20
        pass

    def update(self, dt):
        if self.direction == BulletDirection.UP:
            self.pos_y -= dt * self.move_speed
        if self.direction == BulletDirection.DOWN:
            self.pos_y += dt * self.move_speed
        if self.direction == BulletDirection.LEFT:
            self.pos_x -= dt * self.move_speed
        if self.direction == BulletDirection.RIGHT:
            self.pos_x += dt * self.move_speed

    def draw(self):
        pygame.draw.circle(
            self.display,
            (255, 0, 0),
            (int(self.pos_x + self.size / 2), int(self.pos_y + self.size / 2)),
            int(self.size))
        pass

