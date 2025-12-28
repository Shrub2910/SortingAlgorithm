# imports and setup
from unittest import TextTestResult
import pygame
import random
import sys
pygame.init()

# some predefined variables
line_color = "white"
start_x_cord = 1
height = 10
test = 0

# pygame window settings
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithm")
screen.fill("black")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # program code below

    while test != 100:
        pygame.draw.rect(screen, line_color, pygame.Rect(start_x_cord, 1020, 10, 30))
        start_x_cord += 15
        test+=1

    # dont change what is below this
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()