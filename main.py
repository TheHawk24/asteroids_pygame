import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot


def main():
    print("Starting asteroids!")

    pygame.init()

    if not pygame.get_init():
        sys.exit("Failed to intialize pygame")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # add groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    triangle_player = Player(x, y)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for sprite in updatable:
            sprite.update(dt)
        for sprite in asteroids:
            if sprite.detect_collision(triangle_player):
                sys.exit("Game Over!")
            for bullet in shots:
                if sprite.detect_collision(bullet):
                    bullet.kill()
                    sprite.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        time_passed = time.tick(60)
        dt = time_passed/1000


if __name__ == "__main__":
    main()
