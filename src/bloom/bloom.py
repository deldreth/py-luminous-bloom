#!/usr/bin/env python

from enum import Enum
import opc
import math
import copy
from time import sleep


from .tentacle import Tentacle
from .color import wheel, range_or_luminance, Colors
from .pattern import Pattern


class Direction(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class LuminousBloom(object):
    __l = 64
    __rng = range(__l)
    total_pixels = 385
    tentacles = {
        1: Tentacle(1),
        2: Tentacle(2),
        3: Tentacle(3),
        4: Tentacle(4),
        5: Tentacle(5),
        6: Tentacle(6),
    }

    def __init__(self, client="localhost:7890"):
        self.client = opc.Client(client)
        self.pixels = [(0, 0, 0) for x in range(self.total_pixels)]

        self.write_pixels()

    def write_pixels(self, tsleep=0):
        self.client.put_pixels(self.pixels, 0)
        sleep(tsleep)

    def end_test(self):
        for t in self.tentacles:
            start, end = self.tentacles[t].dims()
            self.pixels[start] = Colors("purple").rgb
            self.pixels[end] = Colors("blue").rgb

            self.pixels[start+5] = Colors("purple").rgb
            # self.pixels[end+5] = Colors("blue").rgb

        self.write_pixels()

    def put(self, t, red=0, green=0, blue=0, rgb=(0, 0, 0)):
        if rgb > (0, 0, 0):
            red, green, blue = rgb

        self.pixels = self.tentacles[t].set(self.pixels, red, green, blue)

    def rainbow_rotate(self, tsleep=0.1):
        for color in range(1, 250, 20):
            for t in range(1, 7):
                self.put(t, rgb=wheel(color))
                self.write_pixels(tsleep)

    def rotate(self, color, loops=5, direction=Direction.RIGHT, tsleep=1/20):
        color = range_or_luminance(color, 64)

        tentacles = list(self.tentacles.items())
        if direction is Direction.LEFT:
            tentacles = list(reversed(tentacles))

        for _ in range(loops):
            for _, tentacle in tentacles:
                self.pixels = [(0, 0, 0)] * self.total_pixels

                for ic, c in enumerate(color):
                    start, _ = tentacle.dims()
                    self.pixels[start + ic] = c

                self.write_pixels(tsleep)

    def swipe(self, tentacles=[1, 2, 3, 4, 5, 6],
              color=Colors("purple"), direction=Direction.UP, tsleep=0.01):
        rng = range(self.__l)

        if direction is Direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for t in tentacles:
                start, _ = self.tentacles[t].dims()
                self.pixels[start + p] = color.rgb

            self.write_pixels(tsleep)

    def swipe_blob(self, color, l=64, tentacles=[1, 2, 3, 4, 5, 6], direction=Direction.UP, tsleep=0.01):
        colors = range_or_luminance(color, l)

        rng = range(l * -1, self.__l + l)

        if direction is Direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for i, c in enumerate(colors):
                if direction is Direction.DOWN:
                    i *= -1

                for t in tentacles:
                    tentacle = self.tentacles[t]
                    start, _ = tentacle.dims()

                    pixel = start + p + i
                    if tentacle.contains(pixel):
                        self.pixels[pixel] = c

            self.write_pixels(tsleep)

    def swipe_pattern(self, colors, tentacles=[1, 2, 3, 4, 5, 6], direction=Direction.UP, tsleep=1/60):
        length = len(colors)
        pattern = Pattern(length, colors)

        rng = range(length * -1, self.__l + length)

        if direction is Direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for i, c in enumerate(pattern):
                if direction is Direction.DOWN:
                    i *= -1

                for t in tentacles:
                    tentacle = self.tentacles[t]
                    start, _ = tentacle.dims()

                    pixel = start + p + i
                    if tentacle.contains(pixel):
                        self.pixels[pixel] = c

            self.write_pixels(tsleep)

    def stripe(self, loops=8, length=8, step=1, tentacles=[1, 2, 3, 4, 5, 6],
               color=Colors("purple"), direction=Direction.UP, tsleep=1 / 60):
        pattern = Pattern(length, color)

        if direction is Direction.DOWN:
            step *= -1

        for _ in range(loops * length):
            for key, t in self.tentacles.items():
                if key in tentacles:
                    self.pixels = t.set_pattern(self.pixels, pattern)

            pattern.shift(step)
            self.write_pixels(tsleep)

    def swirl(self, loops=7, length=8, step=3, tentacles=[1, 2, 3, 4, 5, 6],
              color=Colors("purple"), direction=Direction.UP, tsleep=1 / 60):
        pattern = Pattern(length, color)

        if direction is Direction.DOWN:
            step *= -1

        for _ in self.__rng:
            for key, t in self.tentacles.items():
                if key in tentacles:
                    self.pixels = t.set_pattern(self.pixels, pattern)
                pattern.shift(step)

            self.write_pixels(tsleep)

    def fade(self, colors, tentacles=[1, 2, 3, 4, 5, 6], tsleep=1/8):
        for c in colors:
            for t in tentacles:
                for p in self.tentacles[t]:
                    self.pixels[p] = c.rgb

            self.write_pixels(tsleep)

    def fade_multi(self, colors, tentacles=[[1, 3, 5], [2, 4, 6]], rotate=False, tsleep=1/16):
        """
        fade_multi allows for multiple color generators to be traversed for any number of tentacles.

        The list of color generators and the list of tentacle lists must have the same length.

        rotate=True will force each tentacle to write in sequence instead of at the same time
        """
        if len(colors) is not len(tentacles):
            raise Exception(
                'fade_multi: colors and tentacles should be lists of the same length')

        tentacle_colors = []
        color = None
        for ti, tlist in enumerate(tentacles):
            # generators cannot be rolled back, list() traverses the generator
            color = list(colors[ti])

            for t in tlist:
                tentacle_colors.append((self.tentacles[t], color))

        for x in range(len(color)):
            for tentacle, color in tentacle_colors:
                self.pixels = tentacle.colorize(self.pixels, color[x].rgb)

                if rotate is True:
                    self.write_pixels(tsleep)
            if rotate is False:
                self.write_pixels(tsleep)
