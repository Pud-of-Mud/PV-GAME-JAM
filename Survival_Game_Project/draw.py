# This module handles all drawing operations for the game

import pygame
from utils import load_sprite, get_random_position, text_to_screen

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)

    def _draw(self):
        self.screen.blit(self.background, (0, 0))  # Clear screen with black\
        for x in range(self.screen.get_width()):
            for y in range(self.screen.get_height()):
                if x % 12 == 0:
                    if y % 12 == 0:
                        self.screen.blit(self.background, (x, y))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
    
    def _get_game_objects(self, player, zombies, grass):
        game_objects = [*grass]

        if player:
            game_objects += [*player]
        if zombies:
            game_objects += [*zombies]
        
        
        return game_objects