#!/usr/bin/env python

import opc
import math
import copy
from time import sleep


from .tentacle import Tentacle
from .color import wheel, Colors


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

    def multi_swipe_up(self, tentacles=[1, 2, 3, 4, 5, 6], color=Colors("purple"), tsleep=0.01):
        for p in range(self.__l):
            for t in tentacles:
                start, _ = self.tentacles[t].dims()
                self.pixels[start + p] = color.rgb

            self.write_pixels(tsleep)

    def swipe_blob(self, tentacles=[1, 2, 3, 4, 5, 6], color=Colors("purple"), tsleep=0.01):
        colors = []
        copy_color = color
        n = 10
        for c in range(n):
            copy_color.luminance = c / n
            colors.append(copy_color.rgb)

        for p in range(self.__l):
            for t in tentacles:
                start, end = self.tentacles[t].dims()
                for i, c in enumerate(colors):
                    ref = start - p - i
                    if ref < self.total_pixels:
                        # if start <= ref <= end:
                        self.pixels[ref] = c

            self.write_pixels(tsleep)
