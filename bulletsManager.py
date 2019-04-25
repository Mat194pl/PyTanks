import bullet


class BulletsManager:
    def __init__(self, display, map):
        self.display = display
        self.tile_size = map.tile_size
        self.bullets = []
        self.map = map

    def fire_bullet(self, pos_x, pos_y, direction: bullet.BulletDirection):
        new_bullet = bullet.Bullet(self.display, self.tile_size, direction, pos_x, pos_y)
        new_bullet.pos_x -= new_bullet.size / 2
        new_bullet.pos_y -= new_bullet.size / 2
        self.bullets.append(new_bullet)

    def update(self, dt):
        for x in self.bullets:
            x.update(dt * self.tile_size)
            if x.pos_x > self.map.width_px or x.pos_x < 0 or x.pos_y > self.map.height_px or x.pos_y < 0:
                self.bullets.remove(x)

        pass

    def draw(self):
        for x in self.bullets:
            x.draw()
        pass
