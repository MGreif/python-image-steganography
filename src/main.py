import string
import sys
import re
from File import File
from Cipher import Cipher


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

def test():
    digest, iv = Cipher("asdfasdfasdfasdfasdfasdfasdfasdf").encrypt("lold")
    message = digest.decode("latin-1")
    encoded = textToBinary(message)


    decodedText = binaryToText(encoded) 
    paddedText = decodedText
    decodedText = Cipher("asdfasdfasdfasdfasdfasdfasdfasdf").decrypt(paddedText.encode("latin-1"), b"SuperSecretIV123")
    print(decodedText)
    
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