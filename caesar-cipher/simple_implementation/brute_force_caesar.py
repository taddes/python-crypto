"""Brute-force crack for Caesar-Cipher"""
import caesar_cipher
# Note that whitespace is included in alphabet string
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_brute_crack(cipher_text):
    cracks = []
    for key in range(len(ALPHABET)):
        # Initialize each crack pass as empty str
        plain_text = ''

        for char in cipher_text:
            index = ALPHABET.find(char)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]

        cracks.append({
            'key': key,
            'result': plain_text
        })
    return cracks

if __name__ == "__main__":
    encrypted_message = 'WKHUHCLVCQRCVSRRQ'
    cracked = caesar_brute_crack(encrypted_message)
    for result in cracked:
        print(f'For Key of {result["key"]}, result is {result["result"]}')