import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Screen setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # delta time
    clock = pygame.time.Clock()
    dt = 0

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # player
    Player.containers = (updatable, drawable)
    player_init_x = SCREEN_WIDTH / 2
    player_init_y = SCREEN_HEIGHT / 2
    player = Player(player_init_x, player_init_y)

    Shot.containers = (updatable, drawable, shots)

    
    # GAME LOOP
    while True:

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # background
        screen.fill(pygame.Color("black"))

        # process groups
        for sprite in updatable:
            sprite.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        
        # check asteroids for collisions with player
        for asteroid_sprite in asteroids:
            if asteroid_sprite.is_colliding(player):
                print("Game over!")
                sys.exit()
 
        # check for shot collisions with asteroids
        for asteroid_sprite in asteroids:
            for shot_sprite in shots:
                if shot_sprite.is_colliding(asteroid_sprite):
                    shot_sprite.kill()
                    asteroid_sprite.split()

        # refresh screen
        pygame.display.flip()

        # 60 fps
        time_passed = clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()
