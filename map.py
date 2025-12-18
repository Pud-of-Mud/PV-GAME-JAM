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
            "grdTR": load_background_obj("grassdirt", "grassdirtTOP_RIGHT"),
            "grdTL": load_background_obj("grassdirt", "grassdirtTOP_LEFT"),
            "grdBR": load_background_obj("grassdirt", "grassdirtBOT_RIGHT"),
            "grdBL": load_background_obj("grassdirt", "grassdirtBOT_LEFT"),
            "grsTile": load_background_obj("grassdirt", "grasstile", False),
            "grdTL1": load_background_obj("grassdirt", "grassdirtTOP_LEFT1"),
            "grdTR1": load_background_obj("grassdirt", "grassdirtTOP_RIGHT1"),
            "grdBL1": load_background_obj("grassdirt", "grassdirtBOT_LEFT1"),
            "grdBR1": load_background_obj("grassdirt", "grassdirtBOT_RIGHT1"),
        }
    
    def map1(self):
        self.background
        tiles = [
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"] , self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]], 
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdTL"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"], self.key_back["grdTOP"] ,self.key_back["grdTOP"], self.key_back["grdTR"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]], 
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]], 
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdLEFT"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"], self.key_back["ground"] ,self.key_back["ground"], self.key_back["grdRIGHT"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]], 
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grdBL"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"], self.key_back["grdBOT"] ,self.key_back["grdBOT"], self.key_back["grdBR"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]],
            [self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"] , self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"], self.key_back["grsTile"]]
        ] 
        return tiles
    
    def obstacle_map1(self):
        obstacles = [
            [0 for _ in range(int(self.width))] 
            for _ in range(int(self.height))
        ] 
        return obstacles

