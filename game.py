import pygame
import random

from gamelogic import GameLogic
from draw import Draw
from models import Player, Zombie, Grass
from utils import get_positions
from  pygame import (
    QUIT, 
    KEYDOWN,
    K_ESCAPE, 
    K_SPACE, 
    K_d, 
    K_a, 
    K_w, 
    K_s
)

class Lockenbach:
    MIN_ZOMBIE_DISTANCE = 250

    def __init__(self):
        # Initialize Pygame and game window
        self._init_pygame()
        
        # Initialize Draw Module
        self.draw = Draw()
        
        # Use Draw module for screen and background
        self.screen = self.draw.screen
        #self.background = self.draw.background

        # Initialize GameLogic Module
        #self.game_logic = GameLogic()

        # Initialize clock, font, and message
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        
        # Initialize object lists
        self.grass = []
        self.zombies = []
        self.player = Player((400, 300))

        """
        for x in range(self.screen.get_width()):
            for y in range(self.screen.get_height()):
                if x % 50 == 10:
                    if y % 50 == 10:
                        self.grass.append(Grass(get_positions(x, y), pygame.time.get_ticks()))
        """
        """
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.player.position)
                    > self.MIN_ZOMBIE_DISTANCE
                ):
                    break

            self.zombies.append(Zombie(position, self.zombies.append))
        """

    def start(self):
        self.message = "Press 'Space' to begin!"
        if pygame.key.get_pressed() == K_SPACE:
            return True

    def main_loop(self):
        while True:
            self.draw._set_game_objects(self.player, [], self.grass)

            self._handle_input()
            self.player.update()
            # self.game_logic._process_game_logic()
            self.draw._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Survival Game - Lockenbach")
    
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                quit()
            elif (
                self.player
                and event.type == KEYDOWN
                and event.key == K_SPACE
            ):
                pass
                #self.spaceship.shoot()

        # Check for continuously held keys for movement
        keys = pygame.key.get_pressed()
        numKeysDown = 0

        if self.player:
            moving = False
            if keys[K_d]:
                self.player.rotate("WalkRight")
                self.player.accelerate(7)
                self.player.move(self.screen.get_size())
                moving = True
                numKeysDown += 1
            elif keys[K_a]:
                self.player.rotate("WalkLeft")
                self.player.accelerate(7)
                self.player.move(self.screen.get_size())
                moving = True
                numKeysDown += 1
            if keys[K_w]:
                self.player.rotate("Back")
                self.player.accelerate(10)
                self.player.move(self.screen.get_size())
                moving = True
                numKeysDown += 1
            elif keys[K_s]:
                self.player.rotate("Forward")
                self.player.accelerate(7)
                self.player.move(self.screen.get_size())
                moving = True
                numKeysDown += 1
            if numKeysDown > 1:
                self.player.accelerate(-5)

            if not moving:
                self.player.is_moving = 0

