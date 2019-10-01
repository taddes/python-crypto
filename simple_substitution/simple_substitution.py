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
if __name__ == '__main__':
    main()
