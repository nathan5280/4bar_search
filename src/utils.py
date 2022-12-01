from math import cos, pi, sin
from typing import Callable

import pygame


class Point(list):
    def __init__(self, x_: float, y_: float):
        super().__init__([x_, y_])

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]


class Vector(Point):
    def __init__(self, x_: float, y_: float):
        super().__init__(x_, y_)


class ColorPoint(list):
    def __init__(self, x_: float, y_: float, color_: pygame.Color):
        super().__init__([x_, y_, color_])

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def color(self):
        return self[2]

    @color.setter
    def color(self, color):
        self[2] = color


class Origin(list):
    def __init__(self, x_: float, y_: float, theta_: float):
        super().__init__([x_, y_])
        self.theta = theta_
        self.theta_r = theta_ * 2 * pi / 360

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]


def rotate_point(o: Origin, p: Point) -> Point:
    new_x = o.x + cos(o.theta_r) * p.x - sin(o.theta_r) * p.y
    new_y = o.y + sin(o.theta_r) * p.x + cos(o.theta_r) * p.y
    return Point(new_x, new_y)

def draw_rect(
    screen: pygame.Surface,
    color: pygame.Color,
    o: Origin,
    p: Point,
    coord_xformer: Callable
):
    ll = Point(o.x, o.y)
    lr = rotate_point(o, Point(p.x, 0))
    ur = rotate_point(o, Point(p.x, p.y))
    ul = rotate_point(o, Point(0, p.y))
    print(ll, lr, ur, ul)
    pygame.draw.line(screen, color, coord_xformer(ll), coord_xformer(lr))
    pygame.draw.line(screen, color, coord_xformer(lr), coord_xformer(ur))
    pygame.draw.line(screen, color, coord_xformer(ur), coord_xformer(ul))
    pygame.draw.line(screen, color, coord_xformer(ul), coord_xformer(ll))


