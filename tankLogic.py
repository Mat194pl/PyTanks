from tank import TankState
from tank import MoveDirection
from random import choices
from random import choice
from tank import Tank


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
                self.tank.move_cell(MoveDirection.MOVE_LEFT)
            if next_move == ['go_right']:
                self.tank.move_cell(MoveDirection.MOVE_RIGHT)
            if next_move == ['go_up']:
                self.tank.move_cell(MoveDirection.MOVE_UP)
            if next_move == ['go_down']:
                self.tank.move_cell(MoveDirection.MOVE_DOWN)
        self.tank.update(dt)


class EnemyTankLogic(TankLogic):
    def __init__(self, tank, game_map):
        super().__init__(tank, game_map)
        self.next_shot_timeout = 0

    def update(self, dt):
        super().update(dt)

        # Add shooting
        self.next_shot_timeout -= dt
        if self.next_shot_timeout < 0:
            self.next_shot_timeout = choice([2, 3, 4, 5, 6])
            self.tank.fire_bullet()


class TankGroupManager:
    def __init__(self, display, game_map, bullets_manager):
        self.tanks_logic = []
        self.display = display
        self.game_map = game_map
        self.bullets_manager = bullets_manager
        pass

    def generate_tank(self):
        # create tank
        new_tank = Tank(self.display, self.game_map.tile_size, self.bullets_manager)
        # create tank_logic and connect it with a tank
        self.tanks_logic.append(EnemyTankLogic(new_tank, self.game_map))
        pass

    def update(self, dt):
        for x in self.tanks_logic:
            x.update(dt)

    def draw(self):
        for x in self.tanks_logic:
            x.tank.draw()
