from enum import Enum
from bullet import BulletDirection
from sprites_database import SpriteDatabase
from particlesGenerator import ParticlesGenerator
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
        self.health = 100.0

        self.bullets_manager = bullets_manager
        self.state_changed_callback = None

        self.sprites = {}
        self.sprites['moving_up_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_moving_up')
        self.sprites['moving_up_sprite'].loop = True
        self.sprites['moving_up_sprite'].play()
        self.sprites['moving_down_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_moving_down')
        self.sprites['moving_down_sprite'].loop = True
        self.sprites['moving_down_sprite'].play()
        self.sprites['moving_left_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_moving_left')
        self.sprites['moving_left_sprite'].loop = True
        self.sprites['moving_left_sprite'].play()
        self.sprites['moving_right_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_moving_right')
        self.sprites['moving_right_sprite'].loop = True
        self.sprites['moving_right_sprite'].play()
        self.sprites['up_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_up')
        self.sprites['down_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_down')
        self.sprites['left_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_left')
        self.sprites['right_sprite'] = SpriteDatabase.get_sprite('enemy_tank_1_right')
        self.sprites['gun_up'] = SpriteDatabase.get_sprite('enemy_tank_1_gun_up')
        self.sprites['gun_down'] = SpriteDatabase.get_sprite('enemy_tank_1_gun_down')
        self.sprites['gun_left'] = SpriteDatabase.get_sprite('enemy_tank_1_gun_left')
        self.sprites['gun_right'] = SpriteDatabase.get_sprite('enemy_tank_1_gun_right')

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

        for k, v in self.sprites.items():
            v.update(dt)

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
        if self.direction == TankDirection.UP:
            if self.state == TankState.IDLE:
                self.sprites['up_sprite'].draw(self.display, self.pos_x, self.pos_y)
            else:
                self.sprites['moving_up_sprite'].draw(self.display, self.pos_x, self.pos_y)
            self.sprites['gun_up'].draw(self.display, self.pos_x, self.pos_y)

        if self.direction == TankDirection.DOWN:
            if self.state == TankState.IDLE:
                self.sprites['down_sprite'].draw(self.display, self.pos_x, self.pos_y)
            else:
                self.sprites['moving_down_sprite'].draw(self.display, self.pos_x, self.pos_y)
            self.sprites['gun_down'].draw(self.display, self.pos_x, self.pos_y)

        if self.direction == TankDirection.LEFT:
            if self.state == TankState.IDLE:
                self.sprites['left_sprite'].draw(self.display, self.pos_x, self.pos_y)
            else:
                self.sprites['moving_left_sprite'].draw(self.display, self.pos_x, self.pos_y)
            self.sprites['gun_left'].draw(self.display, self.pos_x, self.pos_y)

        if self.direction == TankDirection.RIGHT:
            if self.state == TankState.IDLE:
                self.sprites['right_sprite'].draw(self.display, self.pos_x, self.pos_y)
            else:
                self.sprites['moving_right_sprite'].draw(self.display, self.pos_x, self.pos_y)
            self.sprites['gun_right'].draw(self.display, self.pos_x, self.pos_y)

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

        if self.direction == TankDirection.UP:
            ParticlesGenerator.add_gun_smoke(
                self.pos_x + (self.size_x / 2),
                self.pos_y,
                pygame.Vector2(0, -10))
            self.sprites['gun_up'].play()
        if self.direction == TankDirection.DOWN:
            ParticlesGenerator.add_gun_smoke(
                self.pos_x + (self.size_x / 2),
                self.pos_y + self.size_y,
                pygame.Vector2(0, 10))
            self.sprites['gun_down'].play()
        if self.direction == TankDirection.LEFT:
            ParticlesGenerator.add_gun_smoke(
                self.pos_x,
                self.pos_y + (self.size_y / 2),
                pygame.Vector2(-10, 0))
            self.sprites['gun_left'].play()
        if self.direction == TankDirection.RIGHT:
            ParticlesGenerator.add_gun_smoke(
                self.pos_x + self.size_x,
                self.pos_y + (self.size_y / 2),
                pygame.Vector2(10, 0))
            self.sprites['gun_right'].play()

    def register_state_change_callback(self, callback):
        self.state_changed_callback = callback

    def change_state(self, new_state):
        self.state = new_state
        if self.state_changed_callback is not None:
            self.state_changed_callback(self.state)
