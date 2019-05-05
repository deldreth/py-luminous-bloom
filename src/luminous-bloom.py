#!/usr/bin/env python

import random
from multiprocessing import Process

from bloom.bloom import LuminousBloom, Direction
from bloom.color import Colors

# for r in range(6):
#     b.swipe_blob(l=8, tentacles=[r + 1], tsleep=0.01, color=colors[r % 3])
#     b.swipe_blob(
#         tentacles=[r + 1], color=colors[r % 3],
#         tsleep=0, direction=Direction.DOWN)

# b.swipe_blob(tentacles=[1, 3, 5], direction=Direction.DOWN)
# b.swipe_blob(tentacles=[2, 4, 6], direction=Direction.UP)

# red = Colors("purple")
# orange = Colors("orange")
# colors = list(red.range_to(orange, 50))

# for r in range(50):
#     b.swipe_blob(tsleep=0.001, color=colors[r])
# b.swipe_blob(tentacles=[1, 2], tsleep=0.001)
# b.swipe_blob(tentacles=[2, 3], tsleep=0.001)
# b.swipe_blob(tentacles=[3, 4], tsleep=0.001)
# b.swipe_blob(tentacles=[4, 5], tsleep=0.001)
# b.swipe_blob(tentacles=[5, 6], tsleep=0.001)
# b.swipe_blob(tentacles=[6, 1], tsleep=0.001)

# for c in Colors("blue").range_to(Colors("white"), 64):
#     b.swipe_blob(l=64, tsleep=0, color=c)

# colors = list(Colors("blue").range_to(Colors("white"), 64))
# b.swipe_blob(l=len(colors), tsleep=0.01, color=colors)
# b.swipe_blob(l=len(colors), tsleep=0.01, color=colors)
# b.swipe_blob(l=len(colors), tsleep=0.01, color=colors)


# b.swipe_blob(tentacles=[2, 4, 6], color=Colors("blue"))
# b.swipe([1, 3, 5], Colors("red"))
# b.swipe([2, 4, 6], Colors("blue"), Direction.DOWN)
# b.rainbow_rotate()

# Process example
def main():
    b = LuminousBloom()

    while True:
        purple_to_white = list(Colors("purple").range_to(
            Colors("white"), 4)) + list(Colors("white").range_to(Colors("purple"), 4))
        b.stripe(loops=64, length=8, color=list(purple_to_white), tsleep=2/120)

        b.swipe_blob(color=Colors("purple"))

        colors = Colors("purple").range_to(Colors("green"), 8)
        b.stripe(color=list(colors))

        b.swipe_blob(color=Colors("green"))


def animation_1(color1=Colors("MediumPurple"), color2=Colors("White"), scale=4):
    # Animation 1: Color(n) to White
    for x in range(1, scale):
        l = 4 * x
        range_to = list(color1.range_to(color2, l))

        b.swipe_blob(color1, tentacles=[1, 3, 5])

        b.stripe(loops=64, length=l,
                 color=range_to, tsleep=1 / 60 / x)

        b.swipe_blob(color1, tentacles=[
            2, 4, 6], direction=Direction.DOWN)


if __name__ == '__main__':
    b = LuminousBloom()

    # animation_1()
    # animation_1(Colors("SeaGreen"))
    # animation_1(Colors("LavenderBlush"))

    colors = Colors("purple").range_to(Colors("green"), 8)
    b.stripe(color=list(colors))

    b.swipe_blob(color=Colors("green"))

    colors = [Colors(hex="#75DDDD"), Colors(hex="#84C7D0"), Colors(hex="#9297C4"),
              Colors(hex="#9C68B7"), Colors(hex="#AA3E98"), Colors(hex="#E0B8D9")]
    for i, c in enumerate(colors):
        b.swipe_blob(l=64, color=c, tentacles=[i + 1], tsleep=1/512)

    colors = list(Colors("red").range_to(Colors("blue"), 8))
    b.swipe_pattern(colors)
    b.swipe_pattern(colors, direction=Direction.DOWN)

    for i, c in enumerate(colors):
        b.swipe_blob(l=64, color=c, tsleep=1/512)

    b.swipe_blob(l=64, color=Colors("lavender"), tsleep=1/120)

    b.rotate(Colors("lavender"))
    b.rotate(Colors("lavender"), direction=Direction.LEFT)

    b.rotate(list(Colors("red").range_to(Colors("blue"), 64)))

    b.swirl(length=2, step=7, color=Colors("red"), tsleep=1/10)

    colors = Colors("red").range_to(Colors("blue"), 8)
    b.fade(colors)

    b.fade_multi(colors=[Colors("red").range_to(
        Colors("blue"), 8), Colors("blue").range_to(Colors("red"), 8)])

    b.fade_multi(colors=[Colors("plum").range_to(
        Colors("turquoise"), 8), Colors("turquoise").range_to(Colors("black"), 8)], rotate=True, tsleep=1/15)

    one_two = Colors("red").range_to(Colors("green"), 16)
    three_four = Colors("green").range_to(Colors(web="blue"), 16)
    five_six = Colors("blue").range_to(Colors("red"), 16)
    b.fade_multi(colors=[one_two, three_four, five_six], tentacles=[
                 [1, 2], [3, 4], [5, 6]], tsleep=1/15)

    # p = Process(target=main)
    # p.start()
    # p.join()
