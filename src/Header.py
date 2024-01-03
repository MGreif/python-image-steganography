class Flags:
    encrypted = False

    def __init__(self, encrypted: bool):
        self.encrypted = encrypted

    def from_byte_string(byte_string):
        if len(byte_string) != 8:
            raise "Byte string has to have 8 characters"
        new = Flags(False)
        new.encrypted = byte_string[7] == "1"
        return new


    def to_binary_string(self):
        b = bin((0*(2^7)) + (0*(2^6)) + (0*(2^5)) + (0*(2^4)) + (0*(2^3)) + (0*(2^2)) + (0*(2^1)) + (int(self.encrypted == True)*(1^0)))[2:]
        return binaryHelper.binary_padding_to_full_byte(b)

# Header Length: 1 byte
# Version: 1 byte
# Flags: 1 byte none - none - none - none - none - none - none - encrypted 
# Content Length: 1 4 byte
#

from FileManager import FileManager
import binaryHelper

class Header():
    version = 1
    flags = Flags(encrypted=False)
    content_length = None
    header_length = None

    def __init__(self, isEncrypted: bool):
        self.flags = Flags(isEncrypted)

    def fromFile(file: FileManager):
        byte_string = file.get_binary_string()

        (header_length, byte_string) = binaryHelper.get_first_byte_string(binary_string=byte_string)
        header_length = binaryHelper.BinaryToDecimal(int(header_length.lstrip("0")))
        (version, byte_string) = binaryHelper.get_first_byte_string(binary_string=byte_string)
        (flags, byte_string) = binaryHelper.get_first_byte_string(binary_string=byte_string)
        (content_length, byte_string) = binaryHelper.get_first_byte_string(binary_string=byte_string, amount_of_bytes=4)

        new = Header(False)
        new.flags = Flags.from_byte_string(flags)
        new.version = int(version, base=2)
        new.header_length = header_length
        new.content_length = int(content_length, base=2)

        return new
        
    
    def calculate_header_byte_length(self):
        version_length = 1 # One byte is minimum
        flags_length = 1 # Bitmap of one byte
        content_byte_length_container = 4
        header_content_length_container = 1 # For now just one byte (256)
        length = version_length + flags_length + content_byte_length_container + header_content_length_container
        return bin(length)[2:]
    
    def to_binary_string(self, content_length_binary_string: str):
        binary_string = binaryHelper.binary_padding_to_full_byte(self.calculate_header_byte_length())

        binary_string += binaryHelper.binary_padding_to_full_byte(bin(self.version)[2:])
        binary_string += binaryHelper.binary_padding_to_full_byte(self.flags.to_binary_string())
        binary_string += binaryHelper.binary_padding_to_full_byte(content_length_binary_string, 4*8)
        
        return binary_string
    


