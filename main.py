# imports and setup
import pygame
import random
import sys
pygame.init()

# some predefined variables
background_color = (255, 255, 255)


# pygame window settings
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithm")


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # program code below
    surface.fill((background_color))

    # dont change what is below this
    pygame.display.flip
    clock.tick()

pygame.quit()
sys.exit()