#!/usr/bin/env python

import unittest

from bloom.image import Image


class ImageCase(unittest.TestCase):
    def test_get_lines(self):
        lines = Image().get_lines("images/color_waves.jpg")

        self.assertEqual(len(lines), 64)

        for line in lines:
            self.assertEqual(len(line), 64)
