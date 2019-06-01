"""Tentacles are strands of lights :const:`LENGTH` long. They have start and end dimensions
which are offsets from the tentacle dict key of tentacles in :attr:`~bloom.control.Control.tentacles`.

<Tentacle 1> : 0..63

<Tentacle 2> : 64..127
"""

LENGTH = 64

class Tentacle:
    def __init__(self, n):
        self.__n = n
        self.start = (n * LENGTH) - LENGTH
        self.end = n * LENGTH - 1

    def __iter__(self):
        """Allows for a tentacles pixel numbers to be iterated over."""
        p = self.start
        while p <= self.end:
            yield p
            p += 1

    def __repr__(self):
        return "<Tentacle {}>".format(self.__n)

    def which(self):
        """Returns the integer key reference of the tentacle."""
        return self.__n

    def dims(self):
        """Returns a tuple containing start and end."""
        return (self.start, self.end)

    def colorize(self, pixels, rgb):
        """Set the :attr:`~bloom.control.Control.pixels` mapped through to tentacle to an rgb tuple.

        :param pixels: List of :attr:`~bloom.control.Control.pixels`
        
        :param rgb: Tuple in the form of (r, g, b)
        :type rgb: Tuple(integer, integer, integer)
        """
        for ic in range(LENGTH):
            if self.contains(self.start + ic):
                pixels[self.start + ic] = rgb

        return pixels

    def patternize(self, pixels, colors):
        """Set the :attr:`~bloom.control.Control.pixels` mapped through the tentacle to a range of :mod:`~bloom.color`.

        :param pixels: List of :attr:`~bloom.control.Control.pixels`

        :param colors: A list of Colors.
        :type colors: List(:class:`~bloom.color.Colors`)
        """
        for ic, c in enumerate(colors):
            if self.contains(self.start + ic):
                pixels[self.start + ic] = c

        return pixels

    def get(self, pixels):
        """Returns a slice of pixels based on the start and end of the tentacle.

        :param pixels: List of :attr:`~bloom.control.Control.pixels`
        """
        return pixels[self.start:self.end + 1]

    def contains(self, pixel):
        """ Returns True if a pixels exists within the tentacles start and end.

        :param pixel: Any integer
        :type pixel: integer
        """
        return self.start <= pixel <= self.end
