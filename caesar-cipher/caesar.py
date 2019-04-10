"""
    Caeser Cipher requires an encrpytion key, related to alphabet index integers from 0-25 to encrypt and decrypt messages.
"""
import pyperclip

# String to be encrypted
message = 'This message will test the power of encryption'
message = 'guv6 zr66ntr 0vyy 7r67 7ur 320r5 2s r1p5!37v21'

# Encrpytion / Decryption Key
key = 13

# Whether operation should encrypt or decrypt
mode = 'decrypt' #set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?'

# Translated -> Store the encrypted/decrypted message
translated = ''

for symbol in message:
    # NOTE only symbols in the SYMBOLS constant can be encrypted/decrpyted
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption.decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex + key

        # Handle wraparound, if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = symbolIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    
    else:
        # Append the symbol without encrypting or decrypting:
        translated = translated + symbol

# Output translated string
print(translated)
pyperclip.copy(translated)



