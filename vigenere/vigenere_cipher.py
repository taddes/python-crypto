"""Vigenere Cipher Implementation"""

# Note that whitespace is included in alphabet string
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ''
    key_index = 0

    for char in plain_text:
        # Number of shifts = index of the char in alphabet + index of the char in the key
        index = (ALPHABET.find(char) + (ALPHABET.find(key[key_index]))) % len(ALPHABET)
        cipher_text += ALPHABET[index]
        key_index += 1

        # If we've considered the last letter of the key, we start again
        if key_index == len(key):
            key_index = 0

    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()

    plain_text = ''
    key_index = 0

    for char in cipher_text:
        index = (ALPHABET.find(char) - (ALPHABET.find(key[key_index]))) % len(ALPHABET)
        plain_text += ALPHABET[index]

        key_index += 1

        if key_index == len(key):
            key_index = 0

    return plain_text

if __name__ == "__main__":
    encrypted = vigenere_encrypt('The world is so small yet so large', 'SPACEMAN')
    print(encrypted)
    print(vigenere_decrypt(encrypted, 'SPACEMAN'))