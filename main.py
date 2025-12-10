# Example file showing a basic pygame "game loop"
import pygame
import random
import utils

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 4:3 resolution
clock = pygame.time.Clock() 
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    xpos = random.randint(0, 800)
    ypos = random.randint(0, 600)

    text_gen.text_to_screen(screen, " # ", xpos, ypos, 50)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits tick rate to 60 FPS 

pygame.quit()