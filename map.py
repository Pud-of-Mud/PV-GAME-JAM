import pygame
from utils import load_sprite, load_background_obj

class Map:
    def __init__(self, width, height):
        self.width = width / 50
        self.height = height /50
        self.back0 = None
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        
    
    def map1(self):
        k = {
            "0": load_background_obj("soils", "ground", False),
            "l": load_background_obj("grassdirt", "grassdirtLEFT"),
            "r": load_background_obj("grassdirt", "grassdirtRIGHT"),
            "tr": load_background_obj("grassdirt", "grassdirtTOP_RIGHT"),
            "tl": load_background_obj("grassdirt", "grassdirtTOP_LEFT"),
            "br": load_background_obj("grassdirt", "grassdirtBOT_RIGHT"),
            "bl": load_background_obj("grassdirt", "grassdirtBOT_LEFT"),
            "x": load_background_obj("grassdirt", "grasstile", False),
            "t": load_background_obj("grassdirt", "grassdirtTOP", False),
            "b": load_background_obj("grassdirt", "grassdirtBOT", False)
        }
        
        tiles = [
            [k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"] , k["x"], k["x"], k["x"], k["x"], k["x"], k["x"]], 
            [k["x"], k["x"], k["x"], k["x"], k["tl"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"], k["t"] ,k["t"], k["tr"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]], 
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]], 
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["l"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"], k["0"] ,k["0"], k["r"], k["x"], k["x"], k["x"], k["x"]], 
            [k["x"], k["x"], k["x"], k["x"], k["bl"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"], k["b"] ,k["b"], k["br"], k["x"], k["x"], k["x"], k["x"]],
            [k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"], k["x"] , k["x"], k["x"], k["x"], k["x"], k["x"], k["x"]]
        ] 
        return tiles
    
    def obstacle_map1(self):
        obstacles = [
            [0 for _ in range(int(self.width))] 
            for _ in range(int(self.height))
        ] 
        return obstacles

