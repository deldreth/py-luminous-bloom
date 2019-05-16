#!/usr/bin/env python

import unittest

from bloom.bloom import LuminousBloom


class BloomTest(unittest.TestCase):
    def setUp(self):
        self.bloom = LuminousBloom()

    def test_init(self):
        for pixel in self.bloom.pixels:
            self.assertEqual(pixel, (0, 0, 0))

    def tearDown(self):
        self.bloom.client.disconnect()
