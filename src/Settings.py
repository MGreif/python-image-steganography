from cmath import pi
from typing import Tuple
from Pixel import Pixel


# Due to just max 3 settings options this will not be a real bitmap.

class Settings():
    isEncrypted = False
    otherSetting = False
    otherSetting2 = False
    bitmap = None

    def __init__(self, isEncrypted: bool, otherSetting: bool, otherSetting2: bool):
        self.isEncrypted = isEncrypted
        self.otherSetting = otherSetting
        self.otherSetting2 = otherSetting2
        self.bitmap = tuple([isEncrypted == 1, otherSetting == 1, otherSetting2 == 1])

    def fromPixel(pixel: Pixel):
        bitmap = pixel.getLastBits()
        isEncrypted = bitmap[0] == "1"
        otherSetting = bitmap[1] == "1"
        otherSetting2 = bitmap[2] == "1"
        return Settings(isEncrypted, otherSetting, otherSetting2)
    