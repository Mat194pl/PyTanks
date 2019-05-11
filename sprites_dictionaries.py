spritesheets_dictionary = {
    "enemy_tank_1": {"file": "PyTanks.png", "frames_x": 6, "frames_y": 8},
    "terrain": {"file": "PyTanksTerrain.png", "frames_x": 6, "frames_y": 6}
}

sprites_dictionary = {
    "enemy_tank_1_moving_up": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [0, 1, 2],
        "frames_duration": [0.100, 0.100, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_moving_down": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [2, 1, 0],
        "frames_duration": [0.100, 0.100, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_moving_left": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [3, 4, 5],
        "frames_duration": [0.100, 0.100, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_moving_right": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [5, 4, 3],
        "frames_duration": [0.100, 0.100, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_up": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "sprite",
        "frame_index": 0,
        "sprite_rotation": 0
    },

    "enemy_tank_1_down": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "sprite",
        "frame_index": 0,
        "sprite_rotation": 0
    },

    "enemy_tank_1_left": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "sprite",
        "frame_index": 3,
        "sprite_rotation": 0
    },

    "enemy_tank_1_right": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "sprite",
        "frame_index": 3,
        "sprite_rotation": 0
    },

    "enemy_tank_1_gun_up": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [6, 7, 8, 9, 10, 11],
        "frames_duration": [0.02, 0.02, 0.02, 0.02, 0.02, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_gun_down": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [24, 25, 26, 27, 28, 29],
        "frames_duration": [0.02, 0.02, 0.02, 0.02, 0.02, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_gun_left": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [23, 22, 21, 20, 19, 18],
        "frames_duration": [0.02, 0.02, 0.02, 0.02, 0.02, 0.100],
        "sprite_rotation": 0
    },

    "enemy_tank_1_gun_right": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [12, 13, 14, 15, 16, 17],
        "frames_duration": [0.02, 0.02, 0.02, 0.02, 0.02, 0.100],
        "sprite_rotation": 0
    },

    "terrain_grass_1": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 0,
        "sprite_rotation": 0
    },

    "terrain_grass_2": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 1,
        "sprite_rotation": 0
    },

    "terrain_grass_3": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 2,
        "sprite_rotation": 0
    },

    "terrain_grass_4": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 3,
        "sprite_rotation": 0
    },

    "terrain_grass_5": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 4,
        "sprite_rotation": 0
    },

    "terrain_grass_6": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 5,
        "sprite_rotation": 0
    },

    "terrain_grass_7": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 6,
        "sprite_rotation": 0
    },

    "terrain_grass_8": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 7,
        "sprite_rotation": 0
    },

    "terrain_water_1": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 21,
        "sprite_rotation": 0
    },

    "terrain_water_2": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 22,
        "sprite_rotation": 0
    },

    "terrain_water_3": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 23,
        "sprite_rotation": 0
    },

    "terrain_asphalt": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 20,
        "sprite_rotation": 0
    },

    "terrain_road_1": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 12,
        "sprite_rotation": 0
    },

    "terrain_road_2": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 13,
        "sprite_rotation": 0
    },

    "terrain_road_3": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 14,
        "sprite_rotation": 0
    },

    "terrain_building_1": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 8,
        "sprite_rotation": 0
    },

    "terrain_building_2": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 9,
        "sprite_rotation": 0
    },

    "terrain_building_3": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 10,
        "sprite_rotation": 0
    },

    "terrain_building_4": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 15,
        "sprite_rotation": 0
    },

    "terrain_building_5": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 16,
        "sprite_rotation": 0
    },

    "terrain_building_6": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 11,
        "sprite_rotation": 0
    },

    "terrain_building_7": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 17,
        "sprite_rotation": 0
    },

    "terrain_building_8": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 18,
        "sprite_rotation": 0
    },

    "terrain_building_9": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 19,
        "sprite_rotation": 0
    },

    "tank_track_down": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 24,
        "sprite_rotation": 0
    },

    "tank_track_up": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 31,
        "sprite_rotation": 0
    },

    "tank_track_left": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 25,
        "sprite_rotation": 0
    },

    "tank_track_right": {
        "spritesheet": "terrain",
        "sprite_type": "sprite",
        "frame_index": 30,
        "sprite_rotation": 0
    }
}