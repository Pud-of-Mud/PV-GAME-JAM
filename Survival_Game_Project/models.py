from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, get_random_position, text_to_screen

UP = Vector2(0, -1)

class Object:
    def __init__(self, time, position, sprite, velocity):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.time = time
        self.sprite = sprite
        self.radius = sprite.get_width() / 2

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius) / 2
        surface.blit(self.sprite, blit_position)

    def move(self, screen_size):
        self.position = self.velocity + self.position
        self.position.x = max(0, min(screen_size[0], self.position.x))
        self.position.y = max(0, min(screen_size[1], self.position.y))

    def rotate(self, angle):
        new_sprite = rotozoom(self.sprite, angle, 1)
        old_center = self.sprite.get_rect().center
        new_rect = new_sprite.get_rect(center=old_center)
        self.sprite = new_sprite
        self.position = Vector2(new_rect.topleft) + Vector2(old_center)

    def is_colliding_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius


class Player(Object):
    ACCELERATION = 0.2
    def __init__(self, position):
        sprite = load_sprite("Player", "PlayerForward")
        self.direction = UP
        self.score = 0
        super().__init__(0, position, sprite, Vector2(0))

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
    
    def deccelerate(self):
        self.velocity -= self.direction * self.ACCELERATION

class Zombie(Object):
    def __init__(self, name, position, sprite, velocity):
        #sprite = load_sprite("zombie")
        super().__init__(name, position, sprite, velocity)

class Grass(Object):
    def __init__(self, time, position, sprite, num=3):
        sprites = {1: "ground",
                   2: "dry grass",
                   3: "grass"}
        grass_type = sprites[num]
        sprite = rotozoom(load_sprite("Grass", grass_type), 0, 0.25)
        super().__init__(time, position, sprite, Vector2(0))