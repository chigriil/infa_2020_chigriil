import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# screen filling
rect(screen, (217, 217, 217), (0, 0, 400, 400))

# body
circle(screen, (255, 253, 84), (200, 200), 125)
circle(screen, (0, 0, 0), (200, 200), 125, 1)

# eyes
circle(screen, (235, 50, 35), (150, 170), 25)
circle(screen, (0, 0, 0), (150, 170), 25, 1)
circle(screen, (0, 0, 0), (150, 170), 10)
circle(screen, (235, 50, 35), (260, 170), 18)
circle(screen, (0, 0, 0), (260, 170), 18, 1)
circle(screen, (0, 0, 0), (260, 170), 10)

# eyebrows
line(screen, (0, 0, 0), (240, 150), (320, 115), 15)
line(screen, (0, 0, 0), (175, 150), (80, 110), 15)

# mouth
rect(screen, (0, 0, 0), (135, 250, 130, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()