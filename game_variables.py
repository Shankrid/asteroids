import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from game_over import *

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

def run_game(clock, screen, font, dt):
    game_status = "playing"
    print("Starting Asteroids!")
    print("Running Asteroids...")
    updatable, drawable, asteroids, shots = setup_groups()
    setup_containers(updatable, drawable, asteroids, shots)
    player_score = 0
    player_health = 1
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting Asteroids...")
                pygame.quit()
                sys.exit()
        screen.fill("black")
        score_text = font.render(f"Score: {player_score}", True, (255, 255, 255))
        health_text = font.render(f"Health: {player_health}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(health_text,(10, 100))
        updatable.update(dt)
        for item in drawable:
            item.draw(screen)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(*new_asteroids)
                    player_score += int(10 - (asteroid.radius / 10))
                    shot.kill()
        for asteroid in asteroids:
            if asteroid.collision(player) and player.invincible_timer <= 0:
                if player_health > 1:
                    player_health -= 1
                    player.invincible_timer = 1.0
                else:
                    game_status = "game_over"
        if game_status == "game_over":
            draw_game_over(screen, player_score)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                print("Restarting game...!")
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000
