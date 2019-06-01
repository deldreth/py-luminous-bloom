#!/usr/bin/env python

import opc
import random
import math
import types
from time import sleep, perf_counter

from .color import range_or_luminance, Colors
from .pattern import Pattern, Range
import bloom.direction as direction
import bloom.tentacle as tentacle
import bloom.image as Image

class Control(object):
    """
    Attributes:
        tentacles       A dict containing 1..6 instances of `bloom.tentacle`
        total_pixels    Total number of pixels. `bloom.tentacle.LENGTH * len(tentacles)`
    """
    tentacles = {
        1: tentacle.Tentacle(1),
        2: tentacle.Tentacle(2),
        3: tentacle.Tentacle(3),
        4: tentacle.Tentacle(4),
        5: tentacle.Tentacle(5),
        6: tentacle.Tentacle(6),
    }
    total_pixels = tentacle.LENGTH * len(tentacles)
    pixels = [(0, 0, 0) for x in range(total_pixels)]

    def __init__(self, client="localhost:7890"):
        self.client = opc.Client(client)
        self.write_pixels()

    def write_pixels(self, wait=0):
        """Utility method to use the opc client to write pixel state. This method direction calls `sleep`.

        Parameters
        ----------
        wait : number
            Number of seconds to wait before another write operation can continue.
        """
        self.client.put_pixels(self.pixels, 0)
        sleep(wait)

    def end_test(self):
        """Utility method to ensure the tentacle dim offsets are working as expected."""
        for t in self.tentacles:
            start, end = self.tentacles[t].dims()
            self.pixels[start] = Colors("purple").rgb
            self.pixels[end] = Colors("blue").rgb

            self.pixels[start+5] = Colors("purple").rgb
            self.pixels[end+5] = Colors("blue").rgb

        self.write_pixels()

    def rotate(self, color, loops=1, direction=direction.RIGHT, duration=10):
        """Iterate over the tentacles, writing a color to each one.

        Parameters
        ----------
        color : Colors|Range
            A color range or color. Luminance will be calculated in a range to a single color. 
        loops : integer
            Number of tentacle rotations to perform
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        color = range_or_luminance(color, 64)

        tentacles = list(self.tentacles.items())
        if direction is direction.LEFT:
            tentacles = list(reversed(tentacles))

        for _, tentacle in tentacles:
            self.pixels = [(0, 0, 0)] * self.total_pixels

            for ic, c in enumerate(color):
                start, _ = tentacle.dims()
                self.pixels[start + ic] = c

            self.write_pixels(duration / 120)

    def rotate_three(self, color, loops=1, direction=direction.RIGHT, duration=10):
        """Iterate over the tentacles and rotate colors on to every other tentacle, 
        stepping each iteration by 1.

        Parameters
        ----------
        color : Colors|Range
            A color range or color. Luminance will be calculated in a range to a single color. 
        loops : integer
            Number of tentacle rotations to perform
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        color = range_or_luminance(color, 64)

        evens = True
        for _ in range(0, len(self.tentacles)):
            for ti, t in self.tentacles.items():
                if evens and ti % 2 == 0:
                    self.pixels = t.patternize(self.pixels, color)
                elif not evens and ti % 2 != 0:
                    self.pixels = t.patternize(self.pixels, color)
                else:
                    self.pixels = t.colorize(self.pixels, (0, 0, 0))

            evens = not evens
            self.write_pixels(duration / 120)

    def swipe(self, color, tentacles=[1, 2, 3, 4, 5, 6], direction=direction.UP, duration=1):
        """Swipe a single color onto any tentacles in a direction. The color will persist.

        Parameters
        ----------
        color : Colors
            Any color
        tentacles : List(integers)
            A list of integers mapped to tentacle keys
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        rng = range(tentacle.LENGTH)

        if direction is direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for t in tentacles:
                start, _ = self.tentacles[t].dims()
                self.pixels[start + p] = color.rgb

            self.write_pixels(duration / 120)

    def swipe_blob(self, color, l=64, tentacles=[1, 2, 3, 4, 5, 6], direction=direction.UP, duration=1):
        """Swipe a range or luminance onto any tentacles in a direction. The color will fade.

        Parameters
        ----------
        color : Colors|Range
            A color range or color. If a single color then a degraded luminance will be calculated for the entire transition.
        l : integer
            Length of a color range, if provided.
        loops : integer
            Number of tentacle rotations to perform
        tentacles : List(integers)
            A list of integers mapped to tentacle keys
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        colors = range_or_luminance(color, l)

        rng = range(l * -1, tentacle.LENGTH + l)

        if direction is direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for i, c in enumerate(colors):
                if direction is direction.DOWN:
                    i *= -1

                for ti in tentacles:
                    t = self.tentacles[ti]
                    start, _ = t.dims()

                    pixel = start + p + i
                    if t.contains(pixel):
                        self.pixels[pixel] = c

            self.write_pixels(duration / 120)

    def swipe_pattern(self, color_or_range, tentacles=[1, 2, 3, 4, 5, 6], direction=direction.UP, duration=2):
        """Swipe a color or range as a pattern onto any number of tentacles.

        Parameters
        ----------
        color : Colors|Range
            A color range or colors.
        tentacles : List(integers)
            A list of integers mapped to tentacle keys
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        length = len(color_or_range)
        pattern = Pattern(length, color_or_range)

        rng = range(length * -1, tentacle.LENGTH + length)

        if direction is direction.DOWN:
            rng = reversed(rng)

        for p in rng:
            for i, c in enumerate(pattern):
                if direction is direction.DOWN:
                    i *= -1

                for ti in tentacles:
                    t = self.tentacles[ti]
                    start, _ = t.dims()

                    pixel = start + p + i
                    if t.contains(pixel):
                        self.pixels[pixel] = c

            self.write_pixels(duration / 120)

    def stripe(self, color_or_range, length=8, step=2, tentacles=[1, 2, 3, 4, 5, 6], direction=direction.UP, duration=1):
        """Patternize any tentacle with a color range separated by black of the same length

        Parameters
        ----------
        color_or_range : Colors|Range
            A color range or colors.
        length : integer
            The length of the stripe. If color_or_range is a range of colors then length must be equal to its length.
        step : integer
            The number of pixels to adjust the pattern during animation
        tentacles : List(integers)
            A list of integers mapped to tentacle keys
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        pattern = Pattern(length, color_or_range)

        if direction is direction.DOWN:
            step *= -1

        for _ in range(tentacle.LENGTH):
            for t in tentacles:
                self.pixels = self.tentacles[t].patternize(
                    self.pixels, pattern)

            pattern.rotate(step)

            self.write_pixels(duration / 120)

    def stripe_multi(self, list_of_ranges, length=8, step=2, tentacles=[[1, 3, 5], [2, 4, 6]], duration=1):
        """Patternize any tentacle with a color range separated by black of the same length. Multiple ranges can be applied seperately to specific lists of tentacles.

        Parameters
        ----------
        list_of_ranges : Colors|Range
            A color range or colors.
        length : integer
            The length of the stripe. If color_or_range is a range of colors then length must be equal to its length.
        step : integer
            he number of pixels to adjust the pattern during animation
        tentacles : List(List[integers])
            A list of integers mapped to tentacle keys
        direction : string
            One of `bloom.direction` constants
        duration : integer
            Sleep time `duration / 120`
        """
        pattern1 = Pattern(length, list_of_ranges[0])
        pattern2 = Pattern(length, list_of_ranges[1])

        for _ in range(tentacle.LENGTH):
            for t in tentacles[0]:
                self.pixels = self.tentacles[t].patternize(
                    self.pixels, pattern1)

            for t in tentacles[1]:
                self.pixels = self.tentacles[t].patternize(
                    self.pixels, pattern2)

            pattern1.rotate(step)
            pattern2.rotate(step)

            self.write_pixels(duration / 120)

    def fade(self, colors, tentacles=[1, 2, 3, 4, 5, 6], duration=1):
        """Fade any tentacle through a color range

        colors -- A range of colors
        """
        for c in colors:
            for t in tentacles:
                for p in self.tentacles[t]:
                    self.pixels[p] = c.rgb

            self.write_pixels(duration / 120)

    def fade_multi(self, colors, tentacles=[[1, 3, 5], [2, 4, 6]], duration=1):
        """
        fade_multi allows for multiple color generators to be traversed for any number of tentacles.

        The list of color generators and the list of tentacle lists must have the same length.
        colors -- List of lists containing color ranges [[Color, Color, Color, ...], [Color, Color, Color, ...]]
        tentacles -- List of lists containing tentacle maps [[Tentacle, Tentacle, Tentacle, ...], [Tentacle, Tentacle, Tentacle, ...]]
        """
        if len(colors) is not len(tentacles):
            raise Exception(
                'fade_multi: colors and tentacles should be lists of the same length')

        tentacle_colors = []
        color = None
        for ti, tlist in enumerate(tentacles):
            # generators cannot be rolled back, list() traverses the generator
            color = list(colors[ti])

            for t in tlist:
                tentacle_colors.append((self.tentacles[t], color))

        for x in range(len(color)):
            for t, color in tentacle_colors:
                self.pixels = t.colorize(self.pixels, color[x].rgb)

            self.write_pixels(duration / 60)

    def cycle(self, colors, tentacles=[1, 2, 3, 4, 5, 6], loops=1, direction=direction.UP, duration=1):
        """
        Cycle patternizes any tentacle with a range of colors. For the best results the length of the
        color range should be 64. However if the color range is less than 64, black will be appended
        to the end of the color range.
        """
        color_range = Range(colors)

        for _ in range(loops):
            for _ in range(tentacle.LENGTH):
                for t in tentacles:
                    self.pixels = self.tentacles[t].patternize(
                        self.pixels, color_range)

                color_range.rotate(-1 if direction is direction.DOWN else 1)

                self.write_pixels(duration / 120)

    def cycle_fade(self, colors, tentacles=[1, 2, 3, 4, 5, 6], loops=1, direction=direction.UP, duration=1):
        """Fades a color range onto a tentacle.

        Useful for animating color ranges blending into other color ranges.
        """
        # Transition the color range before the rotations
        for c, color in enumerate(Range(colors)):
            for t in tentacles:
                start, end = self.tentacles[t].dims()
                if direction is direction.DOWN:
                    self.pixels[end - 1 - c] = color
                else:
                    self.pixels[start + c] = color

            self.write_pixels(duration / 120)

        self.cycle(colors, tentacles, loops, direction, duration)

    def speckle(self, color, tentacles=[1, 2, 3, 4, 5, 6], maximum=5, storage={}, duration=5):
        """Randomly places pixels of a color on any tentacle up to a maximum
        """
        for t in tentacles:
            self.__speckle_helper(color, t, storage, maximum)

        self.write_pixels(duration / 120)

    def speckle_strobe(self, colors, tentacles=[1, 2, 3, 4, 5, 6], maximum=32, duration=5):
        """Randomly places pixels of a color range on any tentacle up to a maximum
        """
        color_range = list(colors)

        start_time = perf_counter()
        pixels = {}
        count = 0
        while perf_counter() - start_time < duration:
            if count >= len(color_range):
                count = 0

            color = color_range[count]

            for t in tentacles:
                self.__speckle_helper(color, t, pixels, maximum)

            count += 1

            self.write_pixels(duration / 120)

    def __speckle_helper(self, color, t, pixels_dict, maximum):
        """Map pixels from a speckle's pixel dictionary."""
        start, end = self.tentacles[t].dims()

        if t not in pixels_dict.keys():
            pixels_dict[t] = []

        pixels_dict[t].append(random.randint(start, end - 1))

        if len(pixels_dict[t]) >= maximum:
            self.pixels[pixels_dict[t].pop(0)] = (0, 0, 0)

        for p in pixels_dict[t]:
            self.pixels[p] = color.rgb

    def ripple(self, color, seed=32, tentacles=[1, 2, 3, 4, 5, 6], fade_out=0.75, duration=4):
        def wave(t, step, point, adjust):
            if step >= point:
                first = t.start + seed + step - point
                last = t.start + seed - step + point

                if t.contains(first):
                    self.pixels[first] = color.rgb

                if t.contains(last):
                    self.pixels[last] = color.rgb

                color.luminance = pow(fade_out, step)

        # Once the step is greater than point began to adjust
        def settle(t, step, reset, point):
            if step > point:
                first = t.start + seed + reset
                last = t.start + seed - reset

                if t.contains(first):
                    self.pixels[first] = (0, 0, 0)

                if t.contains(last):
                    self.pixels[last] = (0, 0, 0)

        time_start = perf_counter()
        step = 0
        reset = 0
        while perf_counter() - time_start < duration:
            for t in tentacles:
                wave(self.tentacles[t], step, 0, 0)
                wave(self.tentacles[t], step, 4, 2)
                settle(self.tentacles[t], step, reset, 11)

            if step > 11:
                reset += 1

            step += 1

            self.write_pixels(duration / 120)

    def shimmer_pulse(self, color, tentacles=[1, 2, 3, 4, 5, 6], fade_out=0.9, duration=4):
        def wave(t, step, point, adjust):
            seed = random.randint(0, 63)
            first = t.start + seed + step - point
            last = t.start + seed - step + point

            if t.contains(first):
                self.pixels[first] = color.rgb

            if t.contains(last):
                self.pixels[last] = color.rgb

            color.luminance = pow(fade_out, step)

        time_start = perf_counter()
        step = 0
        while perf_counter() - time_start <= duration:
            for t in tentacles:
                wave(self.tentacles[t], step, 0, 0)
                wave(self.tentacles[t], step, 4, 2)

            step += 1

            self.write_pixels(duration / 120)

    def flicker(self, cooling=150, sparking=120, tentacles=[1, 2, 3, 4, 5, 6], duration=10):
        def set_heat(pixel, temperature):
            scale = round((temperature/100)*200)
            heatramp = scale & 63
            heatramp <<= 2

            if scale > 128:
                # self.pixels[pixel] = (255, heatramp, 255)
                # self.pixels[pixel] = (heatramp, 255, 255)
                self.pixels[pixel] = (255, 255, heatramp)
            elif scale > 64:
                # self.pixels[pixel] = (heatramp, 255, 255)
                # self.pixels[pixel] = (255, 255, heatramp)
                self.pixels[pixel] = (255, heatramp, 0)
            else:
                # self.pixels[pixel] = (0, 0, heatramp)
                # self.pixels[pixel] = (0, heatramp, 0)
                self.pixels[pixel] = (heatramp, 0, 0)

        start_time = perf_counter()
        while perf_counter() - start_time < duration:
            heat = [x for x in reversed(range(0, 64))]

            for p in range(0, 64):
                cooldown = random.randrange(
                    0, round(((cooling * 10) / 64) + 2))
                if cooldown > heat[p]:
                    heat[p] = 0
                else:
                    heat[p] = heat[p] - cooldown

            for p in range(64 - 1, 1, -1):
                heat[p] = (heat[p - 1] + heat[p - 2] + heat[p - 2]) / 3

            if random.randrange(0, 255) < sparking:
                spark = random.randrange(0, 6)
                heat[spark] = heat[spark] + random.randrange(32, 64)

            for t in tentacles:
                start, _ = self.tentacles[t].dims()
                for p in range(0, 64):
                    set_heat(start + p, heat[p])

            self.write_pixels(1 / 5)

    def meteor(self, color, tentacles=[1, 2, 3, 4, 5, 6], fade=48, duration=1):
        size = 8

        for p in range(tentacle.LENGTH * 2):
            for t in tentacles:
                start, end = self.tentacles[t].dims()

                for pfade in range(start, end + 1):
                    if random.randrange(0, 10) > 5:
                        self.pixels[pfade] = self.__meteor_fade_helper(
                            pfade, fade)

                offset = start + p
                for j in range(size):
                    if offset - j <= end and offset - j >= start:
                        self.pixels[start + p - j] = color.rgb

            self.write_pixels(duration / 60)

    def __meteor_fade_helper(self, pixel, fade=8):
        r, g, b = self.pixels[pixel]
        r = 0 if r <= 10 else round(r - (r * fade / 256))
        g = 0 if g <= 10 else round(g - (g * fade / 256))
        b = 0 if b <= 10 else round(b - (b * fade / 256))

        return (r, g, b)

    def swipe_and_fade(self, color, tentacles=[1, 2, 3, 4, 5, 6]):
        for p in range(tentacle.LENGTH):
            for t in tentacles:
                start, _ = self.tentacles[t].dims()
                self.pixels[start + p] = color.rgb

            self.write_pixels(1 / 120)

        self.fade_all(tentacles)

    def fade_all(self, tentacles=[1, 2, 3, 4, 5, 6]):
        start_time = perf_counter()
        while perf_counter() - start_time < 4:
            for p in range(tentacle.LENGTH):
                for t in tentacles:
                    self.pixels[self.tentacles[t].start +
                                p] = self.__fader(self.tentacles[t].start + p)

            self.write_pixels(1 / 60)

    def __fader(self, pixel, fade=8):
        r, g, b = self.pixels[pixel]
        r = 0 if r <= 20 else round(r - (r * fade / 256))
        g = 0 if g <= 20 else round(g - (g * fade / 256))
        b = 0 if b <= 20 else round(b - (b * fade / 256))

        return (r, g, b)

    def image(self, path, tentacles=[1, 2, 3, 4, 5, 6], duration=1):
        image_lines = Image.get_lines(path)

        for line in image_lines:
            for t in tentacles:
                self.pixels = self.tentacles[t].patternize(self.pixels, line)

            self.write_pixels(duration / 120)

    @classmethod
    def __enseed(self, color_or_list, offset):
        if isinstance(color_or_list, list):
            return (self.tentacles[random.randint(1, 6)], offset, color_or_list[random.randrange(0, len(color_or_list))])
        else:
            return (self.tentacles[random.randint(1, 6)], offset, color_or_list)

    @classmethod
    def __tail_fade(self, pixel, length):
        r, g, b = pixel
        return (
            0 if r <= 20 else round(r - (r * length / 256)),
            0 if g <= 20 else round(g - (g * length / 256)),
            0 if b <= 20 else round(b - (b * length / 256))
        )

    def waterfall(self, color_or_list, highlight_lead=False, saturation=25, length=32, seconds=120):
        seeds = []

        def tail(t, pixel, length, color):
            start, end = t.dims()

            pixel_start = start + pixel
            if t.contains(pixel_start):
                self.pixels[pixel_start] = color.rgb

            for p in range(pixel_start, end):
                if t.contains(p) and t.contains(p + 1):
                    self.pixels[p +
                                1] = self.__tail_fade(self.pixels[p], length)

                if p < start:
                    self.pixels[start] = self.__tail_fade(
                        self.pixels[start], length)

        start_time = perf_counter()
        while perf_counter() - start_time < seconds:
            if random.randint(0, 100) > 100 - saturation:
                seeds.append(self.__enseed(color_or_list, 63 + length))

            for si, seed in enumerate(seeds):
                t, p, color = seed

                if p + length - 1 < 0:
                    seeds.pop(0)
                else:
                    tail(t, p, length, color)
                    seeds[si] = (t, p - 1, color)

                    if highlight_lead and t.contains(t.start + p):
                        self.pixels[t.start + p] = (255, 255, 255)

            self.write_pixels(1/60)

    def geyser(self, color_or_list, highlight_lead=False, saturation=25, length=32, seconds=120):
        seeds = []

        seeds.append(self.__enseed(color_or_list, 0 - length))

        def tail(t, pixel, length, color):
            start, end = t.dims()

            pixel_start = start + pixel
            if t.contains(pixel_start):
                self.pixels[pixel_start] = color.rgb

            for p in range(pixel_start - length, pixel_start):
                if t.contains(p - 1):
                    self.pixels[p -
                                1] = self.__tail_fade(self.pixels[p - 1], length)

                if p > end:
                    self.pixels[end] = self.__tail_fade(
                        self.pixels[end], length)

        start_time = perf_counter()
        while perf_counter() - start_time < seconds:
            if random.randint(0, 100) > 100 - saturation:
                seeds.append(self.__enseed(color_or_list, 0 - length))

            for si, seed in enumerate(seeds):
                t, p, color = seed

                if t.start + p > t.end + length:
                    seeds.pop(0)
                else:
                    tail(t, p, length, color)
                    seeds[si] = (t, p + 1, color)

                    if highlight_lead and t.contains(t.start + p + 1):
                        self.pixels[t.start + p + 1] = (255, 255, 255)

            self.write_pixels(1/60)
