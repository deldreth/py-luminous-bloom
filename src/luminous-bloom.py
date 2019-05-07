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


def animation_2(color1=Colors("Purple"), color2=(Colors("Lavender")), scale=5):
    # Rotate each tentacle, coloring with a range and gradually increasing speed
    color_range = list(color1.range_to(color2, 64))
    for x in range(1, scale):
        b.rotate(color_range, loops=x * scale, tsleep=1/10 / x)


def animation_3(color1=Colors("Purple"), color2=(Colors("Lavender")), scale=4):
    # Rotate each tentacle, coloring with a range and gradually increasing speed
    # Change direction on cycle index modulo 2
    color_range = list(color1.range_to(color2, 64))
    for x in range(1, scale):
        direction = Direction.RIGHT if x % 2 else Direction.LEFT
        b.rotate(color_range, loops=x * scale,
                 direction=direction, tsleep=1/10 / x)


def animation_4(color1, color2, scale=6):
    # Create a color range (length 64) between two colors
    # Cycle all tentacles of that color for "scale" times
    colors = list(color1.range_to(color2, 32)) + \
        list(color2.range_to(color1, 32))
    black = Colors("Black")

    for x in range(1, scale):
        b.cycle_fade(colors, loops=x, tsleep=1/120 / x)
        b.swipe(black, direction=Direction.DOWN, tsleep=1/60 / x)


if __name__ == '__main__':
    b = LuminousBloom()

    # animation_1()
    # animation_1(Colors("SeaGreen"))
    # animation_1(Colors("LavenderBlush"))
    # animation_1(Colors("Firebrick"), Colors("Goldenrod"))

    # animation_2()
    # animation_2(Colors("Firebrick"), Colors("Goldenrod"))
    # animation_2(Colors("Hotpink"), Colors("Deeppink"))

    # animation_3()

    # animation_4(Colors("Lavender"), Colors("Purple"))

    b.sparkle(Colors("Hotpink"))
    b.sparkle(Colors("SeaGreen"))
    b.sparkle(Colors("Purple"))
    b.sparkle(Colors("Goldenrod"))

    # b.cycle(Colors("Lavender").range_to(Colors("Purple"), 64))
    # b.cycle(Colors("Lavender").range_to(Colors("Purple"), 64))
    # b.cycle(Colors("Goldenrod").range_to(Colors("Hotpink"), 64))
    # b.cycle(Colors("Hotpink").range_to(Colors("SeaGreen"), 64))

    # b.swirl(length=2, step=7, color=Colors("red"), tsleep=1/10)

    # colors = Colors("purple").range_to(Colors("green"), 8)
    # b.stripe(color=list(colors))

    # b.swipe_blob(color=Colors("green"))

    # colors = [Colors(hex="#75DDDD"), Colors(hex="#84C7D0"), Colors(hex="#9297C4"),
    #           Colors(hex="#9C68B7"), Colors(hex="#AA3E98"), Colors(hex="#E0B8D9")]
    # for i, c in enumerate(colors):
    #     b.swipe_blob(l=64, color=c, tentacles=[i + 1], tsleep=1/512)

    # colors = list(Colors("red").range_to(Colors("blue"), 8))
    # b.swipe_pattern(colors)
    # b.swipe_pattern(colors, direction=Direction.DOWN)

    # for i, c in enumerate(colors):
    #     b.swipe_blob(l=64, color=c, tsleep=1/512)

    # b.swipe_blob(l=64, color=Colors("lavender"), tsleep=1/120)

    # b.rotate(Colors("lavender"))
    # b.rotate(Colors("lavender"), direction=Direction.LEFT)

    # b.rotate(list(Colors("red").range_to(Colors("blue"), 64)))

    # colors = Colors("red").range_to(Colors("blue"), 8)
    # b.fade(colors)

    # b.fade_multi(colors=[Colors("red").range_to(
    #     Colors("blue"), 8), Colors("blue").range_to(Colors("red"), 8)])

    # b.fade_multi(colors=[Colors("plum").range_to(
    #     Colors("turquoise"), 8), Colors("turquoise").range_to(Colors("black"), 8)], rotate=True, tsleep=1/15)

    # one_two = Colors("red").range_to(Colors("green"), 16)
    # three_four = Colors("green").range_to(Colors(web="blue"), 16)
    # five_six = Colors("blue").range_to(Colors("red"), 16)
    # b.fade_multi(colors=[one_two, three_four, five_six], tentacles=[
    #              [1, 2], [3, 4], [5, 6]], tsleep=1/15)

    # p = Process(target=main)
    # p.start()
    # p.join()
