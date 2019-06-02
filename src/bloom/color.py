#!/usr/bin/env python

from colour import Color, color_scale


class Colors(Color):
    """Extends the :mod:`~colour` Color class in order to allow for rgb values to
    to be returned as tuples of 0-255."""

    def __init__(self, color=None, pick_for=None, **kwargs):
        super().__init__(color, pick_for, kwargs)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return str(self.rgb)

    def get_rgb(self):
        """Override colour.Color rgb getter to return RGB tuple relative to 255."""
        red, green, blue = super().get_rgb()
        return (round(red * 255), round(green * 255), round(blue * 255))

    def range_to(self, color, distance):
        colors = []
        for hsl in color_scale(self._hsl, color.hsl, distance - 1):
            colors.append(Colors(hsl=hsl))

        return colors


def range_or_luminance(color, length):
    """
    Given a single color return a list of luminance adjusted rgb values (dark to bright).
    Given a list of colors return a list of their rgb values
    """
    colors = []
    if isinstance(color, (list,)):
        # colors.append((0, 0, 0)) # This breaks a few animations but is necessary on others...
        for c in color:
            colors.append(c.rgb)
    else:
        for c in range(length):
            color.luminance = c / (length * 2)
            colors.append(color.rgb)

    return colors
