import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'http://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.
    Takes the string of a color name and returns its RGB value.
    """
    def __init__(self, color):
        self.color = color
        self.color = self.color.upper()
        for k, v in COLOR_NAMES.items():
            self.rgb = v
        if self.color not in COLOR_NAMES:
            self.rgb = None
        else:
            self.rgb = COLOR_NAMES[self.color]

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        lst_ch = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
        hex = hex.lstrip('#')
        for c in hex:
            #note that 'c' differs from c because of hex characterisation
            if 'c' not in lst_ch:
                raise ValueError ("not hex compliant elements")
            if len(hex) != 6:
                raise ValueError ("not a hex object")
            else:
                lv = len(hex)
                return tuple(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if isinstance(rgb, str) is True:
            raise ValueError("RGB is a string")
        if isinstance(rgb, str) is False:
            rgb = list(rgb)
            for x in rgb:
                if x < 0 or x > 255:
                    raise ValueError("one or more elements is outside of RGB parameter")
            rgb = tuple(rgb)
            return '#%02x%02x%02x' % (rgb)

    def __repr__(self):
        return f"{self.__class__.__name__}('{(self.color).lower()}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb != None:
            return f'{self.rgb}'
        else:
            return f'Unknown'

