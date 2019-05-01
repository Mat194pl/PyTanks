import pygame
from map import Map
from tank import TankDirection
from bulletsManager import BulletsManager
from tankLogic import *
from sprite import *
from sprites_database import SpriteDatabase

GAME_FPS = 60

pygame.init()

display = gameDisplay = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

testMap = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 1, 1, 2, 2, 1],
    [1, 2, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 3, 1, 1],
    [1, 1, 1, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 2, 1, 1],
    [2, 1, 1, 2, 2, 2, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 1, 1],
]

spritesheets_dictionary = {
    "enemy_tank_1": {"file": "PyTanks.png", "frames_x": 6, "frames_y": 8}
}

sprites_dictionary = {
    "enemy_tank_1_up": {
        "spritesheet": "enemy_tank_1",
        "sprite_type": "animated_sprite",
        "frames": [0, 1, 2],
        "frames_duration": [0.100, 0.100, 0.100]}
}

SpriteDatabase.initialize(spritesheets_dictionary, sprites_dictionary)

gameMap = Map(display, 50)
gameMap.generate_using_map(testMap)

bullets_manager = BulletsManager(display, gameMap)

tank_group = TankGroupManager(display, gameMap, bullets_manager, 1)
#tank_group.generate_tank()
#tank_group.generate_tank()
#tank_group.generate_tank()

tank = Tank(display, 50, bullets_manager)
tank.set_tile_pos(2, 10)
tank.damage_group = 2
player_tank_logic = PlayerTankLogic(tank, gameMap)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            player_tank_logic.process_input(event)

    tank_group.update(1 / GAME_FPS)
    bullets_manager.update(1 / GAME_FPS)
    pygame.display.update()
    player_tank_logic.update(1 / GAME_FPS)
    #sprites_database.enemy_tank_1_animated_sprite.update(1 / GAME_FPS)

    # Draw things
    gameMap.draw()
    tank_group.draw()
    bullets_manager.draw()
    player_tank_logic.tank.draw()
    #sprites_database.enemy_tank_1_animated_sprite.draw()
    clock.tick(GAME_FPS)

pygame.quit()
