#!/usr/bin/env python

from random import randint

from bloom.bloom import LuminousBloom
from animations.animations import Animations
from bloom.color import Colors

bloom = LuminousBloom()
animates = Animations(bloom)

while True:
    animates.shower()

    animates.image("images/bounces/bounces_{}.jpg".format(randint(1, 4)))

    animates.swipe_multi_increment()

    animates.image("images/color_waves.jpg")

    animates.cycle_all()

    animates.image("images/watermelon.jpg")

    animates.swipe_and_stripe()

    animates.image("images/circle_1.jpg")

    animates.gradient_spin()

    animates.image("images/circles/{}.jpg".format(randint(1, 8)))

    animates.cycle_even_and_odds()

    animates.image("images/diamonds/diamond_{}.jpg".format(randint(1, 2)))

    animates.speckle_even_and_odds()

    animates.image("images/waves.jpg")

    animates.fast_drops()

    animates.image("images/water.jpg")

    animates.shimmer_with_time()

    animates.waterfall_rainbow()

    animates.fade_cycle()

    animates.image("images/lantern.jpg")

    animates.shimmer_heartbeat()

    animates.gradient_spin_three()

    animates.image("images/holes/hole_{}.jpg".format(randint(1, 4)))

    animates.meteors()

    animates.meteor_rotate()

    animates.fade_even_and_odds()

    animates.waterfall()

    bloom.flicker(duration=60)

    bloom.fade_all()
