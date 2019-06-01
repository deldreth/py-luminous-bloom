#!/usr/bin/env python

import types
from collections import deque

from .tentacle import LENGTH


class Pattern(deque):
    """
    A Pattern is a deque which contains repeating number of colored
    elements of an arbitary length offset by the same length.

    e.g.,
    pattern = Pattern(1, color)
    [color, black, color, black, color, black, ...]

    pattern = Pattern(2, color)
    [color, color, black, black, color, color, ...]

    Provided color may also be a list of colors equal to the length (l) of the pattern

    Parameters
    ----------
    l : integer
        The length of the color or range being provided
    color_or_range: :class:`~bloom.color.Colors` | List(:class:`~bloom.color.Colors`)
        The color or range to use for the pattern.
    """

    def __init__(self, l, color_or_range):
        whole = range(LENGTH)
        steps = whole[0::l]
        for index, _ in enumerate(steps):
            for p in range(l):
                if index % 2:
                    self.append((0, 0, 0))
                else:
                    if isinstance(color_or_range, (list,)):
                        self.append(color_or_range[(p - l) % l].rgb)
                    else:
                        self.append(color_or_range.rgb)


class Range(deque):
    """A deque constructed of a range of :class:`~bloom.color.Colors` (generator) 
    or list of :class:`~bloom.color.Colors`.

    Parameters
    ----------
    color_range: Iterator(:class:`~bloom.color.Colors`) | List(:class:`~bloom.color.Colors`)
        The color or range to use for the pattern.
    """
    def __init__(self, color_range):
        if isinstance(color_range, types.GeneratorType):
            color_range = list(color_range)

        for color in color_range:
            self.append(color.rgb)
