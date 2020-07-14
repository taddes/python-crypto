# One Time Pad - Vernam Cipher
* This cryptosystem uses as many letters in the key as the length of the plaintext (yet this is not sufficient, as it would be vulnerable to frequency analysis). This necessitates using totally *random numbers* to shift the letters in the plain text, thereby reducing information leaking.
* **Key must be of the same length as the plaintext** & **Key must contain random numbers**
* First constructed by Frank Miller in 1882. Very difficult to crack due to enormous keyspace.
* Generally quite inconvenient and inefficient to use, so not commonly used as a cryptosystem.

### Algorithm
1. Generate a truly random sequence (as many random numbers as the letters in the plaintext). Private key will only be used once; must not reuse the same numbers or seeds as it could result in information leakage.
    * One time pad originally used *XOR operation*, so we must convert all digits into their binary representations. **Find ASCII value for every letter, then convert to binary**. ASCII has 256 (0-255) characters each coresponding to an integer. Summation of each binary digit in the 8-bit formula as follows produces result:
    Ex. a is ASCII 97 == 01100001<br>
    01100001 = 1x2^0 + 0x2^2 + 0x2^2 + 0x2^3 + 0x2^4 + 1x2^5 + 1x2^6 + 0x2^7 = 97
    * Key size is relative to the number of characters: 5 characters x 8-bits = 40-bits
2. Create a key of random numbers
3. Shift the letters in the plaintext with the random numbers/key of the key in the same manner as Caesar or Vigenere. Apply a random sequence of numbers to each character, and based on that number plus the character number, that becomes your new character. **Ei(xi) = (xi + OTPi) % char_length**

### XOR
**Exclusive OR operation**
| X | Y | X XOR Y |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |

* Output of 0 or 1 is with 50% probability!
* One Time Pad (OTP) uses XOR bitwise operation; it is an involution so that the function's inverse is the function itself.
* Bitwise XOR is the same as addition (if there are no carry bits), since we want to shift every letter in the plaintext.

### Random Numbers vs Pseudo-Random Numbers
* The main problem as far as the one time pad is concerned is how to generate truly random numbers.
* *Random number generation is the generation of a sequence of numbers that cannot be reasonably predicted in any way, other than by random chance.*
#### True randomness:
* Radioactive decay, mouse movement, atomspheric noice.
* Values have uniform distribution
* Values are independent of each other
* Not efficient: expensive to generate
#### Pseudo-randomness:    
* Computers are deterministic and can repeat themselves; it is difficlut/impossible to define algorithms to generate true random numbers.
* For example, you can use middle-square method, Marsenne twister or linear congruential generators.
* Values have a uniform distribution.
* Values are not independent of each other.
* There are efficient algorithms that generate pseudo-random values.

#### Middle Square Method
* Input of the algorithm is a **seed**, the starting point that determines a pseudo-random sequence.  This seed *is the input of a simple calculation*, like the measurement of noise or current time in milliseconds.
* Randomness of the sequence depends on the randomness of the seed.  If initial state is random, sequence is random. If initial state is predictable, the sequence is predictable.
* If the algorithm reaches a seed it previously used, then the sequence will keep repeating itself. This is called a **period**, the length of a pseudo-random sequence before it repeats itself.  The period depends on the initial seed exclusively. **N digits seed: algorithm uses 10^N digits before reusing seed**.
    * 2 digit seed: algorithm uses at most 100 digits before reusing seed.
    * 3 digit seed: algorithm uses at most 1000 digits before reusing seed.
* If the key-space is reduced to a much smaller one by the period/seed-space, meaning the one time pad is less secure
* Invented by John von Neumann in 1949.

1. Multiply the seed by itself.
2. Get the middle of the result.
3. The result is the seed in the next iteration.

```
Ex. seed = 152
152 x 152 = 23104

seed = 310
310x310 = 96100

seed = 610
610x610 = 372100

seed = 210
210x210 
Sequence is: 310610210
```
#### Linear Congruential Generator
**x n+1 = (a Xn + c) mod m**


