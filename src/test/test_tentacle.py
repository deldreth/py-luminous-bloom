#!/usr/bin/env python

import unittest

from bloom.tentacle import Tentacle
from bloom.color import Colors


class TentacleCase(unittest.TestCase):
    def setUp(self):
        self.tentacle = Tentacle(1)

    def test_init(self):
        self.assertEqual(self.tentacle.dims()[0], 0)
        self.assertEqual(self.tentacle.dims()[1], 63)

    def test_which(self):
        self.assertEqual(self.tentacle.which(), 1)

    def test_dims(self):
        start, end = self.tentacle.dims()
        self.assertEqual(start, 0)
        self.assertEqual(end, 63)

    def test_patternize(self):
        colors = list(Colors("Red").range_to(Colors("Blue"), 64))
        pixels = [(0, 0, 0) for x in range(385)]
        pixels = self.tentacle.patternize(pixels, colors)

        self.assertEqual(len(pixels), 385)

        for i in self.tentacle:
            self.assertEqual(pixels[i], colors[i])

    def test_colorize(self):
        pixels = [(0, 0, 0) for x in range(385)]
        pixels = self.tentacle.colorize(pixels, (255, 255, 255))

        self.assertEqual(len(pixels), 385)

        for p in self.tentacle:
            self.assertEqual(pixels[p], (255, 255, 255))

    def test_get(self):
        pixels = [(0, 0, 0) for x in range(385)]
        pixels = self.tentacle.colorize(pixels, (255, 255, 255))

        tentacle_pixels = self.tentacle.get(pixels)

        self.assertEqual(len(tentacle_pixels), 64)

        for p in tentacle_pixels:
            self.assertEqual(p, (255, 255, 255))

    def test_contains(self):
        self.assertTrue(self.tentacle.contains(0))
        self.assertTrue(self.tentacle.contains(32))
        self.assertTrue(self.tentacle.contains(63))
        self.assertFalse(self.tentacle.contains(64))
