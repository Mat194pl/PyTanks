import pygame
from map import Map
from tank import Tank
from tank import MoveDirection
from tank import TankDirection
from bulletsManager import BulletsManager
from bullet import BulletDirection
from tankLogic import *

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

gameMap = Map(display, 50)
gameMap.generate_using_map(testMap)

bullets_manager = BulletsManager(display, gameMap)

tank_group = TankGroupManager(display, gameMap, bullets_manager)
tank_group.generate_tank()
tank_group.generate_tank()
tank_group.generate_tank()
tank = Tank(display, 50, bullets_manager)
tank.set_tile_pos(2, 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if gameMap.is_tile_passable(tank.tile_x, tank.tile_y - 1):
                    tank.move_cell(MoveDirection.MOVE_UP)
                else:
                    tank.set_direction(TankDirection.UP)
            if event.key == pygame.K_DOWN:
                if gameMap.is_tile_passable(tank.tile_x, tank.tile_y + 1):
                    tank.move_cell(MoveDirection.MOVE_DOWN)
                else:
                    tank.set_direction(TankDirection.DOWN)
            if event.key == pygame.K_LEFT:
                if gameMap.is_tile_passable(tank.tile_x - 1, tank.tile_y):
                    tank.move_cell(MoveDirection.MOVE_LEFT)
                else:
                    tank.set_direction(TankDirection.LEFT)
            if event.key == pygame.K_RIGHT:
                if gameMap.is_tile_passable(tank.tile_x + 1, tank.tile_y):
                    tank.move_cell(MoveDirection.MOVE_RIGHT)
                else:
                    tank.set_direction(TankDirection.RIGHT)
            if event.key == pygame.K_SPACE:
                tank.fire_bullet()

    tank_group.update(1 / GAME_FPS)
    bullets_manager.update(1 / GAME_FPS)
    pygame.display.update()
    tank.update(1 / GAME_FPS)

    # Draw things
    gameMap.draw()
    tank_group.draw()
    bullets_manager.draw()
    tank.draw()
    clock.tick(GAME_FPS)

pygame.quit()
