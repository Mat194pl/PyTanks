from enum import Enum
import pygame


class MoveDirection(Enum):
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3
    MOVE_RIGHT = 4


class TankState(Enum):
    IDLE = 1
    MOVING_UP = 2
    MOVING_DOWN = 3
    MOVING_LEFT = 4
    MOVING_RIGHT = 5


class Tank:
    def __init__(self, display, tile_size):
        self.pos_x = 0
        self.pos_y = 0
        self.tile_x = 0
        self.tile_y = 0
        self.destination_tile_x = 0
        self.destination_tile_y = 0
        self.state = TankState.IDLE
        self.move_speed = 2
        self.display = display
        self.tile_size = tile_size

    def update(self, dt):
        dx = (self.destination_tile_x - self.tile_x) * self.move_speed * dt * self.tile_size
        dy = (self.destination_tile_y - self.tile_y) * self.move_speed * dt * self.tile_size

        self.pos_x += dx
        self.pos_y += dy

        destination_pos_x = self.destination_tile_x * self.tile_size
        destination_pos_y = self.destination_tile_y * self.tile_size

        if dx > 0 and self.pos_x >= destination_pos_x:
            self.finish_movement()
        if dx < 0 and self.pos_x <= destination_pos_x:
            self.finish_movement()
        if dy > 0 and self.pos_y >= destination_pos_y:
            self.finish_movement()
        if dy < 0 and self.pos_y <= destination_pos_y:
            self.finish_movement()

    def set_tile_pos(self, tile_x, tile_y):
        self.destination_tile_x = tile_x
        self.destination_tile_y = tile_y
        self.finish_movement()

    def finish_movement(self):
        self.pos_x = self.destination_tile_x * self.tile_size
        self.pos_y = self.destination_tile_y * self.tile_size
        self.tile_x = self.destination_tile_x
        self.tile_y = self.destination_tile_y
        self.state = TankState.IDLE

    def draw(self):
        pygame.draw.rect(self.display, (255, 0, 0), (self.pos_x, self.pos_y, self.tile_size, self.tile_size))
        pass

    def move_cell_up(self):
        self.destination_tile_y -= 1
        self.state = TankState.MOVING_UP
        pass

    def move_cell_down(self):
        self.destination_tile_y += 1
        self.state = TankState.MOVING_DOWN
        pass

    def move_cell_left(self):
        self.destination_tile_x -= 1
        self.state = TankState.MOVING_LEFT
        pass

    def move_cell_right(self):
        self.destination_tile_x += 1
        self.state = TankState.MOVING_RIGHT
        pass

    def move_cell(self, direction):
        if self.state != TankState.IDLE:
            return

        possible_move_direction = {
            MoveDirection.MOVE_UP: Tank.move_cell_up,
            MoveDirection.MOVE_DOWN: Tank.move_cell_down,
            MoveDirection.MOVE_LEFT: Tank.move_cell_left,
            MoveDirection.MOVE_RIGHT: Tank.move_cell_right,
        }
        possible_move_direction.get(direction)(self)
