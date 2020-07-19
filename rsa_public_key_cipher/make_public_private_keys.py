"""
    Public Key Generator using textbook RSA
"""
import random
import sys
import os
import prime_num
import crypto_math

def main():
    """
        Create a private/public key pai with 1024-bit keys
    """
    print('Generating keys')
    

def make_key_files(name, keysize):
    """
    Creates two files "x_pubkey.txt" and "x_privkey.txt" (where x
    is the value in name) with the n, e and d, e integers written in 
    them, delimited by comma
    """
    if os.path.exists(f'{name}_pubkey.txt') or os.path.exists(f'{name}_privkey.txt'):
        sys.exit('''WARNING: The public/private key already exists. Use a different 
        name or delete these files to rerun the program''')



if __name__ == '__main__':
    main()