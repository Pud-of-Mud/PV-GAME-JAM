import pygame
from utils import load_sprite, load_background_obj

class Map:
    def __init__(self, width, height):
        self.width = width / 50
        self.height = height /50
        self.background = None
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.key_back = {
            "ground": load_background_obj("soils", "ground", False),
            "grdBOT": load_background_obj("grassdirt", "grassdirtBOT"),
            "grdTOP": load_background_obj("grassdirt", "grassdirtTOP"),
            "grdLEFT": load_background_obj("grassdirt", "grassdirtLEFT"),
            "grdRIGHT": load_background_obj("grassdirt", "grassdirtRIGHT"),
            "grdTR": load_background_obj("grassdirt", "grassdirtTOP_RIGHT")
        }
    
    def map1(self):

        self.background
        tiles = [
            [self.key_back["ground"] for _ in range(int(self.width))] 
            for _ in range(int(self.height))
        ] 
        return tiles

