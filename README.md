# About

This tool performs technical steganography to create an image (PNG) stego-object. It uses the LSB (Least-Significant-Bit) substitution technique to hide a message inside a picture. This message can also be encrypted using the symmetrical `AES256` algorithm.

The steganography will only work on `PNG` as of the current state.

# Requirements for Python3

`pip3 install -r requirements.txt`



# Development

- `make test` - To run basic integration and unit tests that check correct en-/decoding and en-/decryption

# Usage
## Encode

This program can be used to modify a PNG picture to contain a hidden message.

Usage: `main.py example.png`


### Simple example:

```
Encode or Decode an encoded image (encode | decode): encode
Input the text to encode into the image: This is my secret message!
Do you wish to encrypt the message? (y | n): n
Encoded message: 0101010001101000011010010111001100100000011010010111001100100000011011010111100100100000011100110110010101100011011100100110010101110100001000000110110101100101011100110111001101100001011001110110010100100001
Finished encoding
Saved image to <cwd>/<imageName>.encoded.png
```

### Encryption example:

```
Encode or Decode an encoded image (encode | decode): encode
Input the text to encode into the image: This is an encrypted secret message!! 
Do you wish to encrypt the message? (y | n): y
Specify the encryption key: Secret
Encrypted message: Sæ1ûðÓQã<¹Û"GÑmEû;=ÈáQ<Bè4 °_A¶ª«»ªDM
Encoded message: 010100111110011000110001111110111001010110001011111100001101001101010001111000110011110010111001110110111001100100100010100000010100011111010001011011010100010111111011001110110000010100111101110010000001111110010010111000011001111001010001001111000100001011101000001101000001000000100000101100000001111101011111010000011011011010000010101010101010101110111011101010100100010001001101
Finished encoding
Saved image to <cwd>/<imageName>.encoded.png
```

## Decode

The message can be revealed by simple decode an encoded picture.

Usage: `main.py example.encoded.png`

### Simple example

```
Encode or Decode an encoded image (encode | decode): decode
Version: 1
Header length: 7
Content length: 26
Flag byte: 00000000
- Encryption flag: False
Decoded message: This is my secret message!
```

### Decryption example

```
Encode or Decode an encoded image (encode | decode): decode
Version: 1
Header length: 7
Content length: 48
Flag byte: 00000001
- Encryption flag: True
Decoded message: Sæ1ûðÓQã<¹Û"GÑmEû;=ÈáQ<Bè4 °_A¶ª«»ªDM
The text seems to be encrypted ...
Input the keyphrase for decryption: Secret
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
