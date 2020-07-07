"""Dictionary-analysis crack for Caesar-Cipher"""
import caesar_cipher
import brute_force_caesar

# Note that whitespace is included in alphabet string
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ENGLISH_WORDS = {}

def get_data():
    with open('words.txt', 'r') as readfile:
        for idx, word in enumerate(readfile.read().split('\n')):
            ENGLISH_WORDS.update({idx:word})



def count_words(text):
    """Function to count English words """
    text = text.upper()
    words = text.split()
    matches = 0

    for word in words:
        if word in ENGLISH_WORDS.values():
            matches += 1

    return matches

def is_text_english(text):
    """Determines if words within decrypted message are english"""
    matches = count_words(text)
    if (float(matches) / len(text.split('\n'))) * 100 >= 80:
        return True
    return False

if __name__ == "__main__":
    get_data()

    encrypted = caesar_cipher.caesar_encrypt('Where oh where has the old dog gone oh where oh where could he be', 15)
    brute_forced_values = brute_force_caesar.caesar_brute_crack(encrypted)
    for crack in brute_forced_values:
        print(crack)
        if is_text_english(crack['result']) == True:
            print(f'Verified English for crack: Key : {crack["key"]} {crack["result"]}')