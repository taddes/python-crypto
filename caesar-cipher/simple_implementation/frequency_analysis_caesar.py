"""Frequency-analysis crack for Caesar-Cipher"""
import caesar_cipher
import matplotlib.pylab as plt

# Note that whitespace is included in alphabet string
LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def frequency_analysis(text):
    text = text.upper()

    letter_frequency = {}
    for letter in LETTERS:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequency[letter] += 1

    return letter_frequency

def plot_distribution(letter_frequency):
    """
    Plot a histogram of the letter frequency pairs
    """
    centers = range(len(LETTERS))
    plt.bar(centers, letter_frequency.values(), align='center', tick_label=letter_frequency.keys())
    plt.xlim([0, len(LETTERS) - 1])
    plt.show()

if __name__ == "__main__":
    encrypted = caesar_cipher.caesar_encrypt('This is the best cat, because she has wide stripes and the finest paws', 5)
    freq_dist = frequency_analysis(encrypted)
    maxvalue = max(freq_dist, key=freq_dist.get)

    # print(plot_distribution(freq_dist))