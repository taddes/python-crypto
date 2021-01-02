import math, pyperclip

def main():
    my_message = 'Tn, thoo tie tthorb henfeta ,u otq co  umkrbieo! esst'
    my_key = 9

    plaintext = decrypt_message(my_key, my_message)

    # Print with '|' at end of message in case there are spaces at end
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decrypt_message(key, message):
    """Simulate the columns and rows of the frid that plaintext is written on, using alist of strings"""
    # Columns in transposition grid
    num_of_columns = int(math.ceil(len(message) / float(key)))
    # Rows in transposition grid
    num_of_rows = key
    # Shaded or empty spaces in the last column of the grid
    num_of_deadspace = (num_of_columns * num_of_rows) - len(message)
    # Each string in plaintext represents a column in transposition grid
    plaintext = [''] * num_of_columns
    # Column and row variables point to where in the grid the net char in message will go
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next col

        # If there are no more columns or we're at an eunused space, go back to first col and the next row
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_deadspace):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()


  