"""Program to Encrypt/Decrypt Text Files"""

import time, os, sys, transposition_encrypt, transposition_decrypt

def main():
    input_filename = 'frankenstein.txt'
    # input_filename = 'frankenstein.encrypted.txt'
    output_filename = 'frankenstein.encrypted.txt'
    # output_filename = 'frankenstein.decrypted.txt'
    my_key = 10
    my_mode = 'encrypt'
    # my_mode = 'decrypt'

    # If input does not exist, exit program
    if not os.path.exists(input_filename):
        print('The file %s does not exist. Quitting...' % (input_filename))
        sys.exit()

    # If filename exists, give user a change to exit
    if os.path.exists(output_filename):
        print(f'The file {input_filename} already dxists. This will overwrite the file. (C)ontinue or (Q)uit?')
        response = input('>')
        if not response.lower().startswith('c'):
            sys.exit() 

    # Read in the message from input file
    file_obj = open(input_filename)
    content = file_obj.read()
    file_obj.close()

    print(f'Closing {input_filename.title()}')

    # Initiate and Measure how long the encrpytion/decryption takes
    starttime = time.time()
    if my_mode == 'encrypt':
        translated = transposition_encrypt.encrypt_message(my_key, content)
    elif my_mode == 'decrypt':
        translated = transposition_decrypt.decrypt_message(my_key, content)
    totaltime = round(time.time() - starttime, 2)
    print('%sion time: %s seconds' % (my_mode.title(), totaltime))

    # Write out translated message to output file
    output_file_object = open(output_filename, 'w')
    output_file_object.write(translated)
    output_file_object.close()

    print('Done %sing %s (%s characters).' % (my_mode, input_filename, len(content)))
    print('%sed file is %s' % (my_mode.title(), output_filename))

if __name__ == '__main__':
    main()