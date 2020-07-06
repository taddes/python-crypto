# Caeser-Cipher

* Private key encryption (symmetric) method.
* A form of simple *substitution cipher*.
* Each single letter in plaintext is shifted by the same key (rotation).
* The key itself is the number of letters we use for shifting.
* Have to consider wraparound, once you go past 26 characters of the alphabet (0-25) or 256 ASCII characters!

## Process
* Assign numerical values to every letter in the alphabet to be able to use mathematical operations during encryption/decryption.
* Shift the letters by the numeric key, corresponding to the character set (taking into account wrap around).
* Use modulo operation to capture remainder should the value exceed the total alphabet size.

## Formula
### Encryption
**En(x) = (x+n) mod 26**
* Where En(x) is the encrypted letter of the original x letter
* Where x + n is the numeric index of the letter, plus the key shift value (Range [0,SIZE_ALPHABET - 1])
* Mod % used to match the length of the character set (0-25 is 26)

### Decryption
**Dn(x) = (x-n) mod 26**
* Where Dn(x) is the decrypted letter of the original x ciphertext.
* Have to shift the given letter with -n (where n is the key) 
* Range [0,SIZE_ALPHABET - 1])

## Effectiveness & Problems
* Keyspace is small, only 26 keys! Very weak encryption.
* Information leaking, due to the cryptosystem revealing information about both the recurrance of numbers/letters and their distribution. To remedy this, you'd have to use random numbers via *OTP - One Time Pads*.
* Repetitive iterations of encryption will not strengthen encryption. An encryption of 2 follwed by an encryption of 3 is only an encryption of 5. Any additional encrpyptions are simply additive to key. 

### Brute Force
* Can be easily *brute forced*
    * Use of every possible decryption key to crack a cipher. Effective on rather simple encryptions, harder on more complex ciphertext. 
    * Brute force best when keyspace is small.

### Frequency Analysis
* Can be easily broken using *frequency analysis* (recurrance of common letters, E, A, O, I, T)
    * Analyze the frequency distribution of letters in the ciphertext.
    * key = value of ciphertext's most frequent letter (E).
    * Shifting the key alters the letters, but not the distribution/recurrance of letters.
    * Augustine Kerckhoff (19th-C cryptographer): *"A cipher should be secure even if everyone knows how the cipher works."*

1. Calculate the relative frequency distribution of ciphertext letters.
2. Get the most frequent letter in the ciphertext (or second, because the most frequent may be whitespace).
3. Intuit key from distribution.



