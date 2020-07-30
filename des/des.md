# Data Encryption Standard (DES)

* Met the need for encryption in the commercial sector in the 1970's. Developed at IBM by Horst Feistel.
* **Symmetric Block Cipher**, where plaintext is processed to ciphertext in blocks. 64-bit chunk of plaintext/binary in a data stream encrypted, resulting in a 56-bit key, which has an 8-bit drop-off.
* Hybrid of a substitution and permutation cipher. **SD Network**
* No longer used because it is crackable with modern methods. Was replaced by Triple-DES

**Feistel-Structure**
1. Split the plaintext into 64 bit long blocks (the input for 16 rounds of encryption).
2. There are so-called rounds/iterations during the encryption/decryption (16 rounds in DES: substitution/XOR operations).
3. Every round needs a different subkey, which are based off of the original 64-bit private key.
4. Main advantage is that encryption and decryption operations are similar (requiring only a reversal of the key schedule).

Block Size: 64-bits
Key Size: 64-bits (56-bits relevant used in algorithm)
Rounds: 16
Subkeys: 16; each subkey being 48-bits
Ciphertext size: 64-bits