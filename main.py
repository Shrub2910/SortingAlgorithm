# imports and setup
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
screenX = 1920
screenY = 1080
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithm")
screen.fill("black")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # program code below

    while test != 128:

        y = screenY - height
        pygame.draw.rect(screen, line_color, pygame.Rect(start_x_cord, y, 15, height))
        height = random.randrange(10, 1080)
        start_x_cord += 15
        test+=1

    # dont change what is below this
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()