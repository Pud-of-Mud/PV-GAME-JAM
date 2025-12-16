import pygame
import random

from gamelogic import GameLogic
from draw import Draw
from models import Player, Zombie, Grass
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
    MIN_ZOMBIE_DISTANCE = 250

    def __init__(self):
        # Initialize Pygame and game window
        self._init_pygame()
        
        # Initialize Draw Module
        draw = Draw()
        self.draw = draw
        
        # Use Draw module for screen and background
        self.screen = self.draw.screen
        self.background = self.draw.background

        # Initialize clock, font, and message
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        
        # Initialize object lists
        self.grass = []
        self.zombies = []
        self.player = Player((400, 300))
        
    
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.player.position)
                    > self.MIN_ZOMBIE_DISTANCE
                ):
                    break

            self.zombies.append(Zombie(position, self.zombies.append))
    
    def start(self):
        self.message = "Press 'Space' to begin!"
        if pygame.key.get_pressed() == K_SPACE:
            return True

    def main_loop(self):
        while True:
            self.draw._get_game_objects(self.player, self.asteroids, [])

            self._handle_input()
            GameLogic._process_game_logic()
            self.draw._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Survival Game - Lockenbach")
    
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