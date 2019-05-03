#!/usr/bin/env python

from multiprocessing import Process

from bloom.bloom import LuminousBloom
from bloom.color import Colors

b = LuminousBloom()
b.swipe_blob(tentacles=[1, 3, 5])
b.swipe_blob(tentacles=[2, 4, 6], color=Colors("blue"))
b.swipe_blob(tentacles=[1, 3, 5])
# b.multi_swipe_up([1, 3, 5], (255, 0, 0))
# b.multi_swipe_up([2, 4, 6], (0, 255, 0))
# b.rainbow_rotate()
# b.swipe_up(1, (255, 255, 255))
# b.swipe_up(2, (255, 255, 255))
# b.swipe_up(3, (255, 255, 255))
# b.swipe_up(4, (255, 255, 255))
# b.swipe_up(5, (255, 255, 255))
# b.swipe_up(6, (255, 255, 255))


# def main():
#     x = 0
#     while True:
#         print(x)
#         x += 1


# if __name__ == '__main__':
#     p = Process(target=main)
#     p.start()
#     p.join()
