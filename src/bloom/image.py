#!/usr/bin/env python

from collections import deque
from os import path
from PIL import Image as PILImage


class Image():
    def get_lines(self, image_path):
        img = PILImage.open(path.abspath(image_path))
        img = img.resize((64, 64))

        return self.__pixelize([img])

    def __pixelize(self, images):
        """ Returns a list of pixel data """
        lines = []
        for img in images:
            pixels = img.load()
            for y in range(img.size[1]):
                xs = []
                for x in range(img.size[0]):
                    xs.append(pixels[x, y])

                lines.append(xs)
                del xs

        del images

        return lines
