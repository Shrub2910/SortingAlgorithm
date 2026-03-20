import random
import pygame
import sys

from algorithms import insertionSort, selection_sort, bubbleSort
pygame.init()

# pygame window settings
screenX = 1600
screenY = 900
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithm")

# array initialization
total_lines = 50 # default is 50
value_array = list(range(1, total_lines + 1))

print(value_array)

# some predefined variables
line_width = screenX / total_lines
min_height = screenY / total_lines
TOP_MARGIN = 50
default_color = "white"
selected_color = "orange"

last_update = 0
ITER_DELAY = 100 # default is 100

# sorting variables
current_index = 0
sorter = None
result = ()

running = True

while running:
    now = pygame.time.get_ticks()

    # draw
    screen.fill("black")

    for i, value in enumerate(value_array):
        color = selected_color if i in result else default_color
        height = min_height * value - TOP_MARGIN
        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(line_width * i, screenY - height, line_width, height)
        )

    if now - last_update >= ITER_DELAY:
        if sorter is not None:
            try:
                result = next(sorter)
            except StopIteration:
                sorter = None
        last_update = now

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                sorter = None
                random.shuffle(value_array)
                print(value_array)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                sorter = selection_sort(value_array)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                sorter = insertionSort(value_array)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:
                sorter = bubbleSort(value_array)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()