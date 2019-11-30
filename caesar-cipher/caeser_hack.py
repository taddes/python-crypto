"""
Implementation of how to hack the Caeser Cipher with brute force
"""
import timeit

message = 'QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD LC ZXBPXO XKA VLRO RKFNRB PLIRQFLK FP DZMODJKJBOIK'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


def crack_caesar(message, symbols):
# Iterate through all possible keys
    for key in range(len(SYMBOLS)):
        # Important is to set translated to the blank string so that the previous interation value for translation is cleared
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                  symbol_index = SYMBOLS.find(symbol)
                  translated_index = symbol_index - key

                  # Handle circling back past final symbols
                  if translated_index < 0:
                      translated_index = translated_index + len(SYMBOLS)

                  # Append the decrypted symbol
                  translated = translated + SYMBOLS[translated_index]

            else:
                # Append symbol without encrypting/decrypting
                translated = translated + symbol

        print('Key #%s: %s' % (key, translated))

crack_caesar(message, SYMBOLS)