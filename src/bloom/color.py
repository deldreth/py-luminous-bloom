#!/usr/bin/env python

from colour import Color, color_scale


class Colors(Color):
    def __init__(self, color=None, pick_for=None, **kwargs):
        super().__init__(color, pick_for, kwargs)

        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return str(self.rgb)

    def get_rgb(self):
        red, green, blue = super().get_rgb()
        return (round(red * 255), round(green * 255), round(blue * 255))

    def range_to(self, color, distance):
        colors = []
        for hsl in color_scale(self._hsl, color.hsl, distance - 1):
            colors.append(Colors(hsl=hsl))

        return colors


def range_or_luminance(color, length):
    """
    Given a single color return a list of luminance adjusted rgb values (dark to bright).
    Given a list of colors return a list of their rgb values
    """
    colors = []
    if isinstance(color, (list,)):
        # colors.append((0, 0, 0)) # This breaks a few animations but is necessary on others...
        for c in color:
            colors.append(c.rgb)
    else:
        for c in range(length):
            color.luminance = c / (length * 2)
            colors.append(color.rgb)

    return colors


def wheel(value):
    """ Given 0-255, make an rgb color with gamma correction """
    if value < 85:
        return (value * 3, 255 - value * 3, 0)
    elif value < 170:
        value -= 85
        return (255 - value * 3, 0, value * 3)
    else:
        value -= 170
        return (0, value * 3, 255 - value * 3)


# Not used, referenced from Colour lib
RGB_TO_COLOR_NAMES = {
    (0, 0, 0): ['Black'],
    (0, 0, 128): ['Navy', 'NavyBlue'],
    (0, 0, 139): ['DarkBlue'],
    (0, 0, 205): ['MediumBlue'],
    (0, 0, 255): ['Blue'],
    (0, 100, 0): ['DarkGreen'],
    (0, 128, 0): ['Green'],
    (0, 139, 139): ['DarkCyan'],
    (0, 191, 255): ['DeepSkyBlue'],
    (0, 206, 209): ['DarkTurquoise'],
    (0, 250, 154): ['MediumSpringGreen'],
    (0, 255, 0): ['Lime'],
    (0, 255, 127): ['SpringGreen'],
    (0, 255, 255): ['Cyan', 'Aqua'],
    (25, 25, 112): ['MidnightBlue'],
    (30, 144, 255): ['DodgerBlue'],
    (32, 178, 170): ['LightSeaGreen'],
    (34, 139, 34): ['ForestGreen'],
    (46, 139, 87): ['SeaGreen'],
    (47, 79, 79): ['DarkSlateGray', 'DarkSlateGrey'],
    (50, 205, 50): ['LimeGreen'],
    (60, 179, 113): ['MediumSeaGreen'],
    (64, 224, 208): ['Turquoise'],
    (65, 105, 225): ['RoyalBlue'],
    (70, 130, 180): ['SteelBlue'],
    (72, 61, 139): ['DarkSlateBlue'],
    (72, 209, 204): ['MediumTurquoise'],
    (75, 0, 130): ['Indigo'],
    (85, 107, 47): ['DarkOliveGreen'],
    (95, 158, 160): ['CadetBlue'],
    (100, 149, 237): ['CornflowerBlue'],
    (102, 205, 170): ['MediumAquamarine'],
    (105, 105, 105): ['DimGray', 'DimGrey'],
    (106, 90, 205): ['SlateBlue'],
    (107, 142, 35): ['OliveDrab'],
    (112, 128, 144): ['SlateGray', 'SlateGrey'],
    (119, 136, 153): ['LightSlateGray', 'LightSlateGrey'],
    (123, 104, 238): ['MediumSlateBlue'],
    (124, 252, 0): ['LawnGreen'],
    (127, 255, 0): ['Chartreuse'],
    (127, 255, 212): ['Aquamarine'],
    (128, 0, 0): ['Maroon'],
    (128, 0, 128): ['Purple'],
    (128, 128, 0): ['Olive'],
    (128, 128, 128): ['Gray', 'Grey'],
    (132, 112, 255): ['LightSlateBlue'],
    (135, 206, 235): ['SkyBlue'],
    (135, 206, 250): ['LightSkyBlue'],
    (138, 43, 226): ['BlueViolet'],
    (139, 0, 0): ['DarkRed'],
    (139, 0, 139): ['DarkMagenta'],
    (139, 69, 19): ['SaddleBrown'],
    (143, 188, 143): ['DarkSeaGreen'],
    (144, 238, 144): ['LightGreen'],
    (147, 112, 219): ['MediumPurple'],
    (148, 0, 211): ['DarkViolet'],
    (152, 251, 152): ['PaleGreen'],
    (153, 50, 204): ['DarkOrchid'],
    (154, 205, 50): ['YellowGreen'],
    (160, 82, 45): ['Sienna'],
    (165, 42, 42): ['Brown'],
    (169, 169, 169): ['DarkGray', 'DarkGrey'],
    (173, 216, 230): ['LightBlue'],
    (173, 255, 47): ['GreenYellow'],
    (175, 238, 238): ['PaleTurquoise'],
    (176, 196, 222): ['LightSteelBlue'],
    (176, 224, 230): ['PowderBlue'],
    (178, 34, 34): ['Firebrick'],
    (184, 134, 11): ['DarkGoldenrod'],
    (186, 85, 211): ['MediumOrchid'],
    (188, 143, 143): ['RosyBrown'],
    (189, 183, 107): ['DarkKhaki'],
    (192, 192, 192): ['Silver'],
    (199, 21, 133): ['MediumVioletRed'],
    (205, 92, 92): ['IndianRed'],
    (205, 133, 63): ['Peru'],
    (208, 32, 144): ['VioletRed'],
    (210, 105, 30): ['Chocolate'],
    (210, 180, 140): ['Tan'],
    (211, 211, 211): ['LightGray', 'LightGrey'],
    (216, 191, 216): ['Thistle'],
    (218, 112, 214): ['Orchid'],
    (218, 165, 32): ['Goldenrod'],
    (219, 112, 147): ['PaleVioletRed'],
    (220, 20, 60): ['Crimson'],
    (220, 220, 220): ['Gainsboro'],
    (221, 160, 221): ['Plum'],
    (222, 184, 135): ['Burlywood'],
    (224, 255, 255): ['LightCyan'],
    (230, 230, 250): ['Lavender'],
    (233, 150, 122): ['DarkSalmon'],
    (238, 130, 238): ['Violet'],
    (238, 221, 130): ['LightGoldenrod'],
    (238, 232, 170): ['PaleGoldenrod'],
    (240, 128, 128): ['LightCoral'],
    (240, 230, 140): ['Khaki'],
    (240, 248, 255): ['AliceBlue'],
    (240, 255, 240): ['Honeydew'],
    (240, 255, 255): ['Azure'],
    (244, 164, 96): ['SandyBrown'],
    (245, 222, 179): ['Wheat'],
    (245, 245, 220): ['Beige'],
    (245, 245, 245): ['WhiteSmoke'],
    (245, 255, 250): ['MintCream'],
    (248, 248, 255): ['GhostWhite'],
    (250, 128, 114): ['Salmon'],
    (250, 235, 215): ['AntiqueWhite'],
    (250, 240, 230): ['Linen'],
    (250, 250, 210): ['LightGoldenrodYellow'],
    (253, 245, 230): ['OldLace'],
    (255, 0, 0): ['Red'],
    (255, 0, 255): ['Magenta', 'Fuchsia'],
    (255, 20, 147): ['DeepPink'],
    (255, 69, 0): ['OrangeRed'],
    (255, 99, 71): ['Tomato'],
    (255, 105, 180): ['HotPink'],
    (255, 127, 80): ['Coral'],
    (255, 140, 0): ['DarkOrange'],
    (255, 160, 122): ['LightSalmon'],
    (255, 165, 0): ['Orange'],
    (255, 182, 193): ['LightPink'],
    (255, 192, 203): ['Pink'],
    (255, 215, 0): ['Gold'],
    (255, 218, 185): ['PeachPuff'],
    (255, 222, 173): ['NavajoWhite'],
    (255, 228, 181): ['Moccasin'],
    (255, 228, 196): ['Bisque'],
    (255, 228, 225): ['MistyRose'],
    (255, 235, 205): ['BlanchedAlmond'],
    (255, 239, 213): ['PapayaWhip'],
    (255, 240, 245): ['LavenderBlush'],
    (255, 245, 238): ['Seashell'],
    (255, 248, 220): ['Cornsilk'],
    (255, 250, 205): ['LemonChiffon'],
    (255, 250, 240): ['FloralWhite'],
    (255, 250, 250): ['Snow'],
    (255, 255, 0): ['Yellow'],
    (255, 255, 224): ['LightYellow'],
    (255, 255, 240): ['Ivory'],
    (255, 255, 255): ['White']
}
