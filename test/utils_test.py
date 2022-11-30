from utils import Point, ColorPoint
import pygame

def test_coord():
    c = Point(1, 2)
    assert isinstance(c, list)
    assert 1 == c.x
    assert 2 == c.y

def test_color_coord():
    c = ColorPoint(1, 2, pygame.Color(0,0,0))
    assert isinstance(c, list)
    assert 1 == c.x
    assert 2 == c.y
    assert (0,0,0) == c.color