"""One-Time Pad Cipher Implementation"""

from random import randint
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    cipher_text = ''

    for index, char in enumerate(plain_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]

    return cipher_text

def decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    plain_text = ''

    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain_text += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    return plain_text


def random_sequence(plain_text):
    """Generate random sequence for key"""
    rand_seq = []
    # Generate as many random values as the number of chars in the plain_text
    # size of the key == size of the plain_text
    for rand in range(len(plain_text)):
        rand_seq.append(randint(0, len(ALPHABET)))

    return rand_seq