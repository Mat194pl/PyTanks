from tank import TankState
from tank import MoveDirection
from random import choices


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

            next_move = choices(tank_choices, tank_choices_wages, k=1)
            if next_move == ['stay']:
                return
            if next_move == ['go_left']:
                self.tank.move_cell(MoveDirection.MOVE_LEFT)
            if next_move == ['go_right']:
                self.tank.move_cell(MoveDirection.MOVE_RIGHT)
            if next_move == ['go_up']:
                self.tank.move_cell(MoveDirection.MOVE_UP)
            if next_move == ['go_down']:
                self.tank.move_cell(MoveDirection.MOVE_DOWN)
        self.tank.update(dt)


class TankGroupManager:
    def __init__(self):
        self.tanks_logic = []
        pass

    def generate_tank(self):
        # create tank

        # create tank_logic and connect it with a tank
        pass
    