import os
from cryptography.hazmat.primitives.scrypt import scrypt
from cryptography.hazmat.primitives.backends import default_backend

salt = os.urandom(16)

kdf = Scrypt(salt=salt, length=32,
                n=2**14, r=8, p=1,
                backend=default_backend())