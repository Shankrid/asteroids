import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        self.points = self.generate_asteroid_points(self.radius)

    def draw(self, screen):
        #pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        offset_points = [(self.position.x + p.x, self.position.y + p.y) for p in self.points]
        pygame.draw.polygon(screen, (255, 255, 255), offset_points, 2)

    def generate_asteroid_points(self, radius, points=12):
        result = []
        for i in range(points):
            angle = i * (360 / points)
            distance = radius * random.uniform(0.75, 1.25)
            vec = pygame.Vector2(1, 0).rotate(angle) * distance
            result.append(vec)
        return result
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
        return new_asteroid_1, new_asteroid_2

        