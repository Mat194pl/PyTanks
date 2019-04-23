from enum import Enum

class Tank:
    class MoveDirection(Enum):
        MOVE_UP = 1,
        MOVE_DOWN = 2,
        MOVE_LEFT = 3,
        MOVE_RIGHT = 4

    class TankState(Enum):
        Idle

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0

    def draw(self):
        pass

    def move(self, dir):
        pass
