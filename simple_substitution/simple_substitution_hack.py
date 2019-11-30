'''Hacking the Simple Substitution Cipher'''


import os
import re
import copy
import pyperclip
import simple_substitution
import wordPatterns
import makeWordPatterns


LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
non_letters_or_space_pattern = re.compile('[^A-Z\s]')

def main():
    message = '''Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr
    sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa
    sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac
    ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx
    Hacking the Simple Substitution Cipher 227
    lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia
    rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh.
    -Facjclxo Ctrramm'''

    # Determine possible valid ciphertext translations:
    print('Hacking...')
    letter_mapping = hack_simple_sub(message)

    # Display results to user
    print('Mapping:')
    print(letter_mapping)
    print()
    print('Original Ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard...')
    hacked_message = decrypt_with_cipher_letter_mapping(message, letter_mapping)
    pyperclip.copy(hacked_message)
    print(hacked_message)


def get_blank_cipher_letter_mapping():
    # Returns a dictionary value that is a blank cipherletter mapping:
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
            'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
            'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
            'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def add_letters_to_mapping(letter_mapping, cipherword, candidate):
    '''
    This function adds the letters in the candidate as potential
    decryption letters for teh cipherletters in the cipherletter mapping.

    letter_mapping parameter takes a dictionary value that
    stores a cipherletter mapping, which is copied by the function.
    The cipherword parameter is a possible English word that the 
    cipherword could derypt to.
    '''

    for i in range(len(cipherword)):
        if candidate[i] not in letter_mapping[cipherword[i]]:
            letter_mapping[cipherword[i]].append(candidate[i])


def intersect_mappings(mapA, mapB):
    '''
    To intersect two maps, create a blank map and then add only
    the potential decryption letters if tehy exist in BOTH maps
    '''
    intersected_mapping = get_blank_cipher_letter_mapping()
    for letter in LETTERS:
        # An empty list means any letter is possible. In this case,
        # just copy the other map entirely
        if mapA[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersected_mapping[letter] = copy.deepcopy(mapA[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter],
            # add that letter to intersectedMapping[letter]
            for mapped_letter in mapA[letter]:
                if mapped_letter in mapB[letter]:
                    intersected_mapping[letter].append(mapped_letter)
    
    return intersected_mapping




if __name__ == '__main__':
    main()