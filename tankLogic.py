from random import choices
from random import choice
from tank import *
import pygame


class TankLogic:
    def __init__(self, tank, game_map):
        self.tank = tank
        self.game_map = game_map

    def update(self, dt):
        if self.tank.state == TankState.IDLE:
            tank_choices = ['stay']
            if self.game_map.is_tile_passable(self.tank.tile_x - 1, self.tank.tile_y):
                tank_choices.append('go_left')
            if self.game_map.is_tile_passable(self.tank.tile_x + 1, self.tank.tile_y):
                tank_choices.append('go_right')
            if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y - 1):
                tank_choices.append('go_up')
            if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y + 1):
                tank_choices.append('go_down')

            tank_choices_wages = ([80] + ([3] * (len(tank_choices) - 1)))

            # Boost last direction

            next_move = choices(tank_choices, tank_choices_wages, k=1)
            if next_move == ['stay']:
                return
            if next_move == ['go_left']:
                #self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "left")
                self.tank.move_cell(MoveDirection.MOVE_LEFT)
            if next_move == ['go_right']:
                #self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "right")
                self.tank.move_cell(MoveDirection.MOVE_RIGHT)
            if next_move == ['go_up']:
                #self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "up")
                self.tank.move_cell(MoveDirection.MOVE_UP)
            if next_move == ['go_down']:
                #self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "down")
                self.tank.move_cell(MoveDirection.MOVE_DOWN)
        self.tank.update(dt)


class EnemyTankLogic(TankLogic):
    def __init__(self, tank, game_map):
        super().__init__(tank, game_map)
        self.next_shot_timeout = 0
        tank.register_state_change_callback(self.tank_state_changed)

    def update(self, dt):
        super().update(dt)

        # Add shooting
        self.next_shot_timeout -= dt
        if self.next_shot_timeout < 0:
            self.next_shot_timeout = choice([2, 3, 4, 5, 6])
            self.tank.fire_bullet()

    def tank_state_changed(self, tank_state):
        if tank_state == TankState.IDLE:
            if self.tank.direction == TankDirection.UP:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "down")
            if self.tank.direction == TankDirection.DOWN:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "up")
            if self.tank.direction == TankDirection.RIGHT:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "left")
            if self.tank.direction == TankDirection.LEFT:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "right")

        if tank_state == TankState.MOVING_UP:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "up")
        if tank_state == TankState.MOVING_LEFT:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "left")
        if tank_state == TankState.MOVING_RIGHT:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "right")
        if tank_state == TankState.MOVING_DOWN:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "down")


class PlayerTankLogic(TankLogic):
    def __init__(self, tank, game_map):
        super().__init__(tank, game_map)
        self.is_key_up_hold = False
        self.is_key_down_hold = False
        self.is_key_left_hold = False
        self.is_key_right_hold = False
        tank.health = 1
        tank.register_state_change_callback(self.tank_state_changed)
        pass

    def update(self, dt):
        self.tank.update(dt)
        pass

    def tank_state_changed(self, tank_state):
        if tank_state == TankState.IDLE:
            if self.tank.direction == TankDirection.UP:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "down")
            if self.tank.direction == TankDirection.DOWN:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "up")
            if self.tank.direction == TankDirection.RIGHT:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "left")
            if self.tank.direction == TankDirection.LEFT:
                self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "right")

            if self.is_key_up_hold:
                if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y - 1):
                    self.tank.move_cell(MoveDirection.MOVE_UP)
            if self.is_key_down_hold:
                if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y + 1):
                    self.tank.move_cell(MoveDirection.MOVE_DOWN)
            if self.is_key_left_hold:
                if self.game_map.is_tile_passable(self.tank.tile_x - 1, self.tank.tile_y):
                    self.tank.move_cell(MoveDirection.MOVE_LEFT)
            if self.is_key_right_hold:
                if self.game_map.is_tile_passable(self.tank.tile_x + 1, self.tank.tile_y):
                    self.tank.move_cell(MoveDirection.MOVE_RIGHT)

        if tank_state == TankState.MOVING_UP:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "up")
        if tank_state == TankState.MOVING_LEFT:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "left")
        if tank_state == TankState.MOVING_RIGHT:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "right")
        if tank_state == TankState.MOVING_DOWN:
            self.game_map.add_tank_track_to_tile(self.tank.tile_x, self.tank.tile_y, "down")

    def process_input(self, input_event):
        if input_event.key == pygame.K_DOWN:
            if input_event.type == pygame.KEYDOWN:
                self.set_key_hold(pygame.K_DOWN)
                if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y + 1):
                    self.tank.move_cell(MoveDirection.MOVE_DOWN)
                else:
                    self.tank.set_direction(TankDirection.DOWN)
            else:
                self.is_key_down_hold = False

        if input_event.key == pygame.K_UP:
            if input_event.type == pygame.KEYDOWN:
                self.set_key_hold(pygame.K_UP)
                if self.game_map.is_tile_passable(self.tank.tile_x, self.tank.tile_y - 1):
                    self.tank.move_cell(MoveDirection.MOVE_UP)
                else:
                    self.tank.set_direction(TankDirection.UP)
            else:
                self.is_key_up_hold = False

        if input_event.key == pygame.K_LEFT:
            if input_event.type == pygame.KEYDOWN:
                self.set_key_hold(pygame.K_LEFT)
                if self.game_map.is_tile_passable(self.tank.tile_x - 1, self.tank.tile_y):
                    self.tank.move_cell(MoveDirection.MOVE_LEFT)
                else:
                    self.tank.set_direction(TankDirection.LEFT)
            else:
                self.is_key_left_hold = False

        if input_event.key == pygame.K_RIGHT:
            if input_event.type == pygame.KEYDOWN:
                self.set_key_hold(pygame.K_RIGHT)
                if self.game_map.is_tile_passable(self.tank.tile_x + 1, self.tank.tile_y):
                    self.tank.move_cell(MoveDirection.MOVE_RIGHT)
                else:
                    self.tank.set_direction(TankDirection.RIGHT)
            else:
                self.is_key_right_hold = False

        if input_event.key == pygame.K_SPACE and input_event.type == pygame.KEYDOWN:
            self.tank.fire_bullet()

    def set_key_hold(self, key):
        self.is_key_up_hold = False
        self.is_key_down_hold = False
        self.is_key_left_hold = False
        self.is_key_right_hold = False

        if key == pygame.K_UP:
            self.is_key_up_hold = True
        if key == pygame.K_DOWN:
            self.is_key_down_hold = True
        if key == pygame.K_LEFT:
            self.is_key_left_hold = True
        if key == pygame.K_RIGHT:
            self.is_key_right_hold = True


class TankGroupManager:
    def __init__(self, display, game_map, bullets_manager, damage_group):
        self.tanks_logic = []
        self.display = display
        self.game_map = game_map
        self.bullets_manager = bullets_manager
        self.damage_group = damage_group
        self.bullets_manager.tanks_groups.append(self)
        pass

    def generate_tank(self):
        # create tank
        new_tank = Tank(self.display, self.game_map.tile_size, self.bullets_manager)
        new_tank.damage_group = self.damage_group
        # create tank_logic and connect it with a tank
        self.tanks_logic.append(EnemyTankLogic(new_tank, self.game_map))
        pass

    def update(self, dt):
        for x in self.tanks_logic:
            x.update(dt)

    def draw(self):
        for x in self.tanks_logic:
            x.tank.draw()

    def do_damage(self, tank_logic, bullet):
        tank_logic.tank.health -= bullet.damage_value
        if tank_logic.tank.health < 0.0:
            # Remove tank
            self.tanks_logic.remove(tank_logic)
        pass
