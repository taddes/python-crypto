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
    # Creates empty ciphertext list corresponding to key
    # with a length of n-1, being the key of the cipher -1 to index from 0.
    ciphertext = [''] * key

    # Loop through each column in the cipher text 
    for column in range(key):
        current_index = column

        # Keep looping until current_index goes past message length
        while current_index < len(message):
            # Place char at current_index in message at the end of current column in the ciphertext list
            ciphertext[column] += message[current_index]
            # Move current_index over by adding key value
            current_index += key
    
    return ''.join(ciphertext)


if __name__ == '__main__':
    main()