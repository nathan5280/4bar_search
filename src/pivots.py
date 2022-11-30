import time
from enum import Enum
from math import cos, pi, sin
from telnetlib import SE
from typing import Union

import pygame

from utils import ColorPoint, Origin, Point, Vector, draw_rect, rotate_point

BLACK_CLR = (0, 0, 0)
WHITE_CLR = (255, 255, 255)
SEARCH_CLR = (0, 200, 200)
ACTIVE_CLR = (0, 0, 255)
INACTIVE_CLR = (255, 0, 0)
UNKNOWN_CLR = (50, 50, 50)

SCREEN_SCALE = 5
WORK_AREA = Point(200, 123)
SEARCH_AREA = Vector(75, 28)
SEARCH_INC = Vector(15, 7)  # search increments

CEILING = 94
EXCLUDE_Y = CEILING - 2
FLOOR_CLEARENCE = 5

L0 = Origin(5, CEILING, 0)

t1 = -90
r1 = t1 * 2 * pi / 360
L1 = Origin(
    SEARCH_AREA.x,
    FLOOR_CLEARENCE + -sin(r1) * SEARCH_AREA.x,
    t1,
)  # origin and orientation of position 2

GRID = list[list[ColorPoint]]


def as_screen(natural_coords: Point) -> Point:
    return Point(
        natural_coords.x * SCREEN_SCALE,
        (WORK_AREA.y - natural_coords.y) * SCREEN_SCALE,
    )


def at_scale(natural_coords: Point) -> Point:
    return Point(natural_coords.x * SCREEN_SCALE, natural_coords.y * SCREEN_SCALE)


def generate_search_grid(
    o: Origin, p: Point, inc: Vector, color: pygame.Color
) -> list[list[ColorPoint]]:
    xs = list(range(0, p.x + inc.x, inc.x))
    ys = list(range(p.y, -inc.y, -inc.y))
    coords = []
    for r in ys:
        row = []
        for sp in xs:
            p = rotate_point(o, Point(sp, r))
            cp = ColorPoint(p.x, p.y, color)
            row.append(cp)
        coords.append(row)
    return coords


def draw_background(screen: pygame.Surface, x1_grid: GRID, x2_grid: GRID):
    screen.fill(WHITE_CLR)
    pygame.draw.rect(
        screen,
        BLACK_CLR,
        pygame.Rect(
            *as_screen(Point(WORK_AREA.x / 2, WORK_AREA.y)),
            *at_scale(Point(WORK_AREA.x / 2, WORK_AREA.y - CEILING)),
        ),
    )
    pygame.draw.rect(
        screen,
        BLACK_CLR,
        pygame.Rect(
            *as_screen(Point(0, EXCLUDE_Y)),
            *at_scale(WORK_AREA),
        ),
    )

    draw_rect(screen, SEARCH_CLR, L0, SEARCH_AREA, as_screen)
    draw_rect(screen, SEARCH_CLR, L1, SEARCH_AREA, as_screen)
    for row in x1_grid:
        for point in row:
            pygame.draw.circle(screen, point.color, as_screen(point), 1)
    for row in x2_grid:
        for point in row:
            pygame.draw.circle(screen, point.color, as_screen(point), 1)
    return x1_grid, x2_grid


def run(screen: pygame.Surface):
    x1_grid = generate_search_grid(L0, SEARCH_AREA, SEARCH_INC, UNKNOWN_CLR)
    x2_grid = generate_search_grid(L1, SEARCH_AREA, SEARCH_INC, UNKNOWN_CLR)
    draw_background(screen, x1_grid, x2_grid)
    x_idx, y_idx = 0, 0
    running = True
    while running:
        pygame.display.flip()
        # Did the user click the window close button?
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
        # return


def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (WORK_AREA.x * SCREEN_SCALE, WORK_AREA.y * SCREEN_SCALE)
    )
    run(screen)
    pygame.quit()


if __name__ == "__main__":
    main()
