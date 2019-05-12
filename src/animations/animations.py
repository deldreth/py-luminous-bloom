#!/usr/bin/env python

from random import randrange
from time import sleep, perf_counter

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

    def swipe_and_stripe(self, bloom, color1, color2, scale=4):
        for x in range(1, scale):
            color_range = list(color1.range_to(color2, 4 * x))
            bloom.swipe_blob(color1, tentacles=self.evens, duration=1)
            bloom.stripe(color_range, length=len(color_range), duration=5)
            bloom.swipe_blob(color1, tentacles=self.odds,
                             direction=Direction.DOWN, duration=1)

    def gradient_spin(self, bloom, color1, color2, scale=4):
        # Rotate each tentacle, coloring with a range and gradually increasing speed
        color_range = list(color1.range_to(color2, 64))
        for x in range(1, scale):
            bloom.rotate(color_range, duration=x * scale)

    def cycle_even_and_odds(self, bloom, color1, color2, scale=4):
        # Create a color range (length 63) between two colors
        # Cycle odd tentacles up and even tentcales down some number of "scale" times
        range_to = list(color1.range_to(color2, 32))
        colors = range_to + list(reversed(range_to[0:31]))

        for _ in range(scale):
            bloom.cycle(colors, tentacles=self.odds)
            bloom.cycle(colors, tentacles=self.evens, direction=Direction.DOWN)

    def fast_drop(self, bloom, color_list, duration=1):
        color = randrange(0, len(color_list))
        seed = randrange(0, 64)
        bloom.ripple(color_list[color], seed=seed,
                     duration=duration)

    def shimmer_with_time(self, bloom, color1, color2, color3):
        duration = 1

        def shimmer():
            bloom.shimmer_pulse(
                color1, tentacles=self.evens, duration=duration)
            bloom.shimmer_pulse(
                color2, tentacles=self.odds, duration=duration)

        for _ in range(6):
            shimmer()
            duration /= 2

        for _ in range(6):
            shimmer()
            duration *= 2

    def shimmer_heartbeat(self, bloom, color_list):
        for color in color_list:
            bloom.shimmer_pulse(color, duration=0.3)
            bloom.shimmer_pulse(color, duration=1.25)

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
