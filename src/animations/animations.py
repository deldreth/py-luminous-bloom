#!/usr/bin/env python

from functools import wraps
from random import randrange
from time import perf_counter

from bloom.bloom import LuminousBloom, Direction
from bloom.color import Colors


class Animations():
    odds = [1, 3, 5]
    evens = [2, 4, 6]
    colors = ["MediumBlue", "MediumSpringGreen",
              "Lime", "ForestGreen", "Turquoise",
              "MidnightBlue", "DarkGreen", "Indigo",
              "BlueViolet", "MediumVioletRed",
              "Aquamarine", "Magenta", "DeepPink",
              "HotPink", "FireBrick", "SaddleBrown",
              "DarkGoldenrod", "OrangeRed", "DarkOrange",
              "Gold", "SeaGreen", "DarkBlue"]

    def __init__(self, bloom):
        self.bloom = bloom

    def swipe_and_stripe(self):
        colors = [
            (Colors("OrangeRed"), Colors("SeaGreen")),
            (Colors("DarkGreen"), Colors("Indigo")),
            (Colors("MediumPurple"), Colors("White")),
            (Colors("MediumBlue"), Colors("MediumVioletRed")),
            (Colors("SaddleBrown"), Colors("Yellow")),
        ]

        start = perf_counter()
        while perf_counter() - start < 120:
            color1, color2 = colors[randrange(0, len(colors))]

            for x in range(1, 3):
                color_range = list(color1.range_to(color2, 4 * x))
                self.bloom.swipe_blob(color1, duration=1)
                for d in range(10, 2, -1):
                    self.bloom.stripe(color_range, length=len(
                        color_range), duration=d)

        self.bloom.fade_all()

    def swipe_multi_increment(self):
        range1 = list(Colors("Red").range_to(Colors("Blue"), 8))
        range2 = list(reversed(range1))

        start = perf_counter()
        while perf_counter() - start < 30:
            self.bloom.stripe_multi([range1, range2], duration=5)

    def gradient_spin(self):
        start = perf_counter()
        while perf_counter() - start < 30:
            color1 = self.colors[randrange(0, len(self.colors))]
            color2 = self.colors[randrange(0, len(self.colors))]
            color_range = list(Colors(color1).range_to(Colors(color2), 64))
            for x in range(1, 5):
                self.bloom.rotate(color_range, duration=x * 3)

    def gradient_spin_three(self):
        start = perf_counter()
        while perf_counter() - start < 30:
            color1 = self.colors[randrange(0, len(self.colors))]
            color2 = self.colors[randrange(0, len(self.colors))]
            color_range = list(Colors(color1).range_to(Colors(color2), 64))

            for d in range(15, 5, -1):
                self.bloom.rotate_three(color_range, duration=d)

    def cycle_even_and_odds(self):
        colors = [
            (Colors("White"), Colors("Purple")),
            (Colors("Black"), Colors("Hotpink")),
            (Colors("OrangeRed"), Colors("SeaGreen")),
            (Colors("DarkGreen"), Colors("Indigo")),
            (Colors("MediumPurple"), Colors("White")),
            (Colors("MediumBlue"), Colors("MediumVioletRed")),
            (Colors("SaddleBrown"), Colors("Yellow")),
        ]

        count = 0
        start = perf_counter()
        while perf_counter() - start < 60:
            c1, c2 = colors[count]
            range_to = list(c1.range_to(c2, 32))
            color_list = range_to + list(reversed(range_to[0:31]))

            for _ in range(5):
                self.bloom.cycle(color_list, tentacles=self.odds)
                self.bloom.cycle(color_list, tentacles=self.evens,
                                 direction=Direction.DOWN)

            count += 1

            if count > len(colors) - 1:
                count = 0

        self.bloom.fade_all()

    def cycle_all(self):
        colors = [
            (Colors("Indigo"), Colors("BlueViolet")),
            (Colors("MediumPurple"), Colors("Seagreen")),
            (Colors("SeaGreen"), Colors("OrangeRed")),
            (Colors("OrangeRed"), Colors("Gold")),
            (Colors("Gold"), Colors("MediumBlue")),
            (Colors("MediumBlue"), Colors("MidnightBlue")),
        ]

        start = perf_counter()
        while perf_counter() - start < 60:
            c1, c2 = colors[randrange(0, len(colors))]
            range_to = list(c1.range_to(c2, 32))
            color_list = range_to + list(reversed(range_to[0:31]))

            for _ in range(10):
                self.bloom.cycle(color_list, duration=2)

        self.bloom.fade_all()

    def fast_drops(self):
        start = perf_counter()
        while perf_counter() - start < 60:
            color = Colors(self.colors[randrange(0, len(self.colors))])
            seed = randrange(0, 64)
            self.bloom.ripple(color, seed=seed, fade_out=0.88, duration=1.75)

    def shimmer_with_time(self):
        duration = 2

        def shimmer(c1, c2):
            self.bloom.shimmer_pulse(
                c1, tentacles=self.evens, duration=duration)
            self.bloom.shimmer_pulse(
                c2, tentacles=self.odds, duration=duration)

        start = perf_counter()
        while perf_counter() - start < 60:
            c1 = Colors(self.colors[randrange(0, len(self.colors))])
            c2 = Colors(self.colors[randrange(0, len(self.colors))])
            r = randrange(0, 6)

            for _ in range(r):
                shimmer(c1, c2)
                duration /= 2

            for _ in range(r):
                shimmer(c1, c2)
                duration *= 2

        self.bloom.fade_all()

    def shimmer_heartbeat(self):
        colors = [
            Colors("Seagreen").range_to(Colors("Deeppink"), 8)
        ]

        count = 0
        start = perf_counter()
        while perf_counter() - start < 60:
            for color in colors[count]:
                self.bloom.shimmer_pulse(color, duration=0.3)
                self.bloom.shimmer_pulse(color, duration=1.25)

            count += 1

            if count > len(colors) - 1:
                count = 0

        self.bloom.fade_all()

    def speckle_even_and_odds(self):
        start = perf_counter()
        storage = {}
        while perf_counter() - start < 60:
            c1 = Colors(self.colors[randrange(0, len(self.colors))])
            c2 = Colors(self.colors[randrange(0, len(self.colors))])

            self.bloom.speckle(c1, tentacles=self.evens,
                               maximum=16, storage=storage, duration=10)
            self.bloom.speckle(c2, tentacles=self.odds, storage=storage)

        self.bloom.fade_all()

    def meteors(self):
        start = perf_counter()
        while perf_counter() - start < 60:
            color = self.colors[randrange(0, len(self.colors))]
            self.bloom.meteor(Colors(color), duration=2)

            color = self.colors[randrange(0, len(self.colors))]
            self.bloom.meteor(
                Colors(color), tentacles=self.evens, duration=0.5)

            color = self.colors[randrange(0, len(self.colors))]
            self.bloom.meteor(Colors(color), tentacles=self.odds, duration=0.5)

        self.bloom.fade_all()

    def meteor_rotate(self):
        start = perf_counter()
        while perf_counter() - start < 60:
            for t in self.bloom.tentacles:
                color = Colors(self.colors[randrange(0, len(self.colors))])
                self.bloom.meteor(color, tentacles=[
                                  t], fade=15, duration=0.25)

        self.bloom.fade_all()

    def image(self, path):
        start = perf_counter()
        while perf_counter() - start < 60:
            self.bloom.image(path, duration=5)

        self.bloom.fade_all()

    def fade_even_and_odds(self):
        start = perf_counter()
        while perf_counter() - start < 60:
            c1 = Colors("Red")
            c2 = Colors("Blue")

            self.bloom.fade_multi(
                [c1.range_to(c2, 12), c2.range_to(c1, 12)], duration=8)
            self.bloom.fade_multi(
                [c2.range_to(c1, 12), c1.range_to(c2, 12)], duration=8)

        self.bloom.fade_all()

    def fade_cycle(self):
        colors = [
            ("OrangeRed", "SeaGreen"),
            ("DarkGreen", "Indigo"),
            ("MediumPurple", "White"),
            ("MediumBlue", "MediumVioletRed"),
            ("SaddleBrown", "Yellow"),
        ]
        start = perf_counter()
        while perf_counter() - start < 60:
            c1, c2 = colors[randrange(0, len(colors))]
            self.bloom.fade(Colors(c1).range_to(Colors(c2), 30), duration=12)
            self.bloom.fade(Colors(c2).range_to(Colors(c1), 30), duration=12)

        self.bloom.fade_all()
