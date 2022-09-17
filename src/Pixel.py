
from pickletools import uint1


def toggleBit(value, position: uint1, set):
    mask = 1 << position
    value &= ~mask
    if set == 1:
        value |= mask
    return value
    

class Pixel():
    r = None
    g = None
    b = None

    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b

    def setLastBits(self, first, second, third):
        self.r = toggleBit(self.r, 0, first)
        self.g = toggleBit(self.g, 0, second)
        self.b = toggleBit(self.b, 0, third)
        return self
    
    def getLastBits(self):
        rLastBit = bin(self.r)[-1]
        gLastBit = bin(self.g)[-1]
        bLastBit = bin(self.b)[-1]
        return "{}{}{}".format(rLastBit, gLastBit, bLastBit)

    def print(self):
        print("{} {} {}".format(bin(self.r)[0:2], self.g, self.b))

    def serialize(self):
        return tuple([self.r, self.g, self.b])
