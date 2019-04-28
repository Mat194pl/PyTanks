import bullet
from pygame.math import Vector2
from pygame import Rect


class BulletsManager:
    def __init__(self, display, game_map):
        self.display = display
        self.tile_size = game_map.tile_size
        self.bullets = []
        self.game_map = game_map

    def fire_bullet(self, pos_x, pos_y, direction: bullet.BulletDirection):
        new_bullet = bullet.Bullet(self.display, self.tile_size, direction, pos_x, pos_y)
        new_bullet.pos_x -= new_bullet.size / 2
        new_bullet.pos_y -= new_bullet.size / 2
        self.bullets.append(new_bullet)

    def update(self, dt):
        for x in self.bullets:
            x.update(dt * self.tile_size)
            if x.pos_x > self.game_map.width_px or x.pos_x < 0 or x.pos_y > self.game_map.height_px or x.pos_y < 0:
                self.bullets.remove(x)
            else:
                # Check if bullet hits a wall or a tank
                # Check for surrounding tiles
                check_tiles = []
                center_tile_pos = Vector2(
                    (int)(x.pos_x / self.game_map.tile_size),
                    (int)(x.pos_y / self.game_map.tile_size))
                center_tile = self.game_map.get_tile(center_tile_pos.x, center_tile_pos.y)
                check_tiles.append(self.game_map.get_tile(center_tile_pos.x, center_tile_pos.y))
                bullet_rect = Rect(x.pos_x, x.pos_y, x.size, x.size)
                for tile in check_tiles:
                    if bullet_rect.colliderect(
                            Rect(center_tile.pos_x, center_tile.pos_y, center_tile.SIZE_X, center_tile.SIZE_Y)):
                        if not center_tile.is_bullet_passable:
                            self.bullets.remove(x)
                    pass
        pass

    def draw(self):
        for x in self.bullets:
            x.draw()
        pass
