#!/usr/bin/env python

from random import randint

from bloom.bloom import LuminousBloom
from animations.animations import Animations

bloom = LuminousBloom()
animates = Animations(bloom)

while True:
    animates.image("images/color_waves.jpg")

    animates.cycle_all()

    animates.image("images/watermelon.jpg")

    animates.swipe_and_stripe()

    animates.image("images/circle_1.jpg")

    animates.gradient_spin()

    animates.image("images/circles/{}.jpg".format(randint(1, 8)))

    animates.cycle_even_and_odds()

    animates.speckle_even_and_odds()

    animates.image("images/waves.jpg")

    animates.fast_drops()

    animates.image("images/water.jpg")

    animates.shimmer_with_time()

    animates.fade_cycle()

    animates.shimmer_heartbeat()

    animates.meteors()

    animates.meteor_rotate()

    animates.fade_even_and_odds()

    bloom.flicker(duration=60)

    bloom.fade_all()
