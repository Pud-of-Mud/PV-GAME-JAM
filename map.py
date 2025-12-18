import pygame
from utils import load_sprite, load_background_obj

class Map:
    def __init__(self, width, height):
        self.width = width / 50
        self.height = height /50
        self.back = None
    
    def tile_convert(self, map_str, k):
        tiles = [
            [k[char] for char in line.strip()] 
            for line in map_str.strip().splitlines()
        ]
        return tiles

    # map1 function: creates a tile-based map layout
    # To make a new map:
    # 1. Define a new dictionary mapping characters to background objects
    # 2. Create a new multi-line string representing the map layout
    # 3. Use tile_convert to convert the string into a 2D list of background objects
    
    def map1(self):
        k = {
            "0": load_background_obj("soils", "ground", False),
            "l": load_background_obj("grassdirt", "grassdirtLEFT"),
            "r": load_background_obj("grassdirt", "grassdirtRIGHT"),
            "1": load_background_obj("grassdirt", "grassdirtTOP_RIGHT"),
            "2": load_background_obj("grassdirt", "grassdirtTOP_LEFT"),
            "3": load_background_obj("grassdirt", "grassdirtBOT_RIGHT"),
            "4": load_background_obj("grassdirt", "grassdirtBOT_LEFT"),
            "x": load_background_obj("grassdirt", "grasstile", False),
            "t": load_background_obj("grassdirt", "grassdirtTOP", False),
            "b": load_background_obj("grassdirt", "grassdirtBOT", False)
        }
        
        map1 = '''
        xxxxxxxxxxxxxxxxxxxxxxxx
        xxxx2tttttttttttttt1xxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxxl00000000000000rxxxx
        xxxx4bbbbbbbbbbbbbb3xxxx
        xxxxxxxxxxxxxxxxxxxxxxxx
        '''

        tiles = self.tile_convert(map1, k)

        return tiles
    
    def obstacle_map1(self):
        obstacles = [
            [0 for _ in range(int(self.width))] 
            for _ in range(int(self.height))
        ] 
        return obstacles

