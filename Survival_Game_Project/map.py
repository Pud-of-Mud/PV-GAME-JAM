import pygame
from utils import load_sprite, load_background_obj

class Map:
    def __init__(self, width, height):
        self.width = width / 50
        self.height = height /50
        self.background = None
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
    
    def map1(self):
        self.background = load_background_obj("ground")

