# Caeser-Cipher

* Private key encryption (symmetric) method.
* A form of simple *substitution cipher*.
* Each single letter in plaintext is shifted by the same key (rotation).
* The key itself is the number of letters we use for shifting.
* Have to consider wraparound, once you go past 26 characters of the alphabet.

## Process
* Assign numerical values to every letter in the alphabet to be able to use mathematical operations during encryption/decryption


* Can be easily brute forced: 
    * Use of every possible decryption key to crack a cipher. Effective on rather simple encryptions, harder on more complex.
    * Augustine Kerckhoff (19th-C cryptographer): *"A cipher should be secure even if everyone knows how the cipher works."*
