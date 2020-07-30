"""
    An advanced implementation of Caeser Cipher using Ascii characters
    and substitution tables, created for each message. This is a more
    performant method of implementing the cipher.
"""
import string

def create_shift_substitutions(n):
    """
        Function to create two encoding/decoding key dictionaries
        n is the shift parameter/key
    """
    encoding = {}
    decoding = {}

    alphabet_size = len(string.ascii_uppercase)

    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        subst_letter = string.ascii_uppercase[(i+n) % alphabet_size]
        encoding[letter] = subst_letter
        decoding[subst_letter] = letter

    return encoding, decoding


def encode(message, subst):
    cipher = ""

    for letter in message:
        if letter in subst:
            cipher += subst[letter]
        else:
            cipher += letter
    
    return cipher

def encode_concice(message, subst):
    return ''.join(subst.get(x, x) for x in message)

def decode(message, subst):
    return encode(message, subst)

def printable_substitution(subst):
    """Sort by source character so result is alphabetized"""
    mapping = sorted(subst.items())

    alphabet_line = ' '.join(letter for letter, _ in mapping)
    cipher_line = ' '.join(subst_letter for _, subst_letter in mapping)
    return f'{alphabet_line}\n{cipher_line}'


if __name__ == "__main__":

    while True:
        try:
            n = int(input('Enter an integer for the key: '))
        except TypeError as e:
            print(f'Must be an integer value.')
        except ValueError as e:
            print(f'Must be an integer value.')
        else:
            encoding, decoding = create_shift_substitutions(n)
            break

    while True:
        print("\nShift Encoder Decoder")
        print("--------------------")
        print("\tCurrent Shift: {}\n".format(n))
        print("\t1. Print Encoding/Decoding Tables.")
        print("\t2. Encode Message.")
        print("\t3. Decode Message.")
        print("\t4. Change Shift")
        print("\t5. Quit.\n")
        choice = input(">> ")
        print()

        if choice == '1':
            print('Encoding Table:')
            print(printable_substitution(encoding))
            print('Decoding Table')
            print(printable_substitution(decoding))
        
        elif choice == '2':
            message = input('\nMessage to encode: ')
            print(f'Encoded message: {encode(message.upper(), encoding)}')

        elif choice == '3':
            message = input('\nMessage to decode: ')
            print(f'Decoded Message: {decode(message.upper(), decoding)}')

        elif choice == '4':
            new_shift = input(f'\nNew shift (currently {n}): ')
            try:
                new_shift = int(new_shift)
                if new_shift < 1:
                    raise Exception('Shift must be greater than 0')
            except ValueError:
                print(f'Shift {new_shift} is not a valid number')
            else:
                n = new_shift
                encoding, decoding = create_shift_substitutions(n)

        elif choice == '5':
            print('Terminating. This program will self destruct in 5 seconds...\n')
            break
        
        else:
            print(f'Unknown option {choice}')