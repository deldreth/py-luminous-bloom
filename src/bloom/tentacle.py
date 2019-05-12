#!/usr/bin/python


class Tentacle:
    __l = 64  # Pixel length

    def __init__(self, n):
        self.__n = n  # Tentacle number

        # Tentacle dimensions, each being 64 pixels in length
        self.start = (n * self.__l) - self.__l
        self.end = n * self.__l - 1

    def __iter__(self):
        p = self.start
        while p <= self.end:
            yield p
            p += 1

    def __repr__(self):
        return "<Tentacle {}>".format(self.__n)

    def which(self):
        return self.__n

    def dims(self):
        return (self.start, self.end)

    def set(self, pixels, red, green, blue):
        pixels[self.start:self.end] = [
            (red, green, blue) for _ in range(self.__l)]

        return pixels

    def colorize(self, pixels, rgb):
        for ic in range(self.__l):
            if self.contains(self.start + ic):
                pixels[self.start + ic] = rgb
        return pixels

    def patternize(self, pixels, colors):
        for ic, c in enumerate(colors):
            if self.contains(self.start + ic):
                pixels[self.start + ic] = c
        return pixels

    def set_pattern(self, pixels, pattern):
        # pixels[self.start:self.end] = [pattern[p] for p in range(self.__l)]
        for p, item in enumerate(range(self.start, self.end)):
            pixels[item] = pattern[p]
        return pixels

    def get(self, pixels):
        return pixels[self.start:self.end]

    def contains(self, p):
        """ Returns True if a pixels exists within its dims """
        return self.start <= p < self.end
