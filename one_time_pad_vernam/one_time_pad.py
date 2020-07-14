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
    for _ in range(len(plain_text)):
        rand_seq.append(randint(0, len(ALPHABET)))

    return rand_seq

if __name__ == "__main__":
    plain_text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
    key = random_sequence(plain_text)
    cipher_text = encrypt(plain_text, key)
    print(cipher_text)
    decrypted_text = decrypt(cipher_text, key)
    print(decrypted_text)