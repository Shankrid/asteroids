import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    print("Starting Asteroids!")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x, y)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
             if asteroid.collision(player):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(*new_asteroids)
                    shot.kill()
        pygame.display.flip()
        clock_tick = clock.tick(60)
        dt = clock_tick / 1000
    
    

if __name__ == "__main__":
    main()