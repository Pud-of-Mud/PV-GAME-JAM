# This module handles all drawing operations for the game

import pygame
import pygame
from utils import load_sprite, get_random_position, text_to_screen, load_background_obj
from pygame.transform import rotozoom, scale
from map import Map

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 600))

        # Initialize Map object
        map = Map(self.screen.get_width(), self.screen.get_height())

        self.background = scale(map.background, (50, 50))
        self.game_objects = []

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # Clear screen with black\
        for x in range(self.screen.get_width()):
            for y in range(self.screen.get_height()):
                if x % 50 == 0:
                    if y % 50 == 0:
                        self.screen.blit(self.background, (x, y))

        for game_object in self.game_objects:
            game_object.draw(self.screen)

        pygame.display.flip()
        
        # Sets the game to run 60 ticks per second (FPS)
        clock = pygame.time.Clock()
        clock.tick(60)
    
    def _set_game_objects(self, player, zombies, grass):
        game_objects = [*grass]

        if player:
            game_objects.append(player)
        if zombies:
            game_objects += [*zombies]
        
        self.game_objects = game_objects