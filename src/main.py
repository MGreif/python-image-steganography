import sys
import re
from File import File

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



main()