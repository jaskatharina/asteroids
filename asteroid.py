import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position +=  (self.velocity * dt)

    def split(self):
        self.kill()
        #small asteroid
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        #medium or large asteroid
        else:
            random_angle = random.uniform(20, 50)
            gt_vector = self.velocity.rotate(random_angle)
            lt_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = gt_vector * 1.2
            asteroid2.velocity = lt_vector * 1.2
