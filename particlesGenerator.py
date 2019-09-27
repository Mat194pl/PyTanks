from pygame import Vector2
from pygame import Color
import random
import pygame


class Particle:
    def __init__(self, display):
        self.velocity = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.size = 10
        self.color = Color(255, 255, 255, 10)
        self.display = display
        self.lifetime = 2
        self.init_lifetime = self.lifetime
        self.is_ready_to_remove = False
        pass

    def set_velocity(self, velocity):
        self.velocity = velocity

    def set_position(self, position):
        self.position = position

    def set_size(self, size):
        self.size = size

    def set_lifetime(self, lifetime):
        self.lifetime = lifetime
        self.init_lifetime = self.lifetime

    def update(self, dt):
        self.position += self.velocity * dt
        if self.lifetime > 0:
            self.lifetime -= dt

        if self.lifetime <= 0:
            self.is_ready_to_remove = True
        pass

    def draw(self):
        pygame.draw.circle(
            self.display,
            self.color,
            (int(self.position.x), int(self.position.y)),
            int(self.size))
        pass


class GunSmokeParticle(Particle):
    def __init__(self, display):
        super().__init__(display)
        gray_color = random.randint(200, 255)
        self.color = Color(gray_color, gray_color, gray_color, 10)

    def update(self, dt):
        super().update(dt)
        if self.velocity.length() > 0:
            self.velocity *= 0.99

class FireParticle(Particle):
    def __init__(self, display):
        super().__init__(display)
        # The color of flame should vary from white to red and yellow
        # Create 3 base colors: red, yellow and white, and them add some random to them
        #color_modifier = random.randint(0, 40)

        #rgb_modified_value = 255 - color_modifier
        #red_color = Color(rgb_modified_value, 0, 0)
        #yellow_color = Color(rgb_modified_value, rgb_modified_value, 0)
        #white_color = Color(rgb_modified_value, rgb_modified_value, rgb_modified_value)

        self.max_size = 13
        self.min_size = 5
        self.size = self.min_size
        self.color = Color(255, 255, 255)

    def update(self, dt):
        super().update(dt)
        new_size = self.size
        if self.lifetime >= 0:
            new_size = (self.max_size - self.min_size) * (1.0 - (self.lifetime / self.init_lifetime)) + self.min_size



            #if self.lifetime >= self.init_lifetime * 0.75:  # white to yellow pass
            #    new_b = self.lifetime / self.init_lifetime
            #    pass
            #elif self.lifetime >= self.init_lifetime * 0.50:
            #    pass
            #elif self.lifetime >= self.init_lifetime * 0.25:  # yellow to red pass
            #    pass
            #else:  # grey tp dark pass
            #    pass

            #new_r_color
            #new_g_color
            #new_b_color

        self.size = new_size


class ParticlesGroup:
    def __init__(self, display, pos_x, pos_y):
        self.display = display
        self.is_ready_to_remove = False
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.particles = []
        self.is_ready_to_remove = False
        pass

    def update(self, dt):
        for particle in self.particles:
            particle.update(dt)
            if particle.is_ready_to_remove:
                self.particles.remove(particle)

    def get_nmb_of_living_particles(self):
        return len(self.particles)

    def draw(self):
        for particle in self.particles:
            particle.draw()


class FireSmokeParticlesGroup(ParticlesGroup):
    def __init__(self, display, pos_x, pos_y):
        super().__init__(display, pos_x, pos_y)
        self.AVERAGE_FIRE_PARTICLE_SPEED = 10.0
        self.FIRE_PARTICLE_SPEED_DEVIATION = 2.0
        self.AVERAGE_FIRE_PARTICLE_DIRECTION = Vector2(1, -5).normalize()
        self.PARTICLE_GENERATION_RATE = 0.5
        self.next_particle_timeout = 1.0 / self.PARTICLE_GENERATION_RATE

    def update(self, dt):
        super().update(dt)
        self.next_particle_timeout -= dt
        if self.next_particle_timeout <= 0:
            self.next_particle_timeout = 1.0 / self.PARTICLE_GENERATION_RATE
            new_particle = FireParticle(self.display)
            new_particle.set_position(
                Vector2(
                    self.pos_x,
                    self.pos_y))
            new_particle.set_velocity(self.AVERAGE_FIRE_PARTICLE_DIRECTION * self.AVERAGE_FIRE_PARTICLE_SPEED)
            self.particles.append(new_particle)



class GunSmokeParticlesGroup(ParticlesGroup):
    def __init__(self, display, pos_x, pos_y, direction: Vector2):
        super().__init__(display, pos_x, pos_y)

        MIN_SIDE_PARTICLES = 5
        MAX_SIDE_PARTICLES = 10
        MIN_SMOKE_PARTICLE_SIZE = 3
        MAX_SMOKE_PARTICLE_SIZE = 10
        PARTICLE_POSITION_DEVIATION = 6
        PARTICLE_MIN_VELCOITY = 35
        PARTICLE_MAX_VELOCITY = 55
        PARTICLE_MIN_LIFE_TIME = 1.0
        PARTICLE_MAX_LIFE_TIME = 2.0

        left_vector = Vector2(direction.y, -direction.x).normalize()
        right_vector = Vector2(-left_vector.x, -left_vector.y).normalize()

        for j in range(2):
            nmb_of_particles = random.randint(MIN_SIDE_PARTICLES, MAX_SIDE_PARTICLES)
            for i in range(nmb_of_particles):
                new_particle = GunSmokeParticle(self.display)
                new_particle.set_position(
                    Vector2(
                        pos_x + random.randint(-PARTICLE_POSITION_DEVIATION, PARTICLE_POSITION_DEVIATION),
                        pos_y + random.randint(-PARTICLE_POSITION_DEVIATION, PARTICLE_POSITION_DEVIATION)))
                dir_vector = Vector2(0, 0)
                if j == 0:
                    dir_vector = left_vector
                else:
                    dir_vector = right_vector
                new_particle.set_velocity(dir_vector * random.randint(PARTICLE_MIN_VELCOITY, PARTICLE_MAX_VELOCITY))
                new_particle.set_size(random.randint(MIN_SMOKE_PARTICLE_SIZE, MAX_SMOKE_PARTICLE_SIZE))
                new_particle.set_lifetime(random.randrange(PARTICLE_MIN_LIFE_TIME, PARTICLE_MAX_LIFE_TIME))
                self.particles.append(new_particle)
        pass

    def update(self, dt):
        super().update(dt)
        if self.get_nmb_of_living_particles() <= 0:
            self.is_ready_to_remove = True


class SmokeParticlesGroup(ParticlesGroup):
    def __init__(self, display, pos_x, pos_y, duration):
        super().__init__(display, pos_x, pos_y)
        pass


class ParticlesGenerator:
    particles_groups = []

    @staticmethod
    def initialize(display):
        ParticlesGenerator.display = display
        pass

    @staticmethod
    def update(dt):
        for particle_group in ParticlesGenerator.particles_groups:
            particle_group.update(dt)
            if particle_group.is_ready_to_remove:
                ParticlesGenerator.particles_groups.remove(particle_group)
        pass

    @staticmethod
    def draw():
        for particle_group in ParticlesGenerator.particles_groups:
            particle_group.draw()

    @staticmethod
    def add_smoke(pos_x, pos_y, duration):
        new_particles_group = SmokeParticlesGroup(ParticlesGenerator.display, pos_x, pos_y, duration)
        ParticlesGenerator.particles_groups.append(new_particles_group)
        pass

    @staticmethod
    def add_gun_smoke(pos_x, pos_y, direction: Vector2):
        new_particles_group = GunSmokeParticlesGroup(ParticlesGenerator.display, pos_x, pos_y, direction)
        ParticlesGenerator.particles_groups.append(new_particles_group)
        pass

    @staticmethod
    def add_fire_smoke(pos_x, pos_y):
        new_particles_group = FireSmokeParticlesGroup(ParticlesGenerator.display, pos_x, pos_y)
        ParticlesGenerator.particles_groups.append(new_particles_group)
        pass
