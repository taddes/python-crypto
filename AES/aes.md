# AES - Advanced Encryption Standard
* Originally Rijndael, by Vincent Rijmen and Joan Daemen. Named partly after Rivindell from Lord of the Rings. Invented in 2001 and remains the most state-of-the-art cryptosystem to this day. Was the result of a competion run by NIST to find the most robust, modern cryptosystem. 
* Private Key (Symmetric Cipher) with 3 key lengths:
  * 128-bit : 10 rounds
  * 192-bit : 12 rounds
  * 256-bit : 14 rounds
* Stores values (plaintext, key, ciphertext) in matrix form.

### Block
* Plaintext block - 128-bit (4 words, as 1 word is 32 bits)
  * 4x4 matrix, total of 16 blocks, where each matrix entry is a byte (8-bits).
  * Each column (32-bits) represents a single word 
* Key size: 128-bits
* Subkeys: 10 subkeys (1 for each round)
  * 1 subkey per round plus original 128-bit key before applying round function
* Ciphertext block: 128-bits
* Data in matrix handled in a column by column basis. Count up from leftmost, top column.

### Algorithm
1. Input 128-bit plaintext block & 128-bit private key.
  * Subkey Generation:
  * Rotation operation which means binary shift left, but in this case we shift every byte up  one step in a circular manner. Then use S-box for each byte (4-bit row index, 4-bit col index)
  * Use XOR operation with previous words in teh key and the values in the rcon table (round constant table), which is a lookup table.
2. Add Round Key Operation:
    * XOR bitwise operation between key and plaintext 
    * **NOTE**: because XOR has a 50% probability of being 1 or 0, it is close to random, hence it is strong! More options would not necessarily be better, due to pseudo-random generation possibly making detectable patterns.
3. S-BOX:
* S-Box values are carefully chosen to be resistant to linear and differential cryptoanalysis.

| P1 | P5 | P9  | P13 |
|----|----|-----|-----|
| P2 | P6 | P10 | P14 |
| P3 | P7 | P11 | P15 |
| P4 | P8 | P12 | P16 |

  * 128-bit input. 2 dimensional array of 8-bits each, applying s-box logic to each. 4-bits for row index, 4-bits for column index. 0101 1100 row index first 4, column index last 4.
  * Matrix total of 128-bits, each column being 32-bits. 
  * 8-bit input results in 8-bit output

4. Shift Rows Operation (Circular Left Shift)

| S0 | S4 | S8  | S12 |
|----|----|-----|-----|
| S1 | S5 | S9  | S13 |
| S2 | S6 | S10 | S14 |
| S3 | S7 | S11 | S15 |

* After S-box, we create an intermediate result matrix and apply a Circular Left Shift of bits.
  * First row: shift 0 steps (stay the same: S0, S4, S8, S12)
  * Second row: shift 1 step (S5, S9, S13, S1)
  * Third row: shift 2 steps (S10, S14, S2, S6)
  * Fourth row: shift 3 steps (S15, S3, S7, S11)

  Result: 
  | S0  | S4  | S8  | S12 |
  |-----|-----|-----|-----|
  | S5  | S9  | S13 | S1  |
  | S10 | S14 | S2  | S6  |
  | S15 | S3  | S7  | S11 |

5. Mix Columns Operation - Matrix Vector Multiplication
* Take the columns from the state-matrix and multiply the predifined matrix with these vectors. Result is referred to the **Galois-field**
* Addition is the XOR operation
* Multiplication of a binary sequence by 3 is approximately the left shift binary operation.

Pre-defined Matrix
| 2 | 3 | 1 | 1 |
|---|---|---|---|
| 1 | 2 | 3 | 1 |
| 1 | 1 | 2 | 3 |
| 3 | 1 | 1 | 2 |

6. Mix Columns
**NOTE: This operation is not done in the last round of rounding.**

7. Add Round Key
**EACH ROUND GETS ITS UNIQUE SUBKEY**
Add Round Key Operation:
    * XOR bitwise operation between state-matrix and subkey 
    * **NOTE**: because XOR has a 50% probability of being 1 or 0, it is close to random, hence it is strong! More options would not necessarily be better, due to pseudo-random generation possibly making detectable patterns.


### Claude Shannon's Confusion and Diffusion
* Since AES keyspace is 2^256, it's not feasible to crack AES with brute force.

Properties of a secure cipher:
1. **Confusion**:  each binary digit of the ciphertest should depend on several digits of the private key. We want the relationship between input and output to be as complex as possible. The ciphertest should give no clue about the plaintext; this is why non-linear transformations are preferred, which destroy patterns in the plaintext (S-Boxes).
2. **Diffusion**: if we chance a single bit in the input, then half of the digits in the output should change. There are 2 states (0 and 1), meaning a 50% of either choice, which introduces randomness. This is often referred to as the *avalanche effect*. Overall aim is to increase the redundancy of the input to obscure the statistical structure of the input so frequency analysis is not useful (Permutations - mix columns, shifts).
