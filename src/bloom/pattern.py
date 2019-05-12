#!/usr/bin/env python

import types
from collections import deque


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
    """
    __l = 64

    def __init__(self, l, color_or_range):
        whole = range(self.__l)
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

    def shift(self, step=1):
        self.rotate(step)


class Range(deque):
    def __init__(self, color_range):
        if isinstance(color_range, types.GeneratorType):
            color_range = list(color_range)

        for color in color_range:
            self.append(color.rgb)

        # length = len(self)
        # if length < 64:
        #     for _ in range(63 - length):
        #         self.append((0, 0, 0))
