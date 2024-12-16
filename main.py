import pygame
from constants import *
import player


def main():
    print("Starting asteroids!")

    pygame.init()

    if not pygame.get_init():
        return

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    triangle_player = player.Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        triangle_player.draw(screen)
        pygame.display.flip()
        time_passed = time.tick(60)
        dt = time_passed/1000


if __name__ == "__main__":
    main()
