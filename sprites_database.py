from sprite import *
import sprites_dictionaries
import copy


class SpriteDatabase:
    def __init__(self):
        pass

    spritesheets = {}
    sprites = {}
    is_initialized = False

    @staticmethod
    def initialize(spritesheets, sprites):
        for key, value in spritesheets.items():
            SpriteDatabase.spritesheets[key] = SpriteSheet(value['file'], value['frames_x'], value['frames_y'])

        for key, value in sprites.items():
            if value['sprite_type'] == 'sprite':
                spritesheet = SpriteDatabase.spritesheets.get(value['spritesheet'])
                SpriteDatabase.sprites[key] = Sprite(spritesheet, value['frame_index'], value['sprite_rotation'])
            if value['sprite_type'] == 'animated_sprite':
                spritesheet = SpriteDatabase.spritesheets.get(value['spritesheet'])
                SpriteDatabase.sprites[key] = AnimatedSprite(spritesheet, value['frames'], value['frames_duration'], value['sprite_rotation'])

        pass

    @staticmethod
    def get_sprite(sprite_name):
        # Perform lazy initialization
        if not SpriteDatabase.is_initialized:
            SpriteDatabase.initialize(
                sprites_dictionaries.spritesheets_dictionary,
                sprites_dictionaries.sprites_dictionary)
            SpriteDatabase.is_initialized = True

        sprite_entry = SpriteDatabase.sprites.get(sprite_name)

        new_sprite = copy.copy(sprite_entry)
        return new_sprite

