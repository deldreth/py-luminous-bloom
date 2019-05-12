#!/usr/bin/env python

import random
from multiprocessing import Process
from time import sleep, perf_counter

from bloom.bloom import LuminousBloom, Direction
from bloom.color import Colors
from animations.animations import Animations


def main():
    b = LuminousBloom()

    while True:
        animates = Animations()

        # b.flicker()

        # animates.swipe_and_stripe(b, Colors("Mediumpurple"), Colors("White"))

        # animates.gradient_spin(b, Colors("Mediumpurple"), Colors("White"))

        animates.cycle_even_and_odds(b, Colors("White"), Colors("Purple"))

        # animates.fast_drop(
        #     b, list(Colors("Goldenrod").range_to(Colors("MediumPurple"), 5)))

        # animates.shimmer_with_time(
        #     b, Colors("Goldenrod"), Colors("MediumPurple"), Colors("Seagreen"))

        # animates.shimmer_heartbeat(b, list(
        #     Colors("Seagreen").range_to(Colors("Deeppink"), 8)))


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
