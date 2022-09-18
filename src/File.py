import re
import string
from PIL import Image
import numpy as np
from Cipher import Cipher
from Pixel import Pixel
from Settings import Settings
import os

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
    for i in range(0, len(binString), 9):
        temp_data = int(binString[i:i + 9])

        decimal_data = BinaryToDecimal(temp_data)

        str = str + chr(decimal_data)
    return str


def concatAndUnify(byte):
    concatedByte = byte[2:]

    # Unify each character to a full byte
    while len(concatedByte) < 9:
        concatedByte = "0{}".format(concatedByte)
    return concatedByte

def textToBinary(message: string):
    binArr = map(bin, bytearray(message, "latin-1"))
    binArr = list(map(concatAndUnify, binArr))
    binString = "".join(binArr)
    return binString


class File():
    filePath = None
    settings = Settings(False, False, False)
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
        print(self.settings.isEncrypted)
        if self.settings.isEncrypted == True:
            digest, iv = Cipher("asd").encrypt(message)
            message = digest.decode("latin-1")
            print("encoded message", message)

        encoded = textToBinary(message)
        print("Started encoding")
        print("encoded text: {}".format(encoded))
        editedPixels = self.pixels.copy()
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                if h == 0 and w == 0:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(
                        1 if self.settings.isEncrypted else 0,
                        1 if self.settings.otherSetting else 0,
                        1 if self.settings.otherSetting2 else 0
                    ).serialize()

                    continue
                if len(encoded) > 0:
                    encodedR = int(encoded[0])
                    
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(0,0,0).serialize()
                    encoded = encoded[1:]
                    continue

                if len(encoded) > 1:
                    encodedG = int(encoded[1])
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(encodedR,1,0).serialize()
                    encoded = encoded[2:]
                    continue
                if len(encoded) > 2:
                    encodedB = int(encoded[2])
                else:
                    editedPixels[h][w] = editedPixels[h][w].setLastBits(encodedR,encodedG,1).serialize()
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
        stop = False
        print('Started decoding')
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                if stop:
                    continue
                if h == 0 and w == 0:
                    self.settings = Settings.fromPixel(editedPixels[0][0])
                    continue
                binString = binString + editedPixels[h][w].getLastBits()
                if re.search("10000000000000", binString):
                    stop = True
                    binString = binString[:len(binString) - 15]


        decodedText = binaryToText(binString) 
        print("encoded text: {}".format(binString))
        if self.settings.isEncrypted == True:
            decodedText = Cipher("asd").decrypt(decodedText.encode("latin-1"), b"SuperSecretIV123")

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
