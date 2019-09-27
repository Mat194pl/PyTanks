from pygame import *
from map import Map
from tank import TankDirection
from bulletsManager import BulletsManager
from particlesGenerator import ParticlesGenerator
from tankLogic import *
from sprite import *
from sprites_database import SpriteDatabase

GAME_FPS = 60
TILE_SIZE = 50

pygame.init()

display = gameDisplay = pygame.display.set_mode((400, 550))
running = True
clock = pygame.time.Clock()

testMap = [
    [1, 1, 1, 1, 6, 1, 1, 1],
    [1, 2, 2, 1, 4, 2, 2, 1],
    [1, 2, 2, 1, 6, 7, 1, 1],
    [1, 1, 7, 1, 6, 7, 1, 1],
    [5, 5, 5, 5, 4, 7, 1, 1],
    [1, 7, 1, 1, 6, 7, 7, 1],
    [1, 1, 1, 2, 4, 5, 4, 1],
    [2, 1, 1, 2, 2, 2, 1, 1],
    [2, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 2, 2, 2, 1, 1],
]

gameMap = Map(display, TILE_SIZE)
gameMap.generate_using_map(testMap)

bullets_manager = BulletsManager(display, gameMap)

tank_group = TankGroupManager(display, gameMap, bullets_manager, 1)

for i in range(0, 6):
    tank_group.generate_tank()

tank = Tank(display, TILE_SIZE, bullets_manager)
tank.set_tile_pos(2, 10)
tank.damage_group = 2
player_tank_logic = PlayerTankLogic(tank, gameMap)

ParticlesGenerator.initialize(display)
ParticlesGenerator.add_fire_smoke(100, 100)
game_logic_running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if game_logic_running:
                player_tank_logic.process_input(event)

    GAME_DELTA = 1 / GAME_FPS

    if game_logic_running:
        player_tank_logic.update(GAME_DELTA)
    tank_group.update(GAME_DELTA)

    bullets_manager.update(GAME_DELTA)
    bullets_manager.check_player_collision(player_tank_logic)
    ParticlesGenerator.update(GAME_DELTA)
    pygame.display.update()

    # Draw things
    gameMap.draw()
    tank_group.draw()
    bullets_manager.draw()
    player_tank_logic.tank.draw()
    ParticlesGenerator.draw()

    if player_tank_logic.tank.health < 0:
        game_over_sprite = SpriteDatabase.get_sprite("game_over")
        game_over_sprite.draw(display, 50, 100)
        game_logic_running = False
        pass

    clock.tick(GAME_FPS)

pygame.quit()
