from Crypto.Cipher import AES
from Crypto import Random
import binascii

def append_space_padding(str, blocksize=128):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a' * pad_len
    return str + padding

def remove_space_padding(str, blocksize=128):
    pad_len = 0

    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break
    str = str[:-pad_len]
    return str

def encrypt(plaintext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(plaintext)

def decrypt(plaintext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(plaintext).decode('UTF-8')

if __name__ == "__main__":
    key = Random.new().read(16)
    plaintext = "Attack at dawn"
    plaintext = append_space_padding(plaintext)
    print(len(plaintext))

    ciphertext = encrypt(plaintext, key)
    print(binascii.hexlify(bytearray(ciphertext)))

    decrypted = decrypt(ciphertext, key)
    decrypted = remove_space_padding(decrypted)
    print(decrypted)