from enum import Enum
from bullet import BulletDirection
from sprites_database import SpriteDatabase
import sprites_database
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


class TankDirection(Enum):
    UP = 2
    DOWN = 3
    LEFT = 4
    RIGHT = 5


class Tank:
    def __init__(self, display, tile_size, bullets_manager):
        # Pixel position
        self.pos_x = 0
        self.pos_y = 0

        # Tile position
        self.tile_x = 0
        self.tile_y = 0

        # Destination tile position
        self.destination_tile_x = 0
        self.destination_tile_y = 0

        # Tank state
        self.state = TankState.IDLE
        self.move_speed = 2
        self.display = display
        self.size_x = tile_size
        self.size_y = tile_size

        # Tank direction
        self.direction = TankDirection.UP

        # Tank group, bullets can hit only tanks with another group
        self.damage_group = 0

        self.bullets_manager = bullets_manager
        self.state_changed_callback = None

        self.up_sprite = SpriteDatabase.get_sprite('enemy_tank_1_up')

    def update(self, dt):
        dx = (self.destination_tile_x - self.tile_x) * self.move_speed * dt * self.size_x
        dy = (self.destination_tile_y - self.tile_y) * self.move_speed * dt * self.size_y

        self.pos_x += dx
        self.pos_y += dy

        destination_pos_x = self.destination_tile_x * self.size_x
        destination_pos_y = self.destination_tile_y * self.size_y

        if dx > 0 and self.pos_x >= destination_pos_x:
            self.finish_movement()
        if dx < 0 and self.pos_x <= destination_pos_x:
            self.finish_movement()
        if dy > 0 and self.pos_y >= destination_pos_y:
            self.finish_movement()
        if dy < 0 and self.pos_y <= destination_pos_y:
            self.finish_movement()

        self.up_sprite.update(dt)

    def set_tile_pos(self, tile_x, tile_y):
        self.destination_tile_x = tile_x
        self.destination_tile_y = tile_y
        self.finish_movement()

    def finish_movement(self):
        self.pos_x = self.destination_tile_x * self.size_x
        self.pos_y = self.destination_tile_y * self.size_y
        self.tile_x = self.destination_tile_x
        self.tile_y = self.destination_tile_y
        self.change_state(TankState.IDLE)

    def draw(self):



        pygame.draw.rect(self.display, (255, 0, 0), (self.pos_x, self.pos_y, self.size_x, self.size_y))

        if self.direction == TankDirection.UP:
            pygame.draw.rect(
                self.display,
                (128, 0, 0),
                (self.pos_x + self.size_x / 2 - self.size_x / 8,
                 self.pos_y + self.size_y / 4,
                 self.size_x / 4,
                 self.size_y / 4))

        if self.direction == TankDirection.DOWN:
            pygame.draw.rect(
                self.display,
                (128, 0, 0),
                (self.pos_x + self.size_x / 2 - self.size_x / 8,
                 self.pos_y + self.size_y / 4 + self.size_y / 4,
                 self.size_x / 4,
                 self.size_y / 4))

        if self.direction == TankDirection.LEFT:
            pygame.draw.rect(
                self.display,
                (128, 0, 0),
                (self.pos_x + self.size_x / 4,
                 self.pos_y + self.size_y / 2 - self.size_y / 8,
                 self.size_x / 4,
                 self.size_y / 4))

        if self.direction == TankDirection.RIGHT:
            pygame.draw.rect(
                self.display,
                (128, 0, 0),
                (self.pos_x + self.size_x / 4 + self.size_x / 4,
                 self.pos_y + self.size_y / 2 - self.size_y / 8,
                 self.size_x / 4,
                 self.size_y / 4))

        self.up_sprite.draw(self.display, self.pos_x, self.pos_y)

    def move_cell_up(self):
        self.destination_tile_y -= 1
        self.change_state(TankState.MOVING_UP)
        self.direction = TankDirection.UP
        pass

    def move_cell_down(self):
        self.destination_tile_y += 1
        self.change_state(TankState.MOVING_DOWN)
        self.direction = TankDirection.DOWN
        pass

    def move_cell_left(self):
        self.destination_tile_x -= 1
        self.change_state(TankState.MOVING_LEFT)
        self.direction = TankDirection.LEFT
        pass

    def move_cell_right(self):
        self.destination_tile_x += 1
        self.change_state(TankState.MOVING_RIGHT)
        self.direction = TankDirection.RIGHT
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

    def set_direction(self, direction):
        self.direction = direction

    def fire_bullet(self):
        tank_dir_to_bullet_dir = {
            TankDirection.UP: BulletDirection.UP,
            TankDirection.DOWN: BulletDirection.DOWN,
            TankDirection.LEFT: BulletDirection.LEFT,
            TankDirection.RIGHT: BulletDirection.RIGHT
        }

        self.bullets_manager.fire_bullet(
            self.pos_x + (self.size_x / 2),
            self.pos_y + (self.size_y / 2),
            tank_dir_to_bullet_dir.get(self.direction),
            self.damage_group)

    def register_state_change_callback(self, callback):
        self.state_changed_callback = callback

    def change_state(self, new_state):
        self.state = new_state
        if self.state_changed_callback is not None:
            self.state_changed_callback(self.state)
