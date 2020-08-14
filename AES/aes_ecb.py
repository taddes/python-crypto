import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key = os.urandom(16)
aesCipher = Cipher(algorithms.AES(key),
                    modes.ECB(),
                    backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecrpytor = aesCipher.decryptor()