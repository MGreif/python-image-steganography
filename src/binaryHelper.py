
def binary_padding_to_full_byte(binary_string: str, padding = 8):
    modulus = len(binary_string) % padding
    if (modulus == 0):
        return binary_string
    padding_needed = padding - modulus
    return padding_needed * "0" + binary_string


def get_first_byte_string(binary_string, amount_of_bytes = 1):
    return (binary_string[:amount_of_bytes*8], binary_string[amount_of_bytes*8:])


def concatAndUnify(byte):
    concatedByte = byte[2:]

    # Unify each character to a full byte
    while len(concatedByte) < 8:
        concatedByte = "0{}".format(concatedByte)
    return concatedByte


def textToBinary(message: str):
    binArr = map(bin, bytearray(message, "latin-1"))
    binArr = list(map(concatAndUnify, binArr))
    binString = "".join(binArr)
    return binString

def remove_padding(binary_string: str):
    return binary_string.lstrip("0")


def BinaryToDecimal(binary: int):
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

 
def binaryToText(binString: str):
    str =''

    # Get binary string, split into full bytes and convert binary to decimal of each byte
    for i in range(0, len(binString), 8):
        temp_data = int(binString[i:i + 8])

        decimal_data = BinaryToDecimal(temp_data)

        str = str + chr(decimal_data)
    return str




