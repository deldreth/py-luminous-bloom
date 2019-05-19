#!/usr/bin/env python

from random import randint, randrange

from bloom.bloom import LuminousBloom
from animations.animations import Animations

bloom = LuminousBloom()
animates = Animations(bloom)

animations = [
    (animates.swipe_and_stripe, None),
    (animates.swipe_multi_increment, None),
    (animates.cycle_all, None),
    (animates.cycle_even_and_odds, None),
    (animates.fade_cycle, None),
    (animates.fade_even_and_odds, None),
    (animates.gradient_spin, None),
    (animates.gradient_spin_three, None),
    (animates.speckle_even_and_odds, None),
    (animates.fast_drops, None),
    (animates.shimmer_with_time, None),
    (animates.shimmer_heartbeat, None),
    (animates.meteors, None),
    (animates.meteor_rotate, None),
    (animates.waterfall, None),
    (animates.waterfall, True),
    (animates.waterfall_rainbow, None),
    (animates.gusher, None),
    (animates.gusher, True),
    (animates.shower, None),
    (animates.shower, True),
    (animates.flicker, None),
    (animates.image, "images/lantern.jpg"),
    (animates.image, "images/water.jpg"),
    (animates.image, "images/waves.jpg"),
    (animates.image, "images/color_waves.jpg"),
    (animates.image, "images/watermelon.jpg"),
    (animates.image, "images/circle_1.jpg"),
    (animates.image, lambda: "images/circles/{}.jpg".format(randint(1, 8))),
    (animates.image, lambda: "images/diamonds/diamond_{}.jpg".format(randint(1, 2))),
    (animates.image, lambda: "images/bounces/bounces_{}.jpg".format(randint(1, 4))),
    (animates.image, lambda: "images/holes/hole_{}.jpg".format(randint(1, 4)))
]

print("Starting for {} animations.".format(len(animations)))

while True:
    func, args = animations[randrange(0, len(animations))]

    if callable(args):
        func(args())
    elif args is not None:
        func(args)
    else:
        func()
