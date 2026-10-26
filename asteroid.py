from turtle import position

import pygame
import random
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            log_event("asteroid_split")
            self.kill()
            angle = random.uniform(20, 50)
            first_new_asteroid_movement = self.velocity.rotate(angle)
            second_new_asteroid_movement = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = first_new_asteroid_movement * 1.2
            new_asteroid_2.velocity = second_new_asteroid_movement * 1.2
