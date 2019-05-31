#!/usr/bin/env python

from enum import Enum


class Direction(Enum):
    """
    Enum containing constants to represent strand LED animation direction (up|down)
    or rotate direction (left|right)
    """

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
