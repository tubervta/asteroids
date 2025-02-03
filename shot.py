import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        white = (255, 255, 255)
        ttup = (self.position.x, self.position.y)
        pygame.draw.circle(screen, white, ttup, self.radius)

    def update(self, dt):
        self.position.x += (self.velocity.x * dt)
        self.position.y += (self.velocity.y * dt)