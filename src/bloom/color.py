#!/usr/bin/env python

from colour import Color, color_scale


class Colors(Color):
    def __init__(self, color=None, pick_for=None, **kwargs):
        super().__init__(color, pick_for, kwargs)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return str(self.rgb)

    def get_rgb(self):
        red, green, blue = super().get_rgb()
        return (round(red * 255), round(green * 255), round(blue * 255))

    def range_to(self, color, distance):
        for hsl in color_scale(self._hsl, color.hsl, distance - 1):
            yield Colors(hsl=hsl)


def range_or_luminance(color, length):
    """
    Given a single color return a list of luminance adjusted rgb values (dark to bright).
    Given a list of colors return a list of their rgb values
    """
    colors = []
    if isinstance(color, (list,)):
        colors.append((0, 0, 0))
        for c in color:
            colors.append(c.rgb)
    else:
        for c in range(length):
            color.luminance = c / (length * 2)
            colors.append(color.rgb)

    return colors


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
