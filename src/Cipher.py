import hashlib
from Crypto import Random
from Crypto.Cipher import AES

class Cipher():
    iv = b"SuperSecretIV123" #Random.new().read(AES.block_size)\
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode("latin-1")).digest()
        self.bs = AES.block_size
        
    def encrypt(self, message: str) -> (bytes, bytes):
        encoded = self._pad(message).encode("latin-1")
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        digest = cipher.encrypt(encoded)
        return (digest, self.iv)



    def decrypt(self, digest):
        newCipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = newCipher.decrypt(digest)
        return Cipher._unpad(decrypted.decode("latin-1"))

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
