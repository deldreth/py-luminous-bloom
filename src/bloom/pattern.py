#!/usr/bin/env python

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

    def __init__(self, l, color):
        whole = range(self.__l)
        steps = whole[0::l]
        for index, _ in enumerate(steps):
            for p in range(l):
                if index % 2:
                    self.append((0, 0, 0))
                else:
                    if isinstance(color, (list,)):
                        self.append(color[(p - l) % l].rgb)
                    else:
                        self.append(color.rgb)

    def shift(self, step=1):
        self.rotate(step)
