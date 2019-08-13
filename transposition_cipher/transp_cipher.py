import pyperclip

def main():
    my_message = 'Common sense is not so common.'
    my_key = 8

    ciphertext = encrypt_message(my_key, my_message)
    # Print encrypted ciphertext to screen with a | ('pipe') delimeter to indicate end of message
    print(ciphertext + '|')

    # Copy the ciphertext to clipboard
    pyperclip.copy(ciphertext)


def encrypt_message(key, message):
    


if __name__ == '__main__':
    main()