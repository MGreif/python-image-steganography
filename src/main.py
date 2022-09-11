import os

from pickletools import uint1
import string
import sys
from PIL import Image
import re
import numpy as np

def main():
    try:
        filePath = sys.argv[1]
        fileName = filePath.split(".")[0]
        fileExtension = filePath.split(".")[-1]
        action = sys.argv[2]
        if action == "encode":
            text = sys.argv[3]
    except IndexError:
        print("Usage: command <picture.png> <decode|encode> [text]")
        exit()

    if re.search(".+\.(png)$", filePath, re.IGNORECASE) == None:
        print("Must have png extension")
        exit()

    try:
        file = File(filePath)
    except FileNotFoundError:
        print("File {} not found".format(filePath))
        exit()

    if action == "encode":
        file.encodeImage(text, "{}.encoded".format(fileName))
    elif action == "decode":
        file.decodeImage()
    else:
        print("Usage: command <picture.png> <decode|encode> [text]")
        exit()


def toggleBit(value, position: uint1, set: bool):
    mask = 1 << position
    value &= ~mask
    if set == '1':
        value |= mask
    return value
    
def BinaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

 
def binaryToText(binString):
    str =''

    # Get binary string, split into full bytes and convert binary to decimal of each byte
    for i in range(0, len(binString), 8):
        temp_data = int(binString[i:i + 8])

        decimal_data = BinaryToDecimal(temp_data)

        str = str + chr(decimal_data)
    return str


def concatAndUnify(byte):
    concatedByte = byte[2:]

    # Unify each character to a full byte
    while len(concatedByte) < 8:
        concatedByte = "0{}".format(concatedByte)
    return concatedByte

def textToBinary(message: string):
    binArr = map(bin, bytearray(message, "utf8"))
    binArr = list(map(concatAndUnify, binArr))
    binString = "".join(binArr)
    return binString

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

class File():
    filePath = None
    image = None
    pixels = []
    def __init__(self, filePath: string) -> None:
        self.filePath = filePath
        self.image = Image.open(self.filePath)
        self.calcPixel()


    def print(self):
        print(self.filePath)
        print(self.image.getdata())

    def calcPixel(self):
        width, height = self.image.size
        data = []

        for h in range(height):
            data.append([])
            for w in range(width):
                result = self.image.getpixel(tuple([w,h]))
                r = result[0]
                g = result[1]
                b = result[2]
                pixel = Pixel(r, g, b)
                data[h].append(pixel)

        self.pixels = data
        return data

    def encodeImage(self, message: string, fileName: string):
        encoded = textToBinary(message)
        print("Started encoding")
        print("encoded text: {}".format(encoded))
        editedPixels = self.pixels.copy()
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                if len(encoded) > 0:
                    encodedR = encoded[0]
                    
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(0,0,0).serialize()
                    encoded = encoded[1:]
                    continue

                if len(encoded) > 1:
                    encodedG = encoded[1]
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(encodedR,0,0).serialize()
                    encoded = encoded[2:]
                    continue
                if len(encoded) > 2:
                    encodedB = encoded[2]
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(encodedR,encodedG,0).serialize()
                    encoded = ""
                    continue
                editedPixels[h][w] = editedPixels[h][w].setLastBits(encodedR,encodedG,encodedB).serialize()
                encoded = encoded[3:]

        img = Image.fromarray(np.array(editedPixels, dtype=np.uint8))
        img.save("{}.png".format(fileName))
        print("Finished encoding")
        print("Saved image in {0}/{1}.png".format(os.getcwd(), fileName))

    def decodeImage(self):
        binString = ""
        editedPixels = self.pixels.copy()
        print('Started decoding')
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                binString = binString + editedPixels[h][w].getLastBits()

        decodedText = binaryToText(binString)
        print("Decoded text:", decodedText),


# left unused for future purposes
    def editImage(self, deltaR, deltaG, deltaB):
        editedPixels = self.pixels.copy()
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                r = editedPixels[h][w].r - deltaR
                g = editedPixels[h][w].g - deltaG
                b = editedPixels[h][w].b - deltaB
                editedPixels[h][w] = Pixel(r,g,b)
        return editedPixels


main()