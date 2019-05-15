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

        animates.swipe_and_stripe()

        animates.image("images/watermelon.jpg")

        animates.gradient_spin()

        animates.image("images/waves.jpg")

        animates.cycle_even_and_odds()

        animates.fast_drops()

        animates.shimmer_with_time()

        animates.image("images/circle_1.jpg")

        animates.speckle_even_and_odds()

        animates.shimmer_heartbeat()

        animates.image("images/circle_2.jpg")

        animates.meteors()

        animates.image("images/color_waves.jpg")

        animates.meteor_rotate()

        animates.fade_even_and_odds()

        animates.image("images/water.jpg")

        bloom.flicker(duration=60)

        bloom.fade_all()


if __name__ == '__main__':
    p = Process(target=main)
    p.start()
    p.join()
