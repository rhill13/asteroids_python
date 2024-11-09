import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = 10

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        sub_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid1.velocity = vec1 * 1.2
        sub_asteroid2.velocity = vec2 * 1.2

