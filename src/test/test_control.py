#!/usr/bin/env python

import unittest

from bloom.control import Control


class BloomTest(unittest.TestCase):
    def setUp(self):
        self.control = Control()

    def test_init(self):
        for pixel in self.control.pixels:
            self.assertEqual(pixel, (0, 0, 0))

    def tearDown(self):
        self.control.client.disconnect()
