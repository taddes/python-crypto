"""Affine Cipher"""
import sys
import random

import pyperclip
import crypto_math

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def main():
    my_message = """A computer would deserve to be called intelligent if it could deceive a human into believing that it was human. 
    -Alan Turing"""
    my_key = 2894
    my_mode = 'encrypt'
    # my_mode = 'decrypt'

    if my_mode == 'encrypt':
        translated = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)
    print('Key: %s' % (my_key))
    print('%sed text: ' % (my_mode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (my_mode))

def get_key_parts(key):
    key_a = key // len(SYMBOLS)
    key_b = key % len(SYMBOLS)
    return (key_a, key_b)


def check_keys(key_a, key_b, mode):
    if key_a == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if key A is 1. Choose a different key.')
    if key_b == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if key B is 0. Choose a different key.')
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    if crypto_math.gcd(key_a, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (key_a, len(SYMBOLS)))



def encrypt_message(key, message):
    key_a, key_b = get_key_parts(key)
    check_keys(key_a, key_b, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symbol_index * key_a + key_b) % len(SYMBOLS)]
        else:
            ciphertext += symbol # Append symbol without encrypting
    return ciphertext


def decrypt_message(key, message):
    key_a, key_b = get_key_parts(key)
    check_keys(key_a, key_b, 'decrypt')
    plaintext = ''
    mod_inverse_of_key_a = crypto_math.find_mod_inverse(key_a, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symbol_index - key_b) * mod_inverse_of_key_a % len(SYMBOLS)]
        else:
            plaintext += symbol # Append symbol without encrypting
    return plaintext


def get_random_key():
    while True:
        key_a = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))
        if crypto_math.gcd(key_a, len(SYMBOLS)) == 1:
            return key_a * len(SYMBOLS) + key_b
        

if __name__ == '__main__':
    main()