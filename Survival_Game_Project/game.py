import pygame
import random

from models import Player
from utils import load_sprite, get_random_position, text_to_screen
from  pygame import (
    QUIT, 
    KEYDOWN,
    K_ESCAPE, 
    K_SPACE, 
    K_RIGHT, 
    K_LEFT, 
    K_UP, 
    K_DOWN
)

class Lockenbach:
    MIN_ASTEROID_DISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        
    
        self.asteroids = []
        self.bullets = []
        self.player = Player((400, 300), self.bullets.append)
        
    
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append))
    def start(self):
        self.message = "Press 'Space' to begin!"
        if pygame.key.get_pressed() == K_SPACE:
            return True

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)
        
        return game_objects
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                quit()
            elif (
                self.spaceship
                and event.type == KEYDOWN
                and event.key == K_SPACE
            ):
                self.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[K_UP]:
                self.spaceship.accelerate()
            elif is_key_pressed[K_DOWN]:
                self.spaceship.decelerate()