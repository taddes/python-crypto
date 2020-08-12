from Crypto.Cipher import DES 
import binascii 

def append_space_padding(str, blocksize=64):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a' * pad_len
    return str + padding

def remove_space_padding(str, blocksize=64):
    pad_len = 0
    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break

        str = str[:-pad_len]
        return str

def encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plaintext)

def decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext).decode('UTF-8')

if __name__ == "__main__":
    key = 'secretaa'
    plaintext = 'This is where cats liek to yowl'