import pygame
from enum import Enum

class MapTileType(Enum):
    GRASS = 1,
    WATER = 2


class MapTile:
    def __init__(self, idx_x, idx_y, display):
        self.idx_x = idx_x
        self.idx_y = idx_y
        self.display = display
        self.is_solid = False
        self.is_destroyable = False
        self.SIZE_X = 50
        self.SIZE_Y = 50
        self.pos_x = idx_x * self.SIZE_X
        self.pos_y = idx_y * self.SIZE_Y
        self.type = MapTileType.GRASS

    def draw(self):
        tile_color = {
            MapTileType.GRASS: (0, 255, 0),
            MapTileType.WATER: (0, 0, 255)
        }
        pygame.draw.rect(self.display, tile_color.get(self.type), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))
        pass


class Map:
    def __init__(self, display):
        self.tiles = []
        self.width = 10
        self.height = 10
        self.display = display
        pass

    def generate(self):
        self.tiles = []
        for i in range(0, self.width):
            for j in range(0, self.height):
                self.tiles.append(MapTile(i, j, self.display))
        pass

    def generate_using_map(self, width, height, mapArr):
        self.tiles = []
        self.width = width
        self.height = height
        for i in range(0, len(mapArr)):
            pass

    def draw(self):
        for i in range(0, len(self.tiles)):
            self.tiles[i].draw()
