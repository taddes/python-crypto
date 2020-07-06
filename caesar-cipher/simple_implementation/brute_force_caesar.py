"""Brute-force crack for Caesar-Cipher"""
import caesar_cipher
# Note that whitespace is included in alphabet string
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_brute_crack(cipher_text):
    for key in range(len(ALPHABET)):

        # Initialize each crack pass as empty str
        plain_text = ''

        for char in cipher_text:
            index = ALPHABET.find(char)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]
