# Vigenere Cipher
* The Vigenere cryptosystem is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.
* *Polyalphabetic Substitution*  that uses several keys.
* The numerical representations of the letters of the secret key define how many characters of the plaintext should be shifted.
* Significantly larger keyspace.  
    * The size of the keyspace is the number of characters in the alphabet (or range) to the power of the length of the key. 
    * Ex. S  E C  R E  T
      18 4 2 17 4 19
      **Assuming 26 Char alphabet: 26^6 = *26,000,000***
* A 16th Century Cipher considered to be unbreakable in its day.

## Implementation
* Similar formula to that of Caesar Cipher.
* Overlay the recurring multi-letter key and its numerical index over each plaintext/ciphertext letter and then +/- the key.

### Encryption
**Ei(xi) = (xi + Ki) mod 26 (or alphanum len)**
* xi is the actual letter in plaintext
* Ei(xi) is the encrypted letter in the ciphertext
* The i-th letter of the key must be used for encrypting the i-th letter. In other words, in a key composed of many indexes of letters, each key index should be successively used.
* Modulo must again be used to get remainder if wraparound occurs.

### Decryption
**Di(xi) = (xi - Ki) mod 26 (or alphanum len)**
* xi is the actual letter in ciphertext
* Di(xi) is the decrypted letter in the ciphertext
* The i-th letter of the key must be used for decrypting the i-th letter. In other words, in a key composed of many indexes of letters, each key index should be successively used.

