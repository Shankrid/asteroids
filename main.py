import pygame
import sys
from constants import *
from game_variables import run_game
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

"""
def setup_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    return updatable, drawable, asteroids, shots

def setup_containers(updatable, drawable, asteroids, shots):
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
"""

def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)
    dt = 0

    while True:
        run_game(clock, screen, font, dt)
    
if __name__ == "__main__":
    main()