import pygame
from math import pi

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


