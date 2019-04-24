import pygame
from map import Map
from tank import Tank
from tank import MoveDirection

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

gameMap = Map(display)
gameMap.generate_using_map(testMap)

tank = Tank(display, 50)
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
            if event.key == pygame.K_DOWN:
                if gameMap.is_tile_passable(tank.tile_x, tank.tile_y + 1):
                    tank.move_cell(MoveDirection.MOVE_DOWN)
            if event.key == pygame.K_LEFT:
                if gameMap.is_tile_passable(tank.tile_x - 1, tank.tile_y):
                    tank.move_cell(MoveDirection.MOVE_LEFT)
            if event.key == pygame.K_RIGHT:
                if gameMap.is_tile_passable(tank.tile_x + 1, tank.tile_y):
                    tank.move_cell(MoveDirection.MOVE_RIGHT)

    tank.update(1 / GAME_FPS)
    pygame.display.update()
    gameMap.draw()
    tank.draw()

    clock.tick(GAME_FPS)

pygame.quit()
