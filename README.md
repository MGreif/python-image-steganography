# Requirements for Python3

`pip3 install -r requirements.txt`


# Instruction
## Encode

This program can be used to modify a PNG picture to contain a hidden message.

Usage: `main.py example.png`


### Simple example:

```
Encode or Decode an encoded image (encode | decode): encode
Input the text to encode into the picture: This is a secret message!!
Do you wish to encrypt the message? (y | n): n
Started encoding ...
encoded message: 001010100001101000001101001001110011000100000001101001001110011000100000001100001000100000001110011001100101001100011001110010001100101001110100000100000001101101001100101001110011001110011001100001001100111001100101000100001000100001
Finished encoding
Saved image in <cwd>/<imageName>.encoded.png
```

### Encryption example:

```
Encode or Decode an encoded image (encode | decode): encode
Input the text to encode into the picture: This is an encrypted secret message!! 
Do you wish to encrypt the message? (y | n): y
Specify the encryption key: Secret
Started encrypting ...
Encrypted message: Sæ1ûðÓQã<¹Û"GÑmEû;=Èá4 °_A¶ª«»ªDM
Started encoding ...
encoded message: 001010011011100110000110001011111011010010101010001011011110000011010011001010001011100011000111100010111001011011011010011001000100010010000001001000111011010001001101101001000101011111011000111011000000101000111101011001000000011111010010010011100001010011110001010001000111100001000010011101000000110100000010000000100000010110000000011111001011111001000001010110110010000010010101010010101011010111011010101010001000100001001101
Finished encoding
```

## Decode

The message can be revealed by simple decode an encoded picture.

Usage: `main.py example.encoded.png`

### Simple example

```
Encode or Decode an encoded image (encode | decode): decode
Started decoding ...
Decoded message: This is a secret message!!
```

### Decryption example

```
Encode or Decode an encoded image (encode | decode): decode
Started decoding ...
Decoded message: Sæ1ûðÓQã<¹Û"GÑmEû;=Èá4 °_A¶ª«»ªDM
The text seems to be encrypted ...
Input the keyphrase for decryption: Secret
Started decrypting ...
Decrypted message: This is an encrypted secret message!!
```

# Can you decode this?

![Python](python.png)

# TODO
- [x] Add Pixel (First or Last) designated for meta infos bitmap
- [x] Add AES Encryption Method
- [x] Add option to check if image is encrypted
- Generate new IV in each encryption and store in image
- Add verbose mode
- Add GUI
