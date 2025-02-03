# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")

    pygame.init()
    black = (0,0,0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroidField = AsteroidField()
    updatable.add(player)
    drawable.add(player)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill(black)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000.0
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill()
                

if __name__ == "__main__":
    main()