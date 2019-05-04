#!/usr/bin/env python

from enum import Enum
import opc
import math
import copy
from time import sleep


from .tentacle import Tentacle
from .color import wheel, range_or_luminance, Colors


class Direction(Enum):
    UP = "up"
    DOWN = "down"


class LuminousBloom(object):
    __l = 64
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

    def swipe_down(self, tentacle, color=(255, 255, 255), tsleep=0.01):
        for t in reversed(self.tentacles[tentacle]):
            self.pixels[t] = color
            self.write_pixels(tsleep)

    def swipe_up(self, tentacle, color=(255, 255, 255), tsleep=0.01):
        for t in self.tentacles[tentacle]:
            self.pixels[t] = color
            self.write_pixels(tsleep)

    def rainbow_rotate(self, tsleep=0.1):
        for color in range(1, 250, 20):
            for t in range(1, 7):
                self.put(t, rgb=wheel(color))
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

    def swipe_blob(self, l=64, tentacles=[1, 2, 3, 4, 5, 6],
                   color=Colors("purple"), direction=Direction.UP, tsleep=0.01):
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
