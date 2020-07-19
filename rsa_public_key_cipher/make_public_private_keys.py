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
    
def generate_key(keysize):
    """Creates public/private keys"""
    p = 0
    q = 0

    # 1. Create two prime numbers, p and q, calculate n = p * q
    print('Generating p prime')
    while p == q:
        p = prime_num.generate_large_prime_number(keysize)
        q = prime_num.generate_large_prime_number(keysize)

    n = p * q

    # 2. Create e, that is relatively prime to (p - 1)  * (q -1)
    print('Generating e that is relatively prime to (p-1) * (q-1')

    while True:
        # Keep trying random numbers for e until one is valid
        e = random.randrange(2 **(keysize - 1), 2 ** (keysize))
        if crypto_math.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # 3. Calculate d, the mod inverse of e
    print('Calculating d, modular inverse of e.')
    d = crypto_math.find_mod_inverse(e, (p - 1) * (q - 1))

    public_key = (n, e)
    private_key = (n, d)

    return (public_key, private_key)
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