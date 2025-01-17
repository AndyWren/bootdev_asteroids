import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidable = pygame.sprite.Group()
    shootable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroidable)
    Shot.containers = (shootable, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for u in updatable:
            u.update(dt)
        for a in asteroidable:
            if a.collision(player):
                print("Game Over!")
                sys.exit()
            for s in shootable:
                if a.collision(s):
                    s.kill()
                    a.split()
        pygame.Surface.fill(screen, "black")
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()

        p = clock.tick(60)
        dt = p / 1000

if __name__ == '__main__':
    main()
