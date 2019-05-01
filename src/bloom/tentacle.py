#!/usr/bin/python


class Tentacle:
    __l = 64

    def __init__(self, n, p):
        self.__n = n  # Tentacle number

        # Tentacle dimensions, each being 64 pixels in length
        self.__dims = {
            'start': (n * self.__l) - self.__l,
            'end': n * self.__l
        }

    def __iter__(self):
        p = self.__dims['start']
        while p < self.__dims['end']:
            yield p
            p += 1

    def which(self):
        return self.__n

    def dim(self):
        return self.__dims

    def set(self, pixels, red, green, blue):
        pixels[self.__dims['start']:self.__dims['end']] = [
            (red, green, blue) for x in range(self.__l)]

        return pixels
