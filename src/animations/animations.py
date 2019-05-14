#!/usr/bin/env python

from random import randrange
from time import perf_counter

from bloom.bloom import LuminousBloom, Direction
from bloom.color import Colors

# Greens
# Seagreen

# Purples
# Mediumpurple, Lavenderblush

# Pinks...
# Hotpink, Deeppink

# Oranges
# Firebrick, Goldenrod


class Animations():
    evens = [1, 3, 5]
    odds = [2, 4, 6]
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
        while perf_counter() - start < 60:
            color1, color2 = colors[randrange(0, len(colors))]

            for x in range(1, 4):
                color_range = list(color1.range_to(color2, 4 * x))
                self.bloom.swipe_blob(color1, duration=1)
                self.bloom.stripe(color_range, length=len(
                    color_range), duration=10)

    def gradient_spin(self, bloom, color1, color2, scale=4):
        # Rotate each tentacle, coloring with a range and gradually increasing speed
        color_range = list(color1.range_to(color2, 64))
        for x in range(1, scale):
            bloom.rotate(color_range, duration=x * scale)

    def cycle_even_and_odds(self):
        # Create a color range (length 63) between two colors
        # Cycle odd tentacles up and even tentcales down some number of "scale" times

        colors = [
            (Colors("White"), Colors("Purple")),
            (Colors("Firebrick"), Colors("Seagreen")),
            (Colors("Black"), Colors("Hotpink")),
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

    def fast_drops(self):
        colors = [
            Colors("Purple"),
            Colors("Firebrick"),
            Colors("Seagreen"),
            Colors("Hotpink"),
            Colors("Goldenrod")
        ]

        count = 0
        start = perf_counter()
        while perf_counter() - start < 60:
            c1 = randrange(0, len(colors))
            c2 = randrange(0, len(colors))

            color_list = list(colors[c1].range_to(colors[c2], 8))
            color = randrange(0, 8)
            seed = randrange(0, 64)
            self.bloom.ripple(color_list[color], seed=seed, duration=0.75)

            count += 1

            if count > len(colors) - 1:
                count = 0

    def shimmer_with_time(self):
        duration = 1

        colors = [
            (Colors("Goldenrod"), Colors("MediumPurple")),
            (Colors("Deeppink"), Colors("Seagreen")),
        ]

        def shimmer(c1, c2):
            self.bloom.shimmer_pulse(
                c1, tentacles=self.evens, duration=duration)
            self.bloom.shimmer_pulse(
                c2, tentacles=self.odds, duration=duration)

        count = 0
        start = perf_counter()
        while perf_counter() - start < 60:
            c1, c2 = colors[count]

            for _ in range(6):
                shimmer(c1, c2)
                duration /= 2

            for _ in range(6):
                shimmer(c1, c2)
                duration *= 2

            count += 1

            if count > len(colors) - 1:
                count = 0

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

    def speckle_even_and_odds(self):
        colors = [
            (Colors("Deeppink"), Colors("Seagreen")),
        ]

        count = 0
        start = perf_counter()
        storage = {}
        while perf_counter() - start < 60:
            c1, c2 = colors[count]

            self.bloom.speckle(c1, tentacles=self.evens, storage=storage)
            self.bloom.speckle(c2, tentacles=self.odds, storage=storage)

            count += 1

            if count > len(colors) - 1:
                count = 0

    def speckle_all_unique(self):
        colors = [
            [Colors("Deeppink"), Colors("Seagreen"), Colors(
                "RoyalBlue"), Colors("YellowGreen"), Colors("BlueViolet"), Colors("Tomato")]
        ]

        count = 0
        start = perf_counter()
        storage = {}
        while perf_counter() - start < 60:
            color_list = colors[count]

            for i, color in enumerate(color_list):
                self.bloom.speckle(color, tentacles=[i + 1], storage=storage)

            count += 1

            if count > len(colors) - 1:
                count = 0

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

    def meteor_rotate(self):
        start = perf_counter()
        while perf_counter() - start < 60:
            for t in self.bloom.tentacles:
                color = Colors(self.colors[randrange(0, len(self.colors))])
                self.bloom.meteor(color, tentacles=[
                                  t], fade=15, duration=0.25)

    # def animation_9(self, bloom):
    #     colors = list(Colors("Hotpink").range_to(Colors("Black"), 32)) + \
    #         list(Colors("Black").range_to(Colors("Hotpink"), 32))

    #     start_time = perf_counter()
    #     while perf_counter() - start_time < 60:
    #         bloom.cycle(colors, loops=2, duration=5)

    # def animation_10(self, bloom):
    #     color_range = list(Colors("Hotpink").range_to(Colors("Seagreen"), 8))

    #     start_time = perf_counter()
    #     while perf_counter() - start_time < 60:
    #         bloom.stripe(color_range, length=len(color_range), duration=5)
