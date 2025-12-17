from pygame.math import Vector2
from pygame.transform import rotozoom, scale
from utils import load_sprite, get_random_position, text_to_screen

UP = Vector2(0, -1)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)
RIGHT = Vector2(1, 0)

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

    """
    def rotate(self, direction):
        new_sprite = rotozoom(self.sprite, angle, 1)
        old_center = self.sprite.get_rect().center
        new_rect = new_sprite.get_rect(center=old_center)
        self.sprite = new_sprite
        self.position = Vector2(new_rect.topleft) + Vector2(old_center)
    """

    def is_colliding_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance < self.radius + other.radius


class Player(Object):
    ACCELERATION = 0.2
    ANIMATION_SPEED = 5  # frames per animation cycle
    
    def __init__(self, position):
        sprite = scale(load_sprite("Player", "PlayerForward"), (60, 60))
        self.direction = UP
        self.score = 0
        self.animation_frame = 0
        self.is_moving = 0
        #self.is_moving_
        super().__init__(0, position, sprite, Vector2(0))

    # rotate the player sprite
    def rotate(self, direction):
        
        # set direction vector based on input
        if direction == "StandRight" or direction == "WalkRight":
            self.direction = RIGHT
            self.is_moving = 4
        elif direction == "StandLeft" or direction == "WalkLeft":
            self.direction = LEFT
            self.is_moving = 3
        elif direction == "Back" or direction == "Back1":
            self.direction = UP
            self.is_moving = 2
        elif direction == "Forward" or direction == "Forward1":
            self.direction = DOWN
            self.is_moving = 1
        
        # change sprite based on direction
        sprites = {
            "StandRight": "PlayerStandRight",
            "StandLeft": "PlayerStandLeft",
            "WalkRight": "PlayerWalkRight",
            "WalkLeft": "PlayerWalkLeft",
            "Back": "PlayerBack",
            "Forward": "PlayerForward",
            "Back1": "PlayerBack1", 
            "Forward1": "PlayerForward1",
        }

        new_sprite = scale(load_sprite("Player", sprites[direction]), (60, 60))
        # old_center = self.sprite.get_rect().center
        # new_rect = new_sprite.get_rect(center=old_center)
        self.sprite = new_sprite
        # self.position = Vector2(new_rect.topleft) + Vector2(old_center)

    def accelerate(self, speed):
        self.velocity += self.direction * speed
        if self.velocity.length() > speed:
            self.velocity.scale_to_length(speed)

    # animation update for the player sprite
    def update(self):
        if self.is_moving == 1:
            self.animation_frame += 1
            if self.animation_frame >= self.ANIMATION_SPEED:
                self.animation_frame = 0
            
            # Alternate between Forward and Forward1 sprites
            sprite_name = "PlayerForward" if self.animation_frame < self.ANIMATION_SPEED // 2 else "PlayerForward1"
            self.sprite = scale(load_sprite("Player", sprite_name), (60, 60))
        
        elif self.is_moving == 2:
            self.animation_frame += 1
            if self.animation_frame >= self.ANIMATION_SPEED:
                self.animation_frame = 0
            
            # Alternate between Back and Back1 sprites
            sprite_name = "PlayerBack" if self.animation_frame < self.ANIMATION_SPEED // 2 else "PlayerBack1"
            self.sprite = scale(load_sprite("Player", sprite_name), (60, 60))
        
        elif self.is_moving == 3:
            self.animation_frame += 1
            if self.animation_frame >= self.ANIMATION_SPEED:
                self.animation_frame = 0
            
            # Alternate between WalkLeft sprites
            sprite_name = "PlayerWalkLeft" if self.animation_frame < self.ANIMATION_SPEED // 2 else "PlayerStandLeft"
            self.sprite = scale(load_sprite("Player", sprite_name), (60, 60))
        
        elif self.is_moving == 4:
            self.animation_frame += 1
            if self.animation_frame >= self.ANIMATION_SPEED:
                self.animation_frame = 0
            
            # Alternate between WalkRight sprites
            sprite_name = "PlayerWalkRight" if self.animation_frame < self.ANIMATION_SPEED // 2 else "PlayerStandRight"
            self.sprite = scale(load_sprite("Player", sprite_name), (60, 60))
        
        if self.is_moving == 0:
            self.animation_frame = 0
            if self.direction == LEFT:
                self.sprite = scale(load_sprite("Player", "PlayerStandLeft"), (60, 60))
            elif self.direction == RIGHT:
                self.sprite = scale(load_sprite("Player", "PlayerStandRight"), (60, 60))

class Zombie(Object):
    def __init__(self, name, position, sprite, velocity):
        #sprite = load_sprite("zombie")
        super().__init__(name, position, sprite, velocity)

class Grass(Object):
    def __init__(self, position, time, num=3):
        sprites = {1: "ground",
                   2: "dry grass",
                   3: "grass"}
        grass_type = sprites[num]
        sprite = scale(load_sprite("Grass", grass_type), (50, 50))
        super().__init__(time, position, sprite, Vector2(0))