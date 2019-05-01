from sprite import *
import copy

#enemy_tank_1_spritesheet = SpriteSheet("PyTanks.png", 6, 8)



# enemy_tank_1_animated_sprite = AnimatedSprite(enemy_tank_1_spritesheet, [0, 1, 2], [20, 20, 20])
#
# sprites_dictionary = {
#     "enemy_tank_1_up": "DD"
# }

class SpriteDatabase:
    def __init__(self, spritesheets_to_load):
        pass

    spritesheets = {}
    sprites = {}

    @staticmethod
    def initialize(spritesheets, sprites):
        for key, value in spritesheets.items():
            SpriteDatabase.spritesheets[key] = SpriteSheet(value['file'], value['frames_x'], value['frames_y'])

        for key, value in sprites.items():
            if value['sprite_type'] == 'sprite':
                SpriteDatabase.sprites[key] = Sprite()
            if value['sprite_type'] == 'animated_sprite':
                spritesheet = SpriteDatabase.spritesheets.get(value['spritesheet'])
                SpriteDatabase.sprites[key] = AnimatedSprite(spritesheet, value['frames'], value['frames_duration'])

        pass

    @staticmethod
    def get_sprite(sprite_name):
        sprite_entry = SpriteDatabase.sprites.get(sprite_name)

        new_sprite = copy.copy(sprite_entry)
        return new_sprite

