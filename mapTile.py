from enum import Enum
import pygame


class MapTileType(Enum):
    GRASS = 1
    WATER = 2

class MapTile:
    def __init__(self, idx_x, idx_y, display):
        self.idx_x = idx_x
        self.idx_y = idx_y
        self.display = display
        self.is_solid = False
        self.is_destroyable = False
        self.is_passable = False
        self.SIZE_X = 50
        self.SIZE_Y = 50
        self.pos_x = idx_x * self.SIZE_X
        self.pos_y = idx_y * self.SIZE_Y
        self.type = MapTileType.GRASS

    def draw(self):
        pass

    def update(self, dt):
        pass


class MapTileFactory:
    @staticmethod
    def construct_tile(tile_type, idx_x, idx_y, display):
        tile_types = {
            MapTileType.GRASS: MapTileFactory.construct_grass_tile,
            MapTileType.WATER: MapTileFactory.construct_water_tile
        }

        type = MapTileType(tile_type)
        type_func = tile_types.get(type)
        return type_func(idx_x, idx_y, display)

    @staticmethod
    def construct_grass_tile(idx_x, idx_y, display):
        return GrassMapTile(idx_x, idx_y, display)

    @staticmethod
    def construct_water_tile(idx_x, idx_y, display):
        return WaterMapTile(idx_x, idx_y, display)


class GrassMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = True
        pass

    def draw(self):
        pygame.draw.rect(self.display, (0, 255, 0), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))


class WaterMapTile(MapTile):
    def __init__(self,  idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = False
        pass

    def draw(self):
        pygame.draw.rect(self.display, (0, 0, 255), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))

