#!/usr/bin/env python

import unittest

from bloom.tentacle import Tentacle


class TentacleCase(unittest.TestCase):
    def test_init(self):
        tentacle = Tentacle(1)
        self.assertEqual(tentacle.dims()[0], 0)
        self.assertEqual(tentacle.dims()[1], 63)

        tentacle = Tentacle(2)
        self.assertEqual(tentacle.dims()[0], 64)
        self.assertEqual(tentacle.dims()[1], 127)

    def test_which(self):
        tentacle = Tentacle(2)
        self.assertEqual(tentacle.which(), 2)

    def test_dims(self):
        tentacle = Tentacle(3)
        start, end = tentacle.dims()
        self.assertEqual(start, 128)
        self.assertEqual(end, 191)
