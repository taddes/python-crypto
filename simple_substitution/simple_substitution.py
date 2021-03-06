"""Simple Substitution Cipher"""

import sys
import random
import pyperclip


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    my_message = '''
    If a man is offered a fact which goes against his
    instincts, he will scrutinize it closely, and unless the evidence
    is overwhelming, he will refuse to believe it. If, on the other
    hand, he is offered something which affords a reason for acting
    in accordance to his instincts, he will accept it even on the
    slightest evidence. The origin of myths is explained in this way.
    -Bertrand Russell'''
    print(my_message)

    my_key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    my_mode = 'encrypt'
    # my_mode = 'decrypt'

    if not key_is_valid(my_key):
        sys.exit('There is an error in the key or symbol set.')
    if my_mode == 'encrypt':
        translated = encrypt_message(my_key, my_message)
    elif my_mode == 'decrypt':
        translated = decrypt_message(my_key, my_message)
    print('using key %s' % (my_key))
    print('The %sed message is: ' % (my_mode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('Message copied to clipboard')


def key_is_valid(key):
    '''Determine validity of key by comparing to possible characters'''
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    print(str(key_list == letters_list))
    return key_list == letters_list


def encrypt_message(key, message):
    return translate_message(key, message, 'encrypt')


def decrypt_message(key, message):
    return translate_message(key, message, 'decrypt')


def translate_message(key, message, mode):
    translated = ''
    chars_a = LETTERS
    chars_b = key
    if mode == 'decrypt':
        # For decrypting, we use the same code as encrpyting.
        # Just need to swap where the key and LETTERs strings used.
        chars_a, chars_b = chars_b, chars_a

    # Iterate through each symbol in message
    for symbol in message:
        if symbol.upper() in chars_a:
            # encrypt/decrypt symbol
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            # Symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()
