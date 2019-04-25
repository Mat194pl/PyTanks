import pygame
from map import Map
from tank import Tank
from tank import MoveDirection
from tank import TankDirection
from bulletsManager import BulletsManager
from bullet import BulletDirection

GAME_FPS = 60

pygame.init()

display = gameDisplay = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

testMap = [
    [1, 1, 1, 1, 1, 1, 1, 2],
    [1, 2, 2, 1, 1, 1, 1, 2],
    [1, 2, 2, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1, 1, 1, 2]
]

gameMap = Map(display, 50)
gameMap.generate_using_map(testMap)

bullets_manager = BulletsManager(display, gameMap)
bullets_manager.fire_bullet(40, 40, BulletDirection.DOWN)

tank = Tank(display, 50, bullets_manager)
tank.set_tile_pos(5, 5)
# tank.move_cell(MoveDirection.MOVE_RIGHT)
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

    tank.update(1 / GAME_FPS)
    bullets_manager.update(1 / GAME_FPS)

    pygame.display.update()

    # Draw things
    gameMap.draw()
    tank.draw()
    bullets_manager.draw()

    clock.tick(GAME_FPS)

pygame.quit()
