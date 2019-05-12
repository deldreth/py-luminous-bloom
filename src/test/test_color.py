#!/usr/bin/env python

import unittest

from bloom.color import Colors, range_or_luminance


class ColorCase(unittest.TestCase):
    def test_get_rgb(self):
        self.assertEqual(Colors("#FF0000").rgb, (255, 0, 0))
        self.assertEqual(Colors("#00FF00").rgb, (0, 255, 0))
        self.assertEqual(Colors("#0000FF").rgb, (0, 0, 255))

    def test_range_or_luminance(self):
        colors = range_or_luminance(Colors("purple"), 10)
        expected = [(0, 0, 0), (26, 0, 25), (51, 0, 51), (76, 0, 76), (102, 0, 102),
                    (128, 0, 127), (153, 0, 153), (178, 0, 178), (204, 0, 204), (230, 0, 229)]
        self.assertEqual(colors, expected)

        colors = list(Colors("purple").range_to(Colors("white"), 5))
        expected = [(128, 0, 128), (28, 70, 196),
                    (112, 207, 160), (213, 219, 195), (255, 255, 255)]
        self.assertEqual(range_or_luminance(colors, 5), expected)
