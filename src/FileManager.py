import string
from PIL import Image
import numpy as np
from Pixel import Pixel
import os

class FileManager:
    filePath = None
    fileName = None
    image: Image.Image = None
    pixels: list[list[Pixel]] = []
    binary_string: str = None

    def __init__(self, filePath: string) -> None:
        self.filePath = filePath
        self.fileName = os.path.basename(filePath).split(".")[0]
        self.image = Image.open(self.filePath)
        self.pixels = self.getPixels()
        self.binary_string = self.get_binary_string()

    def getPixels(self):
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
        return data

    def write_and_save(self, binary_string: str, filename: str):
        editedPixels = self.pixels.copy()
        rest = binary_string
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                R = 0
                G = 0
                B = 0
                if len(rest) > 0:
                    R = int(rest[0])
                    rest = rest[1:]


                if len(rest) > 0:
                    G = int(rest[0])
                    rest = rest[1:]


                if len(rest) > 0:
                    B = int(rest[0])
                    rest = rest[1:]

                editedPixels[h][w] = editedPixels[h][w].setLastBits(R, G, B).serialize()

        img = Image.fromarray(np.array(editedPixels, dtype=np.uint8))
        img.save("{}.png".format(filename))
        print("Finished encoding")
        print("Saved image in {0}/{1}.png".format(os.getcwd(), filename))

    def get_binary_string(self):
        binString = ""

        for h in range(len(self.pixels)):
            for w in range(len(self.pixels[h])):
                binString = binString + self.pixels[h][w].getLastBits()

        return binString

