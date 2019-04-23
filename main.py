import pygame
from map import Map

GAME_TICK_PERIOD = 5

pygame.init()

display = gameDisplay = pygame.display.set_mode((800, 600))
running = True
clock = pygame.time.Clock()

gameMap = Map(display)
gameMap.generate()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    gameMap.draw()
    clock.tick(GAME_TICK_PERIOD)

pygame.quit()
