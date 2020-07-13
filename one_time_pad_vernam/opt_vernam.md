# One Time Pad - Vernam Cipher
* This cryptosystem uses as many letters in the key as the length of the plaintext (yet this is not sufficient, as it would be vulnerable to frequency analysis). This necessitates using totally *random numbers* to shift the letters in the plain text, thereby reducing information leaking.
* **Key must be of the same length as the plaintext** & **Key must contain random numbers**
* First constructed by Frank Miller in 1882.

### XOR
* One Time Pad (OTP) uses XOR bitwise operation; it is an involution so that the function's inverse is the function itself.
* This operation shifts every letter in the plaintext in an additive manner, whcih is the same as bitwise XOR (if there are no carry bits)

### Random Numbers vs Pseudo-Random Numbers

### Algorithm
1. Generate a truly random sequence (as many random numbers as the letters in the plaintext). Private key will only be used once; must not reuse the same numbers or seeds as it could result in information leakage.
    * One time pad originally used *XOR operation*, so we must convert all digits into their binary representations. **Find ASCII value for every letter, then convert to binary**. ASCII has 256 (0-255) characters each coresponding to an integer. Summation of each binary digit in the 8-bit formula asd follows produces result:
    Ex. a is ASCII 97 == 01100001
    01100001 = 1x2^0 + 0x2^2 + 0x2^2 + 0x2^3 + 0x2^4 + 1x2^5 + 1x2^6 + 0x2^7 = 97


2. Shift the letters in the plaintext with the random numbers of the key in the same manner as Caesar or Vigenere.