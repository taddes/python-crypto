# Note that whitespace is included in alphabet string
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3

def caesar_encrypt(plain_text, key=KEY):
    cipher_text = ''
    # Case insensitivity
    plain_text = plain_text.upper()
    
    for char in plain_text:
        index = ALPHABET.find(char)
        index = (index + KEY) % len(ALPHABET)
        # cipher_text = cipher_text + ALPHABET[index]
        cipher_text += ALPHABET[index]
    
    return cipher_text

def caesar_decrypt(cipher_text, key):
    plain_text = ''
    cipher_text = cipher_text.upper()

    for char in cipher_text:
        index = ALPHABET.find(char)
        index = (index-KEY) % len(ALPHABET)
        # plain_text = plain_text + ALPHABET[index]
        plain_text += ALPHABET[index]

    return plain_text


if __name__ == '__main__':
    encrypted = caesar_encrypt('There is no spoon', 12)
    print(f'Encrypted: {encrypted}')
    decrypted = caesar_decrypt(encrypted, 12)
    print(f'Decrypted: {decrypted}')
    