import base64
import hashlib
import sys
from Crypto import Random
from Crypto.Cipher import AES

class Cipher():
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.bs = AES.block_size
        
    def encrypt(self, message: str):
        encoded = self._pad(message).encode("latin-1")
        iv = b"SuperSecretIV123" #Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        digest = cipher.encrypt(encoded)
        return (digest, iv)

    def decrypt2(self, digest):
        enc = base64.b64decode(digest)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def decrypt(self, digest, iv):
        newCipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = newCipher.decrypt(digest)
        return Cipher._unpad(decrypted.decode("latin-1"))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
