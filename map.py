import mapTile


class Map:
    def __init__(self, display, tile_size):
        self.tiles = []
        self.width = 10
        self.height = 10
        self.display = display
        self.tile_size = tile_size
        self.width_px = self.width * self.tile_size
        self.height_px = self.height * self.tile_size

    def generate(self):
        self.tiles = []

        for i in range(0, self.width):
            for j in range(0, self.height):
                self.tiles.append(mapTile.MapTileFactory.construct_grass_tile(i, j, self.display))
        pass

    def generate_using_map(self, map_arr):
        self.tiles = []
        x = 0
        y = 0
        width = 0
        height = 0
        for i in map_arr:
            for j in i:
                self.tiles.append(mapTile.MapTileFactory.construct_tile(j, x, y, self.display))
                x += 1
                if x > width:
                    width = x
            y += 1
            x = 0
            if y > height:
                height = y
        self.width = width
        self.height = height
        self.width_px = self.width * self.tile_size
        self.height_px = self.height * self.tile_size

    def draw(self):
        for i in range(0, len(self.tiles)):
            self.tiles[i].draw()
            self.tiles[i].draw_tank_track()

    def is_tile_passable(self, tile_x, tile_y):
        for tile in self.tiles:
            if tile.idx_x == tile_x and tile.idx_y == tile_y:
                return tile.is_passable
        return False

    def add_tank_track_to_tile(self, tile_x, tile_y, direction):
        for tile in self.tiles:
            if tile.idx_x == tile_x and tile.idx_y == tile_y:
                tile.add_tank_track(direction)

    def get_tile(self, tile_x, tile_y):
        for tile in self.tiles:
            if tile.idx_x == tile_x and tile.idx_y == tile_y:
                return tile
        return None
