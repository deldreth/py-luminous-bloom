#!/usr/bin/env python

from random import randint, randrange

from bloom.control import Control
import animations.animations as animations

all_animations = [
    (animations.swipe_and_stripe, None),
    (animations.swipe_multi_increment, None),
    (animations.cycle_all, None),
    (animations.cycle_even_and_odds, None),
    (animations.fade_cycle, None),
    (animations.fade_even_and_odds, None),
    (animations.gradient_spin, None),
    (animations.gradient_spin_three, None),
    (animations.speckle_even_and_odds, None),
    (animations.fast_drops, None),
    (animations.shimmer_with_time, None),
    (animations.shimmer_heartbeat, None),
    (animations.meteors, None),
    (animations.meteor_rotate, None),
    (animations.waterfall, None),
    (animations.waterfall, True),
    (animations.waterfall_rainbow, None),
    (animations.gusher, None),
    (animations.gusher, True),
    (animations.shower, None),
    (animations.shower, True),
    (animations.flicker, None),
    (animations.image, "images/water.jpg"),
    (animations.image, "images/waves.jpg"),
    (animations.image, "images/color_waves.jpg"),
    (animations.image, "images/watermelon.jpg"),
    (animations.image, "images/circle_1.jpg"),
    (animations.image, lambda: "images/lanterns/lantern_{}.jpg".format(randint(1, 3))),
    (animations.image, lambda: "images/flares/flare_{}.jpg".format(randint(1, 3))),
    (animations.image, lambda: "images/circles/{}.jpg".format(randint(1, 8))),
    (animations.image, lambda: "images/diamonds/diamond_{}.jpg".format(randint(1, 2))),
    (animations.image, lambda: "images/bounces/bounces_{}.jpg".format(randint(1, 4))),
    (animations.image, lambda: "images/holes/hole_{}.jpg".format(randint(1, 4)))
]

print("Starting for {} animations.".format(len(all_animations)))

previous = []


def pick_animation():
    index = randrange(0, len(all_animations))
    if index in previous:
        return pick_animation()

    previous.append(index)
    return all_animations[index]

bloom = Control()

while True:
    func, args = pick_animation()

    if callable(args):
        func(bloom, args())
    elif args is not None:
        func(bloom, args)
    else:
        func(bloom)

    if len(previous) == len(all_animations):
        previous = []
