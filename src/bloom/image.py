"""
Utility submodule for scanning images. The pixel arrays returned by `get_lines`
can be traversed and written to pixels by :func:`~bloom.control.Control.image`.
"""

from collections import deque
from os import path
from PIL import Image as PILImage

from .tentacle import LENGTH


def get_lines(image_path):
    """Returns a 64x64 pixel array all the lines of an image.

    Parameters
        ----------
        image_path : string
            Relative image page
    """
    img = PILImage.open(path.abspath(image_path))
    img = img.resize((LENGTH, LENGTH))

    lines = []
    
    pixels = img.load()
    for y in range(img.size[1]):
        xs = []
        for x in range(img.size[0]):
            xs.append(pixels[x, y])

        lines.append(xs)
        # del xs
    # del img

    return lines
