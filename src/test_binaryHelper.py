import binaryHelper

def test_textToBinary():
    assert binaryHelper.textToBinary("HoLlA") == "0100100001101111010011000110110001000001"


def test_concatAndUnify():
    assert binaryHelper.concatAndUnify("0b101") == "00000101"

def test_binary_padding_to_full_byte():
    assert binaryHelper.binary_padding_to_full_byte("100") == "00000100"

def test_binary_padding_to_full_byte_when_full():
    assert binaryHelper.binary_padding_to_full_byte("11111111") == "11111111"

def test_binary_padding_to_full_byte_with_argument():
    assert binaryHelper.binary_padding_to_full_byte("100", 10) == "0000000100"

def test_get_first_byte_string():
    assert binaryHelper.get_first_byte_string("0101101011011010")[0] == "01011010" and binaryHelper.get_first_byte_string("0000111100110101")[1] == "00110101"

def test_remove_padding():
    assert binaryHelper.remove_padding("000001") == "1"


def test_binaryToDecimal():
    assert binaryHelper.BinaryToDecimal(1011) == 11


def test_binaryToText():
    assert binaryHelper.binaryToText("1001000") == "H" 