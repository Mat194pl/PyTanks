from enum import Enum
from sprites_database import SpriteDatabase
import random
import pygame


class MapTileType(Enum):
    GRASS = 1
    WATER = 2
    WALL = 3
    ASPHALT = 4
    ROAD_HORIZONTAL = 5
    ROAD_VERTICAL = 6
    BUILDING = 7


class MapTile:
    def __init__(self, idx_x, idx_y, display):
        self.idx_x = idx_x
        self.idx_y = idx_y
        self.display = display
        self.is_solid = False
        self.is_destroyable = False
        self.is_passable = False
        self.is_bullet_passable = False
        self.SIZE_X = 50
        self.SIZE_Y = 50
        self.pos_x = idx_x * self.SIZE_X
        self.pos_y = idx_y * self.SIZE_Y
        self.type = MapTileType.GRASS
        self.is_tank_track_up = False
        self.is_tank_track_left = False
        self.is_tank_track_right = False
        self.is_tank_track_down = False
        self.tank_track_up_sprite = SpriteDatabase.get_sprite("tank_track_up")
        self.tank_track_down_sprite = SpriteDatabase.get_sprite("tank_track_down")
        self.tank_track_left_sprite = SpriteDatabase.get_sprite("tank_track_left")
        self.tank_track_right_sprite = SpriteDatabase.get_sprite("tank_track_right")

    def draw(self):
        pass

    def draw_tank_track(self):
        if self.is_tank_track_up:
            self.tank_track_up_sprite.draw(self.display, self.pos_x, self.pos_y)
        if self.is_tank_track_left:
            self.tank_track_left_sprite.draw(self.display, self.pos_x, self.pos_y)
        if self.is_tank_track_right:
            self.tank_track_right_sprite.draw(self.display, self.pos_x, self.pos_y)
        if self.is_tank_track_down:
            self.tank_track_down_sprite.draw(self.display, self.pos_x, self.pos_y)
        pass

    def update(self, dt):
        pass

    def bullet_hit_callback(self):
        pass

    def add_tank_track(self, direction):
        if direction == "up":
            self.is_tank_track_up = True
        if direction == "left":
            self.is_tank_track_left = True
        if direction == "right":
            self.is_tank_track_right = True
        if direction == "down":
            self.is_tank_track_down = True


class MapTileFactory:
    @staticmethod
    def construct_tile(tile_type, idx_x, idx_y, display):
        tile_types = {
            MapTileType.GRASS: MapTileFactory.construct_grass_tile,
            MapTileType.WATER: MapTileFactory.construct_water_tile,
            MapTileType.WALL: MapTileFactory.construct_wall_tile,
            MapTileType.ASPHALT: MapTileFactory.construct_asphalt_tile,
            MapTileType.ROAD_HORIZONTAL: MapTileFactory.construct_road_horizontal_tile,
            MapTileType.ROAD_VERTICAL: MapTileFactory.construct_road_vertical_tile,
            MapTileType.BUILDING: MapTileFactory.construct_building_tile
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

    @staticmethod
    def construct_wall_tile(idx_x, idx_y, display):
        return WallMapTile(idx_x, idx_y, display)

    @staticmethod
    def construct_asphalt_tile(idx_x, idx_y, display):
        return AsphaltMapTile(idx_x, idx_y, display)

    @staticmethod
    def construct_road_vertical_tile(idx_x, idx_y, display):
        return RoadVerticalMapTile(idx_x, idx_y, display)

    @staticmethod
    def construct_road_horizontal_tile(idx_x, idx_y, display):
        return RoadHorizontalMapTile(idx_x, idx_y, display)

    @staticmethod
    def construct_building_tile(idx_x, idx_y, display):
        return BuildingMapTile(idx_x, idx_y, display)


class GrassMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = True
        self.is_bullet_passable = True
        possible_sprites = [
            "terrain_grass_1",
            "terrain_grass_2",
            "terrain_grass_3",
            "terrain_grass_4",
            "terrain_grass_5",
            "terrain_grass_6",
            "terrain_grass_7",
            "terrain_grass_8",
        ]

        sprite_name = random.choice(possible_sprites)
        self.sprite = SpriteDatabase.get_sprite(sprite_name)
        pass

    def draw(self):
        self.sprite.draw(self.display, self.pos_x, self.pos_y)
        #pygame.draw.rect(self.display, (0, 255, 0), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))


class WaterMapTile(MapTile):
    def __init__(self,  idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = False
        self.is_bullet_passable = True

        possible_sprites = [
            "terrain_water_1",
            "terrain_water_2",
            "terrain_water_3",
        ]

        sprite_name = random.choice(possible_sprites)
        self.sprite = SpriteDatabase.get_sprite(sprite_name)
        pass

    def draw(self):
        self.sprite.draw(self.display, self.pos_x, self.pos_y)
        #pygame.draw.rect(self.display, (0, 0, 255), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))


class WallMapTile(MapTile):
    def __init__(self,  idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = False
        self.is_bullet_passable = False
        pass

    def draw(self):
        pygame.draw.rect(self.display, (128, 128, 128), (self.pos_x, self.pos_y, self.SIZE_X, self.SIZE_Y))


class AsphaltMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = True
        self.is_bullet_passable = True
        self.sprite = SpriteDatabase.get_sprite("terrain_asphalt")
        pass

    def draw(self):
        self.sprite.draw(self.display, self.pos_x, self.pos_y)


class RoadHorizontalMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = True
        self.is_bullet_passable = True

        possible_sprites = [
            "terrain_road_1",
            "terrain_road_2",
            "terrain_road_3",
        ]
        sprite_name = random.choice(possible_sprites)
        self.sprite = SpriteDatabase.get_sprite(sprite_name)
        self.sprite.sprite_rotation = 90
        pass

    def draw(self):
        self.sprite.draw(self.display, self.pos_x, self.pos_y)


class RoadVerticalMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = True
        self.is_bullet_passable = True

        possible_sprites = [
            "terrain_road_1",
            "terrain_road_2",
            "terrain_road_3",
        ]
        sprite_name = random.choice(possible_sprites)
        self.sprite = SpriteDatabase.get_sprite(sprite_name)
        pass

    def draw(self):
        self.sprite.draw(self.display, self.pos_x, self.pos_y)


class BuildingMapTile(MapTile):
    def __init__(self, idx_x, idx_y, display):
        super().__init__(idx_x, idx_y, display)
        self.is_passable = False
        self.is_bullet_passable = False
        self.sprites = []
        possible_sprites_group = [
            ["terrain_building_1", "terrain_building_2", "terrain_building_3"],
            ["terrain_building_4", "terrain_building_5", "terrain_building_6"],
            ["terrain_building_7", "terrain_building_8", "terrain_building_9"],
        ]
        sprites_group = random.choice(possible_sprites_group)
        for sprite_name in sprites_group:
            self.sprites.append(SpriteDatabase.get_sprite(sprite_name))

        self.sprite_idx = 0
        pass

    def bullet_hit_callback(self):
        if self.sprite_idx < 2:
            self.sprite_idx += 1
            if self.sprite_idx == 2:
                self.is_passable = True
                self.is_bullet_passable = True

    def draw(self):
        self.sprites[self.sprite_idx].draw(self.display, self.pos_x, self.pos_y)
