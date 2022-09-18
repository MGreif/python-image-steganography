from pydoc import doc
import sys
import re
from File import File


def main():

    try:
        filePath = sys.argv[1]
        fileName = filePath.split(".")[0]
        fileExtension = filePath.split(".")[-1]

    except IndexError:
        print("Usage: command <picture.png>")
        exit()

    if re.search(".+\.(png)$", filePath, re.IGNORECASE) == None:
        print("Must have png extension")
        exit()

    try:
        file = File(filePath)
    except FileNotFoundError:
        print("File {} not found".format(filePath))
        exit()

    action = ""
    while re.search("encode|decode", action) == None:
        action = input("Encode or Decode an encoded image (encode | decode): ")

    if action == "encode":
        text = input("Input the text to encode into the picture: ")
        file.setMessage(text)
        encrypt = ""
        while re.search("y|n", encrypt) == None:
            encrypt = input("Do you wish to encrypt the message? (y | n): ")
        if (encrypt == "y"):
            encryptionKey = input("Specify the encryption key: ")
            file = file.encryptMessage(encryptionKey)
        file = file.encodeImage("{}.encoded".format(fileName))

    elif action == "decode":
        file = file.decodeImage()
        if file.settings.isEncrypted:
            print("The text seems to be decrypted ...")
            key = input("Input the keyphrase for decryption: ")
            file = file.decryptMessage(key)

main()