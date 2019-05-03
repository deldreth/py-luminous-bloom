#!/usr/bin/env python

from colour import Color


class Colors(Color):
    def __init__(self, color=None,
                 pick_for=None):
        super().__init__(color, pick_for)

    def get_rgb(self):
        red, green, blue = super().get_rgb()
        return (red * 255, green * 255, blue * 255)


def wheel(value):
    """ Given 0-255, make an rgb color with gamma correction """
    if value < 85:
        return (value * 3, 255 - value * 3, 0)
    elif value < 170:
        value -= 85
        return (255 - value * 3, 0, value * 3)
    else:
        value -= 170
        return (0, value * 3, 255 - value * 3)
