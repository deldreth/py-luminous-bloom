#!/usr/bin/env python


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
