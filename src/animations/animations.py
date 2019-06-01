#!/usr/bin/env python

from functools import wraps
from random import randrange
from time import perf_counter

from bloom import direction
from bloom.color import Colors

"""Default time for any animation. A few double this."""
time = 60

"""List of odd numbered tentacles"""
odds = [1, 3, 5]

"""List of even numbered tentacles"""
evens = [2, 4, 6]

"""Default color palette"""
colors = ["MediumBlue", "MediumSpringGreen", "Lime", "ForestGreen",
          "Turquoise", "MidnightBlue", "DarkGreen", "Indigo", "BlueViolet",
          "MediumVioletRed", "Aquamarine", "Magenta", "DeepPink",
          "HotPink", "FireBrick", "SaddleBrown", "DarkGoldenrod",
          "OrangeRed", "DarkOrange", "Gold", "SeaGreen", "DarkBlue"]
num_colors = len(colors)


def random_color(previous_color):
    """With any available color, ensure that a different random color is returned"""
    next_color = previous_color

    while next_color is not previous_color:
        next_color = colors[randrange(0, num_colors)]

    return next_color


def swipe_and_stripe(bloom):
    c = [
        (Colors("OrangeRed"), Colors("SeaGreen")),
        (Colors("DarkGreen"), Colors("Indigo")),
        (Colors("MediumPurple"), Colors("White")),
        (Colors("MediumBlue"), Colors("MediumVioletRed")),
        (Colors("SaddleBrown"), Colors("Yellow")),
    ]

    start = perf_counter()
    while perf_counter() - start < time * 2:
        color1, color2 = c[randrange(0, num_colors)]

        for x in range(1, 3):
            color_range = list(color1.range_to(color2, 4 * x))
            bloom.swipe_blob(color1, duration=1)
            for d in range(10, 4, -1):
                bloom.stripe(color_range, length=len(
                    color_range), duration=d)

    bloom.fade_all()


def swipe_multi_increment(bloom):
    range1 = list(Colors("Red").range_to(Colors("Blue"), 8))
    range2 = list(reversed(range1))

    start = perf_counter()
    while perf_counter() - start < 30:
        bloom.stripe_multi([range1, range2], duration=5)


def gradient_spin(bloom):
    start = perf_counter()
    while perf_counter() - start < time / 2:
        color1 = colors[randrange(0, num_colors)]
        color2 = colors[randrange(0, num_colors)]
        color_range = list(Colors(color1).range_to(Colors(color2), 64))
        for x in range(1, 5):
            bloom.rotate(color_range, duration=x * 3)


def gradient_spin_three(bloom):
    start = perf_counter()
    while perf_counter() - start < time / 2:
        color1 = colors[randrange(0, num_colors)]
        color2 = colors[randrange(0, num_colors)]
        color_range = list(Colors(color1).range_to(Colors(color2), 64))

        for d in range(15, 5, -1):
            bloom.rotate_three(color_range, duration=d)


def cycle_even_and_odds(bloom):
    c = [
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
    while perf_counter() - start < time:
        c1, c2 = c[count]
        range_to = list(c1.range_to(c2, 32))
        color_list = range_to + list(reversed(range_to[0:31]))

        for _ in range(5):
            bloom.cycle(color_list, tentacles=odds)
            bloom.cycle(color_list, tentacles=evens,
                        direction=direction.DOWN)

        count += 1

        if count > num_colors - 1:
            count = 0

    bloom.fade_all()


def cycle_all(bloom):
    c = [
        (Colors("Indigo"), Colors("BlueViolet")),
        (Colors("MediumPurple"), Colors("Seagreen")),
        (Colors("SeaGreen"), Colors("OrangeRed")),
        (Colors("OrangeRed"), Colors("Gold")),
        (Colors("Gold"), Colors("MediumBlue")),
        (Colors("MediumBlue"), Colors("MidnightBlue")),
    ]

    start = perf_counter()
    while perf_counter() - start < time:
        c1, c2 = c[randrange(0, num_colors)]
        range_to = list(c1.range_to(c2, 32))
        color_list = range_to + list(reversed(range_to[0:31]))

        for _ in range(10):
            bloom.cycle(color_list, duration=2)

    bloom.fade_all()


def fast_drops(bloom):
    start = perf_counter()
    while perf_counter() - start < time:
        color = Colors(colors[randrange(0, num_colors)])
        seed = randrange(0, 64)
        bloom.ripple(color, seed=seed, fade_out=0.88, duration=1.75)


def shimmer_with_time(bloom):
    def shimmer(c1, c2, duration):
        bloom.shimmer_pulse(
            c1, tentacles=evens, duration=duration)
        bloom.shimmer_pulse(
            c2, tentacles=odds, duration=duration)

    start = perf_counter()
    while perf_counter() - start < time:
        c1 = Colors(colors[randrange(0, num_colors)])
        c2 = Colors(colors[randrange(0, num_colors)])

        for _ in range(10):
            shimmer(c1, c2, 0.25)

    bloom.fade_all()


def shimmer_heartbeat(bloom):
    c = [
        Colors("Seagreen").range_to(Colors("Deeppink"), 8)
    ]

    count = 0
    start = perf_counter()
    while perf_counter() - start < time:
        for color in c[count]:
            bloom.shimmer_pulse(color, duration=0.3)
            bloom.shimmer_pulse(color, duration=1.25)

        count += 1

        if count > num_colors - 1:
            count = 0

    bloom.fade_all()


def speckle_even_and_odds(bloom):
    start = perf_counter()
    storage = {}
    while perf_counter() - start < time:
        c1 = Colors(colors[randrange(0, num_colors)])
        c2 = Colors(colors[randrange(0, num_colors)])

        bloom.speckle(c1, tentacles=evens,
                      maximum=16, storage=storage, duration=10)
        bloom.speckle(c2, tentacles=odds, storage=storage)

    bloom.fade_all()


def meteors(bloom):
    start = perf_counter()
    while perf_counter() - start < time:
        color = colors[randrange(0, num_colors)]
        bloom.meteor(Colors(color), duration=2)

        color = colors[randrange(0, num_colors)]
        bloom.meteor(
            Colors(color), tentacles=evens, duration=0.5)

        color = colors[randrange(0, num_colors)]
        bloom.meteor(Colors(color), tentacles=odds, duration=0.5)

    bloom.fade_all()


def meteor_rotate(bloom):
    start = perf_counter()
    while perf_counter() - start < time:
        for _ in bloom.tentacles:
            color = Colors(colors[randrange(0, num_colors)])
            bloom.meteor(color, tentacles=evens,
                         fade=8, duration=0.10)

            color = Colors(colors[randrange(0, num_colors)])
            bloom.meteor(color, tentacles=odds,
                         fade=8, duration=0.15)

    bloom.fade_all()


def image(bloom, path):
    start = perf_counter()
    while perf_counter() - start < time:
        bloom.image(path, duration=5)

    bloom.fade_all()


def fade_even_and_odds(bloom):
    start = perf_counter()
    while perf_counter() - start < time:
        c1 = Colors("Red")
        c2 = Colors("Blue")

        bloom.fade_multi(
            [c1.range_to(c2, 12), c2.range_to(c1, 12)], duration=8)
        bloom.fade_multi(
            [c2.range_to(c1, 12), c1.range_to(c2, 12)], duration=8)

    bloom.fade_all()


def fade_cycle(bloom):
    c = [
        ("OrangeRed", "SeaGreen"),
        ("DarkGreen", "Indigo"),
        ("MediumPurple", "White"),
        ("MediumBlue", "MediumVioletRed"),
        ("SaddleBrown", "Yellow"),
    ]
    start = perf_counter()
    while perf_counter() - start < time:
        c1, c2 = c[randrange(0, num_colors)]
        bloom.fade(Colors(c1).range_to(Colors(c2), 30), duration=12)
        bloom.fade(Colors(c2).range_to(Colors(c1), 30), duration=12)

    bloom.fade_all()


def waterfall(bloom, highlight=False):
    color = Colors(colors[randrange(0, num_colors)])
    bloom.waterfall(color, highlight, seconds=time)
    bloom.fade_all()


def shower(bloom, highlight=False):
    color = Colors(colors[randrange(0, num_colors)])
    bloom.waterfall(
        color, highlight, saturation=99, seconds=time)
    bloom.fade_all()


def waterfall_rainbow(bloom):
    bloom.waterfall([Colors(x) for x in colors], seconds=time)
    bloom.fade_all()


def geyser(bloom, highlight=False):
    color = Colors(colors[randrange(0, num_colors)])
    bloom.geyser(color, highlight, seconds=time)
    bloom.fade_all()


def gusher(bloom, highlight=False):
    color = Colors(colors[randrange(0, num_colors)])
    bloom.geyser(color, highlight, saturation=99, seconds=time)
    bloom.fade_all()


def flicker(bloom):
    bloom.flicker(duration=60)
    bloom.fade_all()
