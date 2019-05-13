#!/usr/bin/env python

import random
from multiprocessing import Process
from time import perf_counter

from bloom.bloom import LuminousBloom, Direction
from bloom.color import Colors
from animations.animations import Animations


def main():
    bloom = LuminousBloom()
    animates = Animations(bloom)

    while True:
        animates.swipe_and_stripe(bloom, Colors(
            "Mediumpurple"), Colors("White"))

        # animates.gradient_spin(b, Colors("Mediumpurple"), Colors("White"))

        # animates.cycle_even_and_odds()

        # animates.fast_drops()

        # animates.shimmer_with_time()

        # animates.speckle_even_and_odds()

        # animates.speckle_all_unique()

        # animates.shimmer_heartbeat()

        # animates.meteors()

        # animates.meteor_rotate()


if __name__ == '__main__':
    p = Process(target=main)
    p.start()
    p.join()

    # b.swipe(Colors("Seagreen"))
    # b.swipe_blob(Colors("Goldenrod"))
    # b.swipe_pattern(
    #     list(Colors("MediumPurple").range_to(Colors("Hotpink"), 8)))
    # b.swipe_pattern(
    #     list(Colors("MediumPurple").range_to(Colors("Hotpink"), 8)))
    # b.stripe(list(Colors("MediumPurple").range_to(
    # Colors("Hotpink"), 8)), duration=5)
    # b.fade(Colors("Firebrick").range_to(Colors("Deeppink"), 64))
    # b.fade_multi(colors=[Colors("red").range_to(
    #     Colors("blue"), 64), Colors("blue").range_to(Colors("red"), 64)])
    # b.cycle(list(Colors("Red").range_to(Colors("Blue"), 32)) +
    #         list(Colors("Blue").range_to(Colors("Red"), 32)), loops=20)
    # b.cycle(Colors("Lavender").range_to(Colors("Purple"), 64))
    # b.cycle(Colors("Lavender").range_to(Colors("Purple"), 64))
    # b.cycle(Colors("Goldenrod").range_to(Colors("Hotpink"), 64))
    # b.cycle(Colors("Hotpink").range_to(
    #     Colors("SeaGreen"), 64), loops=10, duration=5)
    # b.cycle(list(Colors("Hotpink").range_to(
    #     Colors("SeaGreen"), 32)) + list(Colors("Seagreen").range_to(Colors("Hotpink"), 32)), loops=10, duration=1)
    # b.speckle_strobe(Colors("Mediumpurple").range_to(Colors("Hotpink"), 10))
    # b.ripple(Colors("Seagreen"))

    # b.swirl(length=2, step=7, color=Colors("red"), tsleep=1/10)
