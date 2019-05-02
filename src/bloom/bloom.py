#!/usr/bin/python

from time import sleep

from .tentacle import Tentacle

import opc


class LuminousBloom(object):
    total_pixels = 384
    tentacles = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    def __init__(self, client="localhost:7890"):
        self.client = opc.Client(client)
        self.pixels = [(0, 0, 0) for x in range(self.total_pixels)]

        for t in self.tentacles:
            self.tentacles[t] = Tentacle(t, self.pixels)

        self.write_pixels()

    def write_pixels(self, tsleep=0):
        self.client.put_pixels(self.pixels, 0)
        sleep(tsleep)

    def put(self, t, red=0, green=0, blue=0, rgb=(0, 0, 0)):
        if rgb > (0, 0, 0):
            red, green, blue = rgb

        self.pixels = self.tentacles[t].set(self.pixels, red, green, blue)

    def swipe_down(self, tentacle, color=(255, 255, 255), tsleep=0.01):
        for t in self.tentacles[tentacle]:
            self.pixels[t] = color
            self.write_pixels(tsleep)

    def swipe_up(self, tentacle, color=(255, 255, 255), tsleep=0.01):
        for t in reversed(list(self.tentacles[tentacle])):
            self.pixels[t] = color
            self.write_pixels(tsleep)
