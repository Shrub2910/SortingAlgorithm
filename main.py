# imports and setup
import pygame
import random
import sys
pygame.init()

# some predefined variables



# pygame window settings
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithm")
screen.fill("white")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # program code below

    # dont change what is below this
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()