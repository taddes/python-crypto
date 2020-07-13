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

## Cracking the Vigenere Cipher
* Cracking Vigenere is challenging, because the complexity of cracking a cipher is proportional to the size of the keyspace. (Alphabet/Charset to power of the key length == 26^6 = 26,000,000)
* Can use a Dictionary Attack, but this would be an equally inefficient *Brute force attack*

* Best solution is **Kasiski-algorithm**
    * Constructed by Friedrich Kasiski in 1863, also discovered by Charles Babbage. 
    * If the key size is known, then frequency analysis can be applied to decrypt the ciphertext.
    * Takes advantage of some information leakage.
    * Example of *suffix tree* data structure to determine repeated substrings.

  ### Kasiski Implementaiton
  1. Find the key size: can analyze repeated substrings and their factors to get a good guess.
  2. Construct substrings from the ciphertext that are encrypted by the same letters.
  3. Use frequency analysis to find the letters of the key.

  * Size of the substrings should be at least 3 letters long.
  * Repeat instances of substrings mean the key and plaintext line up; same letter is possibly encrypted by the same key letters. *this also happens by accident, because the key and a different letter can result in the same ciphertext*


