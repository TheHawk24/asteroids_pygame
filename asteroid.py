import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,
                           self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(rand_angle)
        vec2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_half_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        second_half_asteroid = Asteroid(
            self.position.x, self.position.y, new_radius)
        first_half_asteroid.velocity = vec1 * 1.2
        second_half_asteroid.velocity = vec2 * 1.2
