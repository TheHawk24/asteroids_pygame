import pygame
from constants import *


def main():
    print("Starting asteroids!")

    numpass, numfail = pygame.init()

    if not pygame.get_init():
        return

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
