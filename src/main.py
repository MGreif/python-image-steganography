import sys
import re
from Bundler import Encoder, Decoder
from Header import Header
from FileManager import FileManager
from Cipher import Cipher
import os




def main():
    try:
        filePath = sys.argv[1]
        fileName = os.path.basename(filePath).split(".")[0]

    except IndexError:
        print("Usage: command <picture.png>")
        exit()

    if re.search(".+\.(png)$", filePath, re.IGNORECASE) == None:
        print("Must have png extension")
        exit()

    try:
        file = FileManager(filePath)
    except FileNotFoundError:
        print("File {} not found".format(filePath))
        exit()



    action = ""
    while re.search("encode|decode", action) == None:
        action = input("Encode or Decode an encoded image (encode | decode): ")

    if action == "encode":
        text = input("Input the text to encode into the picture: ")
        encrypt = ""

        header = Header(False)

        while re.search("y|n", encrypt) == None:
            encrypt = input("Do you wish to encrypt the message? (y | n): ")
        if (encrypt == "y"):
            encryptionKey = input("Specify the encryption key: ")
            cipher = Cipher(key=encryptionKey)
            (text, _) = cipher.encrypt(message=text)
            text: bytes = text
            text: str = text.decode("latin-1")
            header.flags.encrypted = True

        encoder = Encoder(file=file, header=header)

        encoder.encode_file_with_message(message=text)

    elif action == "decode":
        decoder = Decoder(file=file)
        decoded_text = decoder.decode()
        print("Decoded message:", decoded_text)

        if decoder.header.flags.encrypted == True:
            print("The text seems to be encrypted ...")
            key = input("Input the keyphrase for decryption: ")
            cipher = Cipher(key=key)
            decrypted = cipher.decrypt(decoded_text.encode("latin-1"))
            print("Decrypted message:", decrypted)

main()