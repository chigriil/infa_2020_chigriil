import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((775, 1050))
screen.fill((255, 255, 255))

# screen filling
rect(screen, (230, 230, 230), (0, 0, 775, 470))


# horizontal lines between ice blocks, r_1 is for new radius drawing z is for vertical line offset
def draw_hor_line(x, y, z, r, r_1, r_2):
    for i in range(0, 4):
        r_1 = r * np.cos(0 + i * np.pi / 8)
        r_2 = r * np.sin(0 + i * np.pi / 8)
        aalines(screen, (0, 0, 0), False, ((x - r_1, y - r_2), (x - r_1 / 2, y + z - r_2),
                                           (x, y + z - r_2), (x + r_1 / 2, y - r_2 + z / 2),
                                           (x + r_1, y - r_2)))


# vertical lines between ice blocks
def draw_vert_line(x, y, r, z):
    arc(screen, (0, 0, 0), (x - int(r / 6), y - r, int(r / 3), 2 * (r + z)), 0, np.pi, 1)
    arc(screen, (0, 0, 0), (x - int(3 * r / 5), y - r, int(6 * r / 5), 2 * (r + z)), 0, np.pi, 1)


# function to draw turned ellipses
def turned_ellipse(x0, y0, r, g, b, alpha, x1, y1):
    turned_ellipse_surf = pygame.Surface((x0, y0), pygame.SRCALPHA)
    ellipse(turned_ellipse_surf, (r, g, b), (0, 0, x0, y0))
    turned_ellipse_surf = pygame.transform.rotate(turned_ellipse_surf, alpha)
    screen.blit(turned_ellipse_surf, (x1, y1))


# ice home
def draw_home(x, y, r, z, r_1, r_2):
    circle(screen, (230, 230, 230), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, 2)
    rect(screen, (250, 250, 250), (x - r, y, 2 * r, r))
    draw_hor_line(x, y, z, r, r_1, r_2)
    draw_vert_line(x, y, r, z)


# function to draw men
def draw_men(x, y, z, k):
    k = 2 * z
    # body
    ellipse(screen, (142, 125, 113), (x, y, z, k))
    # left arm
    ellipse(screen, (142, 125, 113), (x - int(z / 3), y + int(k / 6), int(2 * z / 3), int(k / 12)))
    # turned arm
    turned_ellipse(int(2 * z / 3), int(k / 12), 142, 125, 113, -45, x + int(2 * z / 3), y + int(k / 6))
    # cutting body ellipse
    rect(screen, (255, 255, 255), (x, y + int(k / 2), z, int(k / 2)))
    # legs
    ellipse(screen, (142, 125, 113), (x + int(z / 5), y + int(k / 2), int(z / 5), int(k / 6)))
    ellipse(screen, (142, 125, 113), (x + int(z / 5) + int(z / 2), y + int(k / 2), int(z / 5), int(k / 6)))
    # down rects
    rect(screen, (106, 93, 84), (x, y + int(k / 2), z, int(z / 6)))
    rect(screen, (106, 93, 84), (x + int(z / 3), y + int(k / 15), int(4 * z / 15), int(k / 2)))
    # down legs
    ellipse(screen, (142, 125, 113), (x, int(y + k / 2 + k / 10), int(z / 3), int(k / 10)))
    ellipse(screen, (142, 125, 113), (int(x + z / 2 + z / 5), int(y + k / 2 + k / 10), int(z / 3), int(k / 10)))
    # face
    ellipse_surface_rect = pygame.Surface((1000, 1050), pygame.SRCALPHA)
    ellipse(ellipse_surface_rect, (226, 226, 226, 100), (x, y - int(k / 8), z, int(k / 4)))
    screen.blit(ellipse_surface_rect, (0, 0))
    ellipse(screen, (170, 157, 150), (x + int(z / 6), y - int(k / 8), int(2 * z / 3), int(k / 5)))
    ellipse(screen, (226, 219, 219), (x + int(z / 3), y - int(k / 16), int(z / 3), int(k / 8)))
    # content of face
    line(screen, (0, 0, 0), (x + int(2 * z / 5), y - int(k / 30)), (int(x + 9 * z / 20), int(y - k / 40)), 1)
    line(screen, (0, 0, 0), (x + int(3 * z / 5), y - int(k / 30)), (x + int(z / 2), y - int(k / 40)), 1)
    arc(screen, (0, 0, 0), (x + int(2 * z / 5), y, int(z / 6), int(k / 10)), 0, np.pi)
    # stick
    line(screen, (0, 0, 0), (x - int(z / 3), y), (x - int(2 * z / 15), y + int(k / 2)), 1)


def draw_catfish(x, y, k, z):
    # cat body
    ellipse(screen, (204, 204, 204), (x, y, k, z))
    # cat legs
    turned_ellipse(int(k / 2), int(3 * z / 10), 204, 204, 204, 10, x - int(k / 5), y + int(3 * z / 5))
    ellipse(screen, (204, 204, 204), (x - int(k / 3), y + int(2 * z / 5), int(k / 2), int(3 * z / 10)))
    turned_ellipse(int(k / 2), int(3 * z / 10), 204, 204, 204, -30, x + int(13 * k / 15), y + int(z / 5))
    turned_ellipse(int(k / 2), int(3 * z / 10), 204, 204, 204, -30, x + int(13 * k / 15), y + int(3 * z / 5))
    # cat's tail
    turned_ellipse(int(2 * k / 3), int(2 * z / 5), 204, 204, 204, 45, x + int(4 * k / 5), y - int(4 * z / 5))
    # fish fins
    polygon(screen, (197, 102, 99), ((x - int(k / 10), y - int(z / 5)), (x - int(k / 15), y + int(z / 5)),
                                     (x, y + int(2 * z / 5)), (x - int(k / 30), y + int(z / 10))))
    polygon(screen, (197, 102, 99), ((x - int(k / 15), y - int(z / 5)), (x, y - int(3 * z / 10)),
                                     (x + int(k / 15), y - int(z / 5)), (z, y - int(z / 5))))
    # fish
    turned_ellipse(int(k / 3), int(2 * z / 5), 152, 171, 167, -30, x - int(k / 6), y - int(2 * z / 5))
    # head
    turned_ellipse(int(4 * k / 15), int(3 * z / 5), 204, 204, 204, 10, x, y - int(2 * z / 5))
    # fish's tail
    polygon(screen, (152, 171, 167), ((x + int(k / 10), y + int(3 * z / 10)), (x + int(4 * k / 15), y + int(z / 10)),
                                      (x + int(k / 6), y + int(3 * z / 5))))
    # ears
    polygon(screen, (204, 204, 204), ((x + int(k / 10), y - int(3 * z / 10)), (x + int(k / 6), y - int(z / 2)),
                                      (x + int(k / 5), y - int(3 * z / 10))))
    polygon(screen, (204, 204, 204), ((x + int(7 * k / 30), y - int(3 * z / 10)), (x + int(4 * k / 15), y - int(z / 2)),
                                      (x + int(4 * k / 15), y)))
    # eyes
    circle(screen, (242, 242, 242), (x + int(k / 10), y - int(z / 10)), int(2 * k / z))
    circle(screen, (242, 242, 242), (x + int(k / 5), y - int(z / 10)), int(2 * k / z))
    circle(screen, (0, 0, 0), (x + int(k / 10), y - int(z / 10)), int(k / z))
    circle(screen, (0, 0, 0), (x + int(k / 5), y - int(z / 10)), int(k / z))
    # nose
    circle(screen, (0, 0, 0), (x + int(2 * k / 15), y), int(k / z))

    # fish eye
    circle(screen, (0, 32, 238), (x - int(k / 15), y - int(z / 10)), int(k / z))

    # cat's teeth
    polygon(screen, (255, 255, 255),
            ((x + int(7 * k / 150), y + int(z / 5)), (x + int(3 * k / 50), y + int(3 * z / 10)),
             (x + int(2 * k / 25), y + int(z / 5))))
    polygon(screen, (255, 255, 255), ((x + int(2 * k / 15), y + int(z / 5)), (x + int(4 * k / 24), y + int(3 * z / 10)),
                                      (x + int(13 * 150 / 75), y + int(z / 5))))


# drawing homes
draw_home(50, 500, 75, 5, 0, 0)
draw_home(450, 550, 90, 5, 0, 0)
draw_home(250, 600, 150, 5, 0, 0)
draw_home(100, 650, 100, 5, 0, 0)
draw_home(400, 700, 100, 5, 0, 0)

# drawing men

draw_men(700, 500, 40, 0)
draw_men(650, 450, 40, 0)
draw_men(600, 550, 50, 0)
draw_men(500, 500, 50, 0)
draw_men(510, 600, 100, 0)
draw_men(700, 600, 70, 0)
draw_men(600, 650, 100, 0)

# drawing cats with fish
draw_catfish(-40, 850, 150, 50)
draw_catfish(100, 750, 150, 50)
draw_catfish(300, 850, 150, 50)
draw_catfish(700, 800, 150, 50)
draw_catfish(600, 900, 150, 50)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

