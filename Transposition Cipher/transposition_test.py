"""Application to test encryption and decryption using the Columnar Transposition Cipher"""

import random, sys, transposition_decrypt, transposition_encrypt

def main():
    print('Initializing Transposition Cipher Test.')
    print('Generating and testing random messages.')
    random.seed(42) # set random seed to a static value

    for i in range(20):
        # Generate random messages to test.
        message = 'ABCDEFGHIJKLMNOPQUSTUVWXYZ' * random.randint(4, 40)
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possibl keys for each message
        for key in range(1, int(len(message)/2)):
            encrypted = transposition_encrypt.encrypt_message(key, message)
            decrypted = transposition_decrypt.decrypt_message(key, encrypted)

            # If decryption doesn't match original message, display an error and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed')


if __name__ == '__main__':
    main()