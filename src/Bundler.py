from FileManager import FileManager
from Cipher import Cipher
from Header import Header
import math
import binaryHelper

class Encoder():
    file: FileManager = None
    header: Header = Header(False)

    def __init__(self, file: FileManager, header: Header):
        self.file = file
        self.header = header

    
    
    def encode_file_with_message(self, message: str):
        encoded_message = binaryHelper.textToBinary(message=message)
        message_bit_length = len(encoded_message)

        if (message_bit_length > len(self.file.binary_string)):
            raise "The specified data is too large. Please increase the image size or use another one ..."

        message_byte_length = math.ceil(message_bit_length / 8)
        message_byte_length_binary = bin(message_byte_length)[2:]

        print("Encoded message:", encoded_message)

        header_binary = self.header.to_binary_string(message_byte_length_binary)
        self.file.write_and_save(header_binary+encoded_message, self.file.fileName+".encoded")


class Decoder():
    file: FileManager = None
    header: Header = None

    def __init__(self, file: FileManager):
        self.file = file
        self.extract_header_from_file()

    def extract_header_from_file(self):
        self.header = Header.fromFile(file=self.file)
        return self.header
    
    def decode(self):
        self.header.debug()

        header_length: int = self.header.header_length
        content_binary_string = self.file.binary_string
        content_binary_string = content_binary_string[header_length*8:]
        content_binary_string = content_binary_string[:self.header.content_length*8]
        
        content_string = binaryHelper.binaryToText(content_binary_string)
        return content_string
    


