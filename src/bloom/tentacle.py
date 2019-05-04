#!/usr/bin/python


class Tentacle:
    __l = 64  # Pixel length

    def __init__(self, n):
        self.__n = n  # Tentacle number

        # Tentacle dimensions, each being 64 pixels in length
        self.__dims = {
            'start': (n * self.__l) - self.__l,
            'end': n * self.__l - 1
        }

    def __iter__(self):
        p = self.__dims['start']
        while p <= self.__dims['end']:
            yield p
            p += 1

    def which(self):
        return self.__n

    def dims(self):
        return (self.__dims['start'], self.__dims['end'])

    def set(self, pixels, red, green, blue):
        pixels[self.__dims['start']:self.__dims['end']] = [
            (red, green, blue) for _ in range(self.__l)]

        return pixels

    def get(self, pixels):
        return pixels[self.__dims['start']:self.__dims['end']]

    def contains(self, p):
        """ Returns True if a pixels exists within its dims """
        return self.__dims['start'] <= p <= self.__dims['end']
