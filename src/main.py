import os
import string
import sys
from typing import Tuple
from PIL import Image
import re
import numpy as np

def main():
    try:
        filePath = sys.argv[1]
    except IndexError:
        print("Usage: command <picture.jpeg>")
        exit()

    if (re.search(".+\.(jpeg|jpg|png)$", filePath, re.IGNORECASE) == None):
        print("Must have png, jpg, or jpeg extension")
        exit()

    try:
        file = File(filePath)
    except FileNotFoundError:
        print("File {} not found".format(filePath))
        exit()


    newPixels = file.editImage(-100,20,30)
    editedPixels = newPixels
    for h in range(editedPixels.__len__()):
        for w in range(editedPixels[h].__len__()):
            r = editedPixels[h][w].r
            g = editedPixels[h][w].g
            b = editedPixels[h][w].b
            editedPixels[h][w] = [r,g,b]

    newImage = Image.fromarray(np.array(editedPixels, dtype=np.uint8), mode="RGB")
    newImage.save('test.JPG')


class Pixel():
    r = None
    g = None
    b = None

    def __init__(self, r, g, b) -> None:
        self.r = r
        self.g = g
        self.b = b
    def print(self):
        print("{} {} {}".format(self.r, self.g, self.b))


class File():
    filePath = None
    image = None
    pixels = []
    def __init__(self, filePath: string) -> None:
        self.filePath = filePath
        self.image = Image.open(self.filePath)

    def print(self):
        print(self.filePath)
        print(self.image.getdata())

    def calcPixel(self):
        width, height = self.image.size
        data = []

        for h in range(height):
            data.append([])
            for w in range(width):
                r, g, b = self.image.getpixel(tuple([w,h]))
                pixel = Pixel(r, g, b)
                data[h].append(pixel)

        self.pixels = data
        return data

    def editImage(self, deltaR, deltaG, deltaB):
        if (self.pixels.__len__() == 0):
            self.calcPixel()

        editedPixels = self.pixels.copy()
        for h in range(editedPixels.__len__()):
            for w in range(editedPixels[h].__len__()):
                r = editedPixels[h][w].r - deltaR
                g = editedPixels[h][w].g - deltaG
                b = editedPixels[h][w].b - deltaB
                editedPixels[h][w] = Pixel(r,g,b)
        return editedPixels



        

main()