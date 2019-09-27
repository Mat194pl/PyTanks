import bullet
from pygame.math import Vector2
from pygame import Rect


class BulletsManager:
    def __init__(self, display, game_map):
        self.display = display
        self.tile_size = game_map.tile_size
        self.bullets = []
        self.game_map = game_map
        self.tanks_groups = []
        self.is_player_dead = False

    def fire_bullet(self, pos_x, pos_y, direction: bullet.BulletDirection, damage_group):
        new_bullet = bullet.Bullet(self.display, self.tile_size, direction, pos_x, pos_y)
        new_bullet.damage_group = damage_group
        new_bullet.pos_x -= new_bullet.size / 2
        new_bullet.pos_y -= new_bullet.size / 2
        self.bullets.append(new_bullet)

    def check_tiles_collision(self, bullet_to_check):
        # Check for surrounding tiles TODO: check not only central, but also 3 additional tiles
        check_tiles = []
        center_tile_pos = Vector2(
            (int)(bullet_to_check.pos_x / self.game_map.tile_size),
            (int)(bullet_to_check.pos_y / self.game_map.tile_size))
        center_tile = self.game_map.get_tile(center_tile_pos.x, center_tile_pos.y)
        check_tiles.append(self.game_map.get_tile(center_tile_pos.x, center_tile_pos.y))
        bullet_rect = Rect(bullet_to_check.pos_x, bullet_to_check.pos_y, bullet_to_check.size, bullet_to_check.size)
        is_destroyed = False
        for tile in check_tiles:
            if bullet_rect.colliderect(
                    Rect(center_tile.pos_x, center_tile.pos_y, center_tile.SIZE_X, center_tile.SIZE_Y)):
                if not center_tile.is_bullet_passable:
                    self.bullets.remove(bullet_to_check)
                    is_destroyed = True
                    center_tile.bullet_hit_callback()
                    break
        return is_destroyed

    def check_tanks_collision(self, bullet_to_check):
        bullet_rect = Rect(bullet_to_check.pos_x, bullet_to_check.pos_y, bullet_to_check.size, bullet_to_check.size)

        for tank_group in self.tanks_groups:
            if bullet_to_check.damage_group == tank_group.damage_group:
                continue

            for tank_logic_to_check in tank_group.tanks_logic:
                tank_rect = Rect(
                    tank_logic_to_check.tank.pos_x,
                    tank_logic_to_check.tank.pos_y,
                    tank_logic_to_check.tank.size_x,
                    tank_logic_to_check.tank.size_y)

                if tank_rect.colliderect(bullet_rect):
                    tank_group.do_damage(tank_logic_to_check, bullet_to_check)
                    self.bullets.remove(bullet_to_check)
                    return True
        return False

    def check_player_collision(self, player_tank_logic):
        for x in self.bullets:
            if x.damage_group == player_tank_logic.tank.damage_group:
                continue
            bullet_rect = Rect(x.pos_x, x.pos_y, x.size, x.size)
            tank_rect = Rect(
                player_tank_logic.tank.pos_x,
                player_tank_logic.tank.pos_y,
                player_tank_logic.tank.size_x,
                player_tank_logic.tank.size_y)

            if tank_rect.colliderect(bullet_rect):
                player_tank_logic.tank.health -= x.damage_value
        pass

    def update(self, dt):
        for x in self.bullets:
            x.update(dt * self.tile_size)
            if x.pos_x > self.game_map.width_px or x.pos_x < 0 or x.pos_y > self.game_map.height_px or x.pos_y < 0:
                self.bullets.remove(x)
                continue
            else:
                # Check if bullet hits a wall or a tank
                if self.check_tiles_collision(x):
                    continue

                # Check if bullet hit a tank
                if self.check_tanks_collision(x):
                    continue

    def draw(self):
        for x in self.bullets:
            x.draw()
        pass
