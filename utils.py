import random
import pygame

from pygame import Color
from pygame.image import load
from pygame.math import Vector2

def load_sprite(type, name, with_alpha=True):
    path = f"sprites/{type}/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def load_background_obj(name, with_alpha=True):
    path = f"background objects/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()

def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )

def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

def get_positions(x, y):
    return Vector2(x, y)

def text_to_screen(screen, text, x, y, size, color=(0,0,0), font_type = "fonts/PLACEHOLDER.ttf"):
    try:
        game_font = pygame.font.Font(font_type, size) 
        # Establishes font obj
        
        # generates a surface then places font on it 
        text_surface = game_font.render(text, True, color)  

        # Blits the text onto the screen
        screen.blit(text_surface, (x,y))

    except (Exception):
        print("Font error !")