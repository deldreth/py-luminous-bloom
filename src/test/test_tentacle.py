#!/usr/bin/env python

import unittest

from bloom.tentacle import Tentacle


class TentacleCase(unittest.TestCase):
    def test_init(self):
        tentacle = Tentacle(1)
        self.assertEqual(tentacle.dims()['start'], 0)
        self.assertEqual(tentacle.dims()['end'], 63)

        tentacle = Tentacle(2)
        self.assertEqual(tentacle.dims()['start'], 64)
        self.assertEqual(tentacle.dims()['end'], 127)

    def test_which(self):
        tentacle = Tentacle(2)
        self.assertEqual(tentacle.which(), 2)

    def test_dims(self):
        tentacle = Tentacle(3)
        dims = tentacle.dims()
        self.assertEqual(dims["start"], 128)
        self.assertEqual(dims["end"], 191)
