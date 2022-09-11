# Instruction
## Encode

This program can be used to modify a PNG picture to contain a hidden message.

Usage: `main.py example.png encode "This is a secret message"`


```
Started encoding
encoded text: 010101000110100001101001011100110010000001101001011100110010000001100001001000000111001101100101011000110111001001100101011101000010000001101101011001010111001101110011011000010110011101100101
Finished encoding
Saved image in <cwd>/example.encoded.png
```

## Decode

The message can be revealed by simple decode an encoded picture.

Usage: `main.py example.encoded.png decode`

```
Started decoding
Decoded text: This is a secret message
```

# Can you decode this?

![Python](python.png)

# TODO
- Add AES Encryption Method
- Add verbose mode
- Add GUI
- Add Pixel (First or Last) designated for meta infos bitmap
- Add option to check if image is encoded