# Data Encryption Standard (DES)

* Met the need for encryption in the commercial sector in the 1970's. Developed at IBM by Horst Feistel.
* **Symmetric Block Cipher**, where plaintext is processed to ciphertext in blocks. 64-bit chunk of plaintext/binary in a data stream encrypted, resulting in a 56-bit key, which has an 8-bit drop-off.
* Hybrid of a substitution and permutation cipher. **SD Network**
* No longer used because it is crackable with modern methods. Was replaced by Triple-DES

**Feistel-Structure**
1. Split the plaintext into 64 bit long blocks (the input for 16 rounds of encryption), with each 64 bit block being broken into right and left halves of 32-bits, and the private key is of two 28-bit chunks.
2. There are so-called rounds/iterations during the encryption/decryption (16 rounds in DES: substitution/XOR operations).
3. Every round needs a different subkey, which are based off of the original 64-bit private key.
4. Main advantage is that encryption and decryption operations are similar (requiring only a reversal of the key schedule).

Block Size: 64-bits
Key Size: 64-bits (56-bits relevant used in algorithm)
Rounds: 16
Subkeys: 16; each subkey being 48-bits
Ciphertext size: 64-bits

### Circular Shift (Bitwise Rotation)
* Operator that shifts all the bits, either right or left. A shift of `0100100` to the left results in: `10010000`. Most significant digit is the one on the left, shifted to the place of the least significant digit.
* In DES, we sometimes have to shift by 1 and sometimes by 2.

### S-Boxes
**"Substitution Boxes"**
* Runtime complexity of O(1) - Constant Time.
* Essentialy lookup tables/Hash Table/Dictionary: 6-bit input defines the row and column index in the given s-box and the value associated with that index yields a 4-bit output.
* There are 8 s-boxes in DES. The input for the boxes is 6-bits and the output is 4-bits.
* 48-bit input (8x6)/32-bit output (8x4) total.
* Each s-box contains 64 items.

### Decryption
* Same function with encryption, except that subkeys are used in reverse order: **start with the last (16th subkey)**. Subkeys can be generated with circular left shift operations. Usually in the implementation we generate all 16 subkeys at the start.

## Breaking DES
* Primary weakness: DES keyspace is 2^56, which makes it susceptible to Brute Force cracking.
* *DeepCrack* managed to crack DES within 22 hours. It does not use any internal structure of the cryptosystem, it just considered all the possible keys using linear search.
* Due to this vulnerability, DES was replaced by 3Des or Triple Des, followed by AES. 3DES uses 3 rounds, so 3 private keys, 3x16 = 48 rounds, therefore a much larger key space.