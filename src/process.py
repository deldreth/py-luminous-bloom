#!/usr/bin/env python

from multiprocessing import Process

from bloom.bloom import LuminousBloom
from animations.animations import Animations


def main():
    bloom = LuminousBloom()
    animates = Animations(bloom)

    while True:
        animates.image("images/color_waves.jpg")

        animates.cycle_all()

        animates.image("images/watermelon.jpg")

        animates.swipe_and_stripe()

        animates.image("images/circle_1.jpg")

        animates.gradient_spin()

        animates.image("images/circle_2.jpg")

        animates.cycle_even_and_odds()

        animates.image("images/waves.jpg")

        animates.fast_drops()

        animates.image("images/water.jpg")

        animates.shimmer_with_time()

        animates.speckle_even_and_odds()

        animates.shimmer_heartbeat()

        animates.meteors()

        animates.meteor_rotate()

        animates.fade_even_and_odds()

        bloom.flicker(duration=60)

        bloom.fade_all()


if __name__ == '__main__':
    p = Process(target=main)
    p.start()
    p.join()
