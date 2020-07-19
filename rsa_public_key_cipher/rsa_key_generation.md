# RSA Public & Private Key Generation
Each key in the public/asymmetric key scheme is made of two numbers. The public key will be the two numbers n and e. The privat eky will be the two numbers n and d.
1. Create two random, distinct, large prime numbers p and q. Multiply these two numbers to get a number n.
2. Create a random number called e, which is relatively prime to (p - 1) x (q - 1)
3. Calculate the modular inverse of e, which will be d
* n is used in both keys. d must be kepy secret because it is the private key and can decrypt messages.