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
# def main():
#     x = 0
#     while True:
#         print(x)
#         x += 1


if __name__ == '__main__':
    # p = Process(target=main)
    # p.start()
    # p.join()

    b = LuminousBloom()

    colors = Colors("blue").range_to(Colors("purple"), 8)
    # b.stripe(color=list(colors))
    b.swirl(color=Colors("white"))
